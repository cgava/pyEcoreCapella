
from .libraries import getEClassifier, eClassifiers
from .libraries import name, nsURI, nsPrefix, eClass
from .libraries import ModelInformation, LibraryReference, ModelVersion, AccessPolicy, LibraryAbstractElement

from emde import ElementExtension

from . import libraries

__all__ = ['ModelInformation', 'LibraryReference',
           'ModelVersion', 'AccessPolicy', 'LibraryAbstractElement']

eSubpackages = []
eSuperPackage = None
libraries.eSubpackages = eSubpackages
libraries.eSuperPackage = eSuperPackage

ModelInformation.ownedReferences.eType = LibraryReference
ModelInformation.version.eType = ModelVersion
LibraryReference.library.eType = ModelInformation
LibraryReference.version.eType = ModelVersion

otherClassifiers = [AccessPolicy]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
