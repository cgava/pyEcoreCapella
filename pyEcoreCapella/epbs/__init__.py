print('epbs.__init__.py loading')
from pyecore.resources import global_registry
from .epbs import getEClassifier, eClassifiers
from .epbs import name, nsURI, nsPrefix, eClass
from .epbs import ConfigurationItem, ConfigurationItemKind, ConfigurationItemPkg, EPBSArchitecture, EPBSArchitecturePkg, PhysicalArchitectureRealization, PhysicalArtifactRealization
from . import epbs

__all__ = ['ConfigurationItem', 'ConfigurationItemKind', 'ConfigurationItemPkg', 'EPBSArchitecture',
           'EPBSArchitecturePkg', 'PhysicalArchitectureRealization', 'PhysicalArtifactRealization']

eSubpackages = []
eSuperPackage = None
epbs.eSubpackages = eSubpackages
epbs.eSuperPackage = eSuperPackage

otherClassifiers = [ConfigurationItemKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [epbs] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('epbs.__init__.py loaded')
