#print('libraries.__init__.py loading')
from pyecore.resources import global_registry
from .libraries import getEClassifier, eClassifiers
from .libraries import name, nsURI, nsPrefix, eClass
from .libraries import AccessPolicy, LibraryAbstractElement, LibraryReference, ModelInformation, ModelVersion
from . import libraries

__all__ = ['AccessPolicy', 'LibraryAbstractElement',
           'LibraryReference', 'ModelInformation', 'ModelVersion']

eSubpackages = []
eSuperPackage = None
libraries.eSubpackages = eSubpackages
libraries.eSuperPackage = eSuperPackage

otherClassifiers = [AccessPolicy]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [libraries] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('libraries.__init__.py loaded')
