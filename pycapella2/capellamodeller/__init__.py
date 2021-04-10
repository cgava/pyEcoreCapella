#print('capellamodeller.__init__.py loading')
from pyecore.resources import global_registry
from .capellamodeller import getEClassifier, eClassifiers
from .capellamodeller import name, nsURI, nsPrefix, eClass
from .capellamodeller import Folder, Library, ModelRoot, Project, SystemEngineering, SystemEngineeringPkg
from . import capellamodeller

__all__ = ['Folder', 'Library', 'ModelRoot', 'Project', 'SystemEngineering', 'SystemEngineeringPkg']

eSubpackages = []
eSuperPackage = None
capellamodeller.eSubpackages = eSubpackages
capellamodeller.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [capellamodeller] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('capellamodeller.__init__.py loaded')
