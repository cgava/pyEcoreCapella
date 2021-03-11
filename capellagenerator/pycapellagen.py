import os
import subprocess
from pathlib import Path
import itertools
import multigen
import pyecore.ecore as ecore
from pyecore.resources import ResourceSet
from pyecoregen.ecore import EcoreGenerator, EcoreTask, EcorePackageInitTask, EcorePackageModuleTask
import pyecoregen.adapter as adapter


old_fix_name_clash = adapter.fix_name_clash

def fix_name_clash(value):
    value = old_fix_name_clash(value)
    if value in ('super', 'self'):
        print(f"!! Fixing {value} in {value}_")
        value += '_'
    return value

adapter.fix_name_clash = fix_name_clash


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
        # Sorting EPackage by name
        return {k: v for k, v in sorted(imported_dict.items(), key=lambda x: x[0].name)}


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
            imported_classifiers_package=self.imported_classifiers_package(element)
        )


class CapellaModuleGenerator(EcoreGenerator):
    templates_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            'templates'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, auto_register_package=True, **kwargs)
        self.tasks = [
            CapellaPackageInitTask(formatter=multigen.formatter.format_autopep8),
            CapellaPackageModuleTask(formatter=multigen.formatter.format_autopep8),
            EcorePackageInitInc(formatter=multigen.formatter.format_autopep8),
        ]
        multigen.jinja.JinjaGenerator.__init__(self)


class CapellaGenerator(object):
    def __init__(self, ecore_files):
        self.ecore_files = ecore_files
        self.module_generator = CapellaModuleGenerator()
        self.rset = ResourceSet()
        self.rset.uri_mapper['platform:/plugin/org.polarsys.kitalpha.emde/model'] = '../../org.polarsys.kitalpha.emde/model'

    def generate(self, outfolder):
        print("== Launch main generation")
        rset = self.rset
        module_generator = self.module_generator
        generated_module = []
        for mm in self.ecore_files:
            # print("* Opening", mm)
            mm_root = rset.get_resource(mm).contents[0]
            print(" Generating", mm_root.name, "module")
            module_generator.generate(mm_root, outfolder=outfolder)
            generated_module.append(module_generator.filter_pyfqn(mm_root))
            for sub in mm_root.eSubpackages:
                print("  submodule", sub.name)
                generated_module.append(module_generator.filter_pyfqn(sub))
        self.post_process(outfolder, generated_module)

    def post_process(self, outfolder, generated_module):
        print("== Creating toplevel __init__.py")
        outfolder = Path(outfolder)
        with open(outfolder / "__init__.py", "w") as f:
            print(" Header creation")
            f.write("import sys\nimport os\n")
            f.write("sys.path.append(os.path.dirname(os.path.realpath(__file__)))\n\n")
            print(" Toplevel imports")
            for module in generated_module:
                f.write(f"import {module}\n")
                print(f"  Importing {module}")
            for module in generated_module:
                if "." in module:
                    continue
                print(f" Adding increment from {module} cross_init.inc")
                with open(outfolder / module / "cross_init.inc", "r") as inc:
                    for line in inc:
                        f.write(line)
        print("== Apply patch for circular dependencies")
        patch = Path(os.path.dirname(os.path.realpath(__file__))) / 'patches' / 'circular.patch'
        process = subprocess.Popen(['git', 'apply', patch])
        process.communicate()
