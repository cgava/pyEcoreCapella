print('pa.__init__.py loading')
from pyecore.resources import global_registry
from .pa import getEClassifier, eClassifiers
from .pa import name, nsURI, nsPrefix, eClass
from .pa import LogicalArchitectureRealization, LogicalInterfaceRealization, PhysicalArchitecture, PhysicalArchitecturePkg, PhysicalComponent, PhysicalComponentKind, PhysicalComponentNature, PhysicalComponentPkg, PhysicalFunction, PhysicalFunctionPkg, PhysicalNode
from . import pa
from . import deployment


__all__ = ['LogicalArchitectureRealization', 'LogicalInterfaceRealization', 'PhysicalArchitecture', 'PhysicalArchitecturePkg', 'PhysicalComponent',
           'PhysicalComponentKind', 'PhysicalComponentNature', 'PhysicalComponentPkg', 'PhysicalFunction', 'PhysicalFunctionPkg', 'PhysicalNode']

eSubpackages = [deployment]
eSuperPackage = None
pa.eSubpackages = eSubpackages
pa.eSuperPackage = eSuperPackage

otherClassifiers = [PhysicalComponentKind, PhysicalComponentNature]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [pa] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('pa.__init__.py loaded')
