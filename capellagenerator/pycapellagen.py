import os
import subprocess
from pathlib import Path
import itertools
from functools import lru_cache
import multigen
import pyecore.ecore as ecore
from pyecore.resources import ResourceSet
from pyecoregen.ecore import EcoreGenerator, EcoreTask, EcorePackageInitTask, EcorePackageModuleTask
import pyecoregen.adapter as adapter


old_fix_name_clash = adapter.fix_name_clash

def fix_name_clash(value):
    value = old_fix_name_clash(value)
    if value in ('super', 'self'):
        # print(f"!! Fixing {value} in {value}_")
        value += '_'
    return value

adapter.fix_name_clash = fix_name_clash

ecore.eContainer = lambda: None


class CapellaPackageInitTask(EcorePackageInitTask):
    @classmethod
    def imported_classifiers_package(cls, p: ecore.EPackage):
        imported_dict = super(cls, cls).imported_classifiers_package(p)
        # Sorting EPackage by name
        return {k: v for k, v in sorted(imported_dict.items(), key=lambda x: x[0].name)}


class CapellaPackageModuleTask(EcorePackageModuleTask):
    @classmethod
    def imported_classifiers(cls, p: ecore.EPackage):
        imported_dict = super(cls, cls).imported_classifiers(p)
        circular_deps = CapellaModuleGenerator.identify_circular_inheritance(p)
        all_rejected = flat_list = [item for sublist in circular_deps.values() for item in sublist]
        for k, v in imported_dict.items():
            new_v = [x for x in v if x not in all_rejected]
            imported_dict[k] = new_v
        # Sorting EPackage by name
        return {k: v for k, v in sorted(imported_dict.items(), key=lambda x: x[0].name) if v}

    def create_template_context(self, element, **kwargs):
        context = super().create_template_context(element)
        context['circular_inheritances'] = CapellaModuleGenerator.identify_circular_inheritance(element)
        return context


class EcorePackageInitInc(EcoreTask):
    """Generation of package cross_init include file from Ecore model with Jinja2."""

    template_name = 'cross_init.inc.tpl'
    element_type = ecore.EPackage

    @staticmethod
    def filename_for_element(package: ecore.EPackage):
        return 'cross_init.inc'

    @staticmethod
    def imported_classifiers_package(p: ecore.EPackage):
        """Determines which classifiers have to be imported into given package."""
        classes = {c for c in p.eClassifiers if isinstance(c, ecore.EClass)}

        references = itertools.chain(*(c.eAllReferences() for c in classes))
        references_types = (r.eType for r in references)
        imported = {c for c in references_types if getattr(c, 'ePackage', p) is not p}

        imported_dict = {}
        for classifier in imported:
            imported_dict.setdefault(classifier.ePackage, set()).add(classifier)
        # Sorting EPackage by name
        return {k: v for k, v in sorted(imported_dict.items(), key=lambda x: x[0].name)}
        return imported_dict

    def create_template_context(self, element, **kwargs):
        return super().create_template_context(
            element=element,
            imported_classifiers_package=self.imported_classifiers_package(element),
            circular_inheritances=CapellaModuleGenerator.identify_circular_inheritance(element),
        )


class CapellaModuleGenerator(EcoreGenerator):
    templates_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'templates'
        )

    def __init__(self, package_root, *args, **kwargs):
        self.package_root = package_root
        super().__init__(*args, auto_register_package=True, **kwargs)
        self.tasks = [
            CapellaPackageInitTask(formatter=multigen.formatter.format_autopep8),
            CapellaPackageModuleTask(formatter=multigen.formatter.format_autopep8),
            EcorePackageInitInc(formatter=multigen.formatter.format_autopep8),
        ]
        multigen.jinja.JinjaGenerator.__init__(self)

    @classmethod
    @lru_cache()
    def identify_circular_inheritance(cls, p: ecore.EPackage):
        result = {}
        classes = (c for c in p.eClassifiers if isinstance(c, ecore.EClass))
        for c in classes:
            for st in c.eSuperTypes:
                if st.ePackage is c.ePackage:
                    continue
                other_classes = (c for c in st.ePackage.eClassifiers if isinstance(c, ecore.EClass))
                for oc in other_classes:
                    for oc_st in oc.eSuperTypes:
                        if oc_st.ePackage is c.ePackage and c not in result and oc not in result:
                            result.setdefault(c, []).append(st)
                            print("!!!! Found", c.name, st.name, oc.name, oc_st.name)

        for sub in p.eSubpackages:
            result.update(cls.identify_circular_inheritance(sub))
        return result


    def create_environment(self, **kwargs):
        env = super().create_environment(**kwargs)
        env.globals.update({'package_root': self.package_root})
        return env


class CapellaGenerator(object):
    def __init__(self, package_root, ecore_files):
        self.package_root = package_root
        self.ecore_files = ecore_files
        self.module_generator = CapellaModuleGenerator(self.package_root)
        self.rset = ResourceSet()
        self.rset.uri_mapper['platform:/plugin/org.polarsys.kitalpha.emde/model'] = '../../org.polarsys.kitalpha.emde/model'

    def generate(self, outfolder, version):
        print("== Launch main generation")
        outfolder = Path(outfolder)
        root_package = outfolder / self.package_root
        rset = self.rset
        module_generator = self.module_generator
        generated_module = []
        for mm in self.ecore_files:
            # print("* Opening", mm)
            mm_root = rset.get_resource(mm).contents[0]
            print(" Generating", mm_root.name, "module")
            module_generator.generate(mm_root, outfolder=root_package)
            generated_module.append(module_generator.filter_pyfqn(mm_root))
            for sub in mm_root.eSubpackages:
                print("  submodule", sub.name)
                generated_module.append(module_generator.filter_pyfqn(sub))
        self.post_process(root_package, generated_module, version)

    def post_process(self, root_package, generated_module, version):
        print("== Creating toplevel __init__.py")
        with open(root_package / "__init__.py", "w") as f:
            print(" Header creation")
            f.write(f"__version__ = {version!r}\n\n")
            # f.write("sys.path.append(os.path.dirname(os.path.realpath(__file__)))\n\n")
            print(" Toplevel imports")
            f.write(f"import pyecore.ecore as ecore\n")
            for module in generated_module:
                f.write(f"import {root_package.name}.{module}\n")
                print(f"  Importing {module}")
            for module in generated_module:
                if "." in module:
                    continue
                print(f" Adding increment from {module} cross_init.inc")
                with open(root_package / module / "cross_init.inc", "r") as inc:
                    for line in inc:
                        f.write(line)
        # print("== Apply patch for circular dependencies")
        # patch = Path(os.path.dirname(os.path.realpath(__file__))) / 'patches' / 'circular.patch'
        # process = subprocess.Popen(['git', 'apply', patch])
        # process.communicate()
