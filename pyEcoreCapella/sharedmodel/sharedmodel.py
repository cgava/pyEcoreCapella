print('sharedmodel.sharedmodel loading')
"""Definition of meta model 'sharedmodel'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import CapellaElement, CapellaElement, NamedElement, Namespace, ReuseableStructure, Structure, Structure
from capellamodeller import ModelRoot
from emde import Element, ExtensibleElement
from modellingcore import AbstractNamedElement, ModelElement, PublishableElement, TraceableElement


name = 'sharedmodel'
nsURI = 'http://www.polarsys.org/capella/core/sharedmodel/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.sharedmodel'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class GenericPkg(Structure):

    subGenericPkgs = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    capellaElements = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, subGenericPkgs=None, capellaElements=None, **kwargs):

        super().__init__(**kwargs)

        if subGenericPkgs:
            self.subGenericPkgs.extend(subGenericPkgs)

        if capellaElements:
            self.capellaElements.extend(capellaElements)


class SharedPkg(ReuseableStructure, ModelRoot):

    ownedDataPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedGenericPkg = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedDataPkg=None, ownedGenericPkg=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDataPkg is not None:
            self.ownedDataPkg = ownedDataPkg

        if ownedGenericPkg is not None:
            self.ownedGenericPkg = ownedGenericPkg

print('sharedmodel.sharedmodel loaded')
