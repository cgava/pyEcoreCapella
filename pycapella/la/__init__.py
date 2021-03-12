print('la.__init__.py loading')
from pyecore.resources import global_registry
from .la import getEClassifier, eClassifiers
from .la import name, nsURI, nsPrefix, eClass
from .la import CapabilityRealization, CapabilityRealizationPkg, ContextInterfaceRealization, LogicalArchitecture, LogicalArchitecturePkg, LogicalComponent, LogicalComponentPkg, LogicalFunction, LogicalFunctionPkg, SystemAnalysisRealization
from . import la

__all__ = ['CapabilityRealization', 'CapabilityRealizationPkg', 'ContextInterfaceRealization', 'LogicalArchitecture',
           'LogicalArchitecturePkg', 'LogicalComponent', 'LogicalComponentPkg', 'LogicalFunction', 'LogicalFunctionPkg', 'SystemAnalysisRealization']

eSubpackages = []
eSuperPackage = None
la.eSubpackages = eSubpackages
la.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [la] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('la.__init__.py loaded')
