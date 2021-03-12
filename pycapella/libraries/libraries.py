print('libraries.libraries loading')
"""Definition of meta model 'libraries'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from emde import ElementExtension, ExtensibleElement


name = 'libraries'
nsURI = 'http://www.polarsys.org/capella/common/libraries/1.4.0'
nsPrefix = 'libraries'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
AccessPolicy = EEnum('AccessPolicy', literals=['readOnly', 'readAndWrite'])


@abstract
class LibraryAbstractElement(ExtensibleElement):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)

    def __init__(self, *, id=None, **kwargs):

        super().__init__(**kwargs)

        if id is not None:
            self.id = id


class LibraryReference(LibraryAbstractElement):

    accessPolicy = EAttribute(eType=AccessPolicy, unique=True, derived=False, changeable=True)
    library = EReference(ordered=True, unique=True, containment=False, derived=False)
    version = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, library=None, accessPolicy=None, version=None, **kwargs):

        super().__init__(**kwargs)

        if accessPolicy is not None:
            self.accessPolicy = accessPolicy

        if library is not None:
            self.library = library

        if version is not None:
            self.version = version


class ModelVersion(LibraryAbstractElement):

    majorVersionNumber = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    minorVersionNumber = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    lastModifiedFileStamp = EAttribute(eType=ELong, unique=True, derived=False, changeable=True)

    def __init__(self, *, majorVersionNumber=None, minorVersionNumber=None, lastModifiedFileStamp=None, **kwargs):

        super().__init__(**kwargs)

        if majorVersionNumber is not None:
            self.majorVersionNumber = majorVersionNumber

        if minorVersionNumber is not None:
            self.minorVersionNumber = minorVersionNumber

        if lastModifiedFileStamp is not None:
            self.lastModifiedFileStamp = lastModifiedFileStamp


class ModelInformation(LibraryAbstractElement, ElementExtension):

    ownedReferences = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    version = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, ownedReferences=None, version=None, **kwargs):

        super().__init__(**kwargs)

        if ownedReferences:
            self.ownedReferences.extend(ownedReferences)

        if version is not None:
            self.version = version

print('libraries.libraries loaded')
