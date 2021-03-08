print('emde.__init__.py loading')
from pyecore.resources import global_registry
from .emde import getEClassifier, eClassifiers
from .emde import name, nsURI, nsPrefix, eClass
from .emde import Element, ElementExtension, ExtensibleElement
from . import emde

__all__ = ['Element', 'ElementExtension', 'ExtensibleElement']

eSubpackages = []
eSuperPackage = None
emde.eSubpackages = eSubpackages
emde.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [emde] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('emde.__init__.py loaded')
