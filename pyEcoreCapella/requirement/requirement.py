"""Definition of meta model 'requirement'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import Namespace, NamedElement, Namespace, Structure, CapellaElement, Relationship, Trace
from modellingcore import TraceableElement, AbstractNamedElement, PublishableElement, AbstractRelationship, ModelElement, AbstractTrace, TraceableElement
from emde import ExtensibleElement, Element


name = 'requirement'
nsURI = 'http://www.polarsys.org/capella/core/requirement/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.requirement'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class DerivedRelatedcapellaelements(EDerivedCollection):
    pass


@abstract
class Requirement(Namespace):

    isObsolete = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    requirementId = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    additionalInformation = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    verificationMethod = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    verificationPhase = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    implementationVersion = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    feature = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    relatedCapellaElements = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRelatedcapellaelements)

    def __init__(self, *, isObsolete=None, requirementId=None, additionalInformation=None, verificationMethod=None, verificationPhase=None, implementationVersion=None, feature=None, relatedCapellaElements=None, **kwargs):

        super().__init__(**kwargs)

        if isObsolete is not None:
            self.isObsolete = isObsolete

        if requirementId is not None:
            self.requirementId = requirementId

        if additionalInformation is not None:
            self.additionalInformation = additionalInformation

        if verificationMethod is not None:
            self.verificationMethod = verificationMethod

        if verificationPhase is not None:
            self.verificationPhase = verificationPhase

        if implementationVersion is not None:
            self.implementationVersion = implementationVersion

        if feature is not None:
            self.feature = feature

        if relatedCapellaElements:
            self.relatedCapellaElements.extend(relatedCapellaElements)


class RequirementsPkg(Structure):

    additionalInformation = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    level = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    ownedRequirements = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    ownedRequirementPkgs = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)

    def __init__(self, *, additionalInformation=None, level=None, ownedRequirements=None, ownedRequirementPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if additionalInformation is not None:
            self.additionalInformation = additionalInformation

        if level is not None:
            self.level = level

        if ownedRequirements:
            self.ownedRequirements.extend(ownedRequirements)

        if ownedRequirementPkgs:
            self.ownedRequirementPkgs.extend(ownedRequirementPkgs)


class SystemFunctionalInterfaceRequirement(Requirement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SystemFunctionalRequirement(Requirement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SystemNonFunctionalInterfaceRequirement(Requirement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SystemNonFunctionalRequirement(Requirement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SystemUserRequirement(Requirement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RequirementsTrace(Trace):

    _source = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='source', transient=True)
    _target = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='target', transient=True)

    @property
    def source(self):
        raise NotImplementedError('Missing implementation for source')

    @property
    def target(self):
        raise NotImplementedError('Missing implementation for target')

    def __init__(self, *, source=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target
