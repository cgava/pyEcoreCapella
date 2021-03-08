
from .emde import getEClassifier, eClassifiers
from .emde import name, nsURI, nsPrefix, eClass
from .emde import Element, ExtensibleElement, ElementExtension


from . import emde

__all__ = ['Element', 'ExtensibleElement', 'ElementExtension']

eSubpackages = []
eSuperPackage = None
emde.eSubpackages = eSubpackages
emde.eSuperPackage = eSuperPackage

ExtensibleElement.ownedExtensions.eType = ElementExtension

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
