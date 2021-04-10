#print('sharedmodel.__init__.py loading')
from pyecore.resources import global_registry
from .sharedmodel import getEClassifier, eClassifiers
from .sharedmodel import name, nsURI, nsPrefix, eClass
from .sharedmodel import GenericPkg, SharedPkg
from . import sharedmodel

__all__ = ['GenericPkg', 'SharedPkg']

eSubpackages = []
eSuperPackage = None
sharedmodel.eSubpackages = eSubpackages
sharedmodel.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [sharedmodel] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('sharedmodel.__init__.py loaded')
