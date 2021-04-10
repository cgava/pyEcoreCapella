"""Definition of meta model 'oa'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pycapella2.activity import ActivityPartition
from pycapella2.capellacommon import AbstractCapabilityPkg
from pycapella2.capellacore import Allocation, InvolvedElement, Involvement, NamedElement, NamedRelationship, Namespace, Relationship, Structure
from pycapella2.cs import BlockArchitecture, Component, ComponentPkg
from pycapella2.fa import AbstractFunction, ComponentExchange, FunctionalChain, FunctionPkg
from pycapella2.information import AbstractInstance
from pycapella2.interaction import AbstractCapability
from pycapella2.modellingcore import InformationsExchanger


name = 'oa'
nsURI = 'http://www.polarsys.org/capella/core/oa/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.oa'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class OperationalScenario(NamedElement):

    context = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    objective = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, context=None, objective=None, **kwargs):

        super().__init__(**kwargs)

        if context is not None:
            self.context = context

        if objective is not None:
            self.objective = objective


class RoleAssemblyUsage(NamedElement):

    child = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, child=None, **kwargs):

        super().__init__(**kwargs)

        if child is not None:
            self.child = child


class Concept(NamedElement):

    compliances = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    compositeLinks = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)

    def __init__(self, *, compliances=None, compositeLinks=None, **kwargs):

        super().__init__(**kwargs)

        if compliances:
            self.compliances.extend(compliances)

        if compositeLinks:
            self.compositeLinks.extend(compositeLinks)


class ConceptCompliance(Relationship):

    complyWithConcept = EReference(ordered=True, unique=True, containment=False, derived=False)
    compliantCapability = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, complyWithConcept=None, compliantCapability=None, **kwargs):

        super().__init__(**kwargs)

        if complyWithConcept is not None:
            self.complyWithConcept = complyWithConcept

        if compliantCapability is not None:
            self.compliantCapability = compliantCapability


class ItemInConcept(NamedElement):

    concept = EReference(ordered=True, unique=True, containment=False, derived=False)
    item = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, concept=None, item=None, **kwargs):

        super().__init__(**kwargs)

        if concept is not None:
            self.concept = concept

        if item is not None:
            self.item = item


class CommunityOfInterest(NamedElement):

    communityOfInterestCompositions = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, communityOfInterestCompositions=None, **kwargs):

        super().__init__(**kwargs)

        if communityOfInterestCompositions:
            self.communityOfInterestCompositions.extend(communityOfInterestCompositions)


class CommunityOfInterestComposition(NamedElement):

    communityOfInterest = EReference(ordered=True, unique=True, containment=False, derived=False)
    interestedOrganisationUnit = EReference(
        ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, communityOfInterest=None, interestedOrganisationUnit=None, **kwargs):

        super().__init__(**kwargs)

        if communityOfInterest is not None:
            self.communityOfInterest = communityOfInterest

        if interestedOrganisationUnit is not None:
            self.interestedOrganisationUnit = interestedOrganisationUnit


class OrganisationalUnit(NamedElement):

    organisationalUnitCompositions = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    communityOfInterestMemberships = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, organisationalUnitCompositions=None, communityOfInterestMemberships=None, **kwargs):

        super().__init__(**kwargs)

        if organisationalUnitCompositions:
            self.organisationalUnitCompositions.extend(organisationalUnitCompositions)

        if communityOfInterestMemberships:
            self.communityOfInterestMemberships.extend(communityOfInterestMemberships)


class OrganisationalUnitComposition(NamedElement):

    organisationalUnit = EReference(ordered=True, unique=True, containment=False, derived=False)
    participatingEntity = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, organisationalUnit=None, participatingEntity=None, **kwargs):

        super().__init__(**kwargs)

        if organisationalUnit is not None:
            self.organisationalUnit = organisationalUnit

        if participatingEntity is not None:
            self.participatingEntity = participatingEntity


class EntityOperationalCapabilityInvolvement(Involvement):

    _entity = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='entity', transient=True)
    _capability = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='capability', transient=True)

    @property
    def entity(self):
        raise NotImplementedError('Missing implementation for entity')

    @property
    def capability(self):
        raise NotImplementedError('Missing implementation for capability')

    def __init__(self, *, entity=None, capability=None, **kwargs):

        super().__init__(**kwargs)

        if entity is not None:
            self.entity = entity

        if capability is not None:
            self.capability = capability


class RolePkg(Structure):

    ownedRolePkgs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedRoles = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedRolePkgs=None, ownedRoles=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRolePkgs:
            self.ownedRolePkgs.extend(ownedRolePkgs)

        if ownedRoles:
            self.ownedRoles.extend(ownedRoles)


class ConceptPkg(Structure):

    ownedConceptPkgs = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedConcepts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedConceptPkgs=None, ownedConcepts=None, **kwargs):

        super().__init__(**kwargs)

        if ownedConceptPkgs:
            self.ownedConceptPkgs.extend(ownedConceptPkgs)

        if ownedConcepts:
            self.ownedConcepts.extend(ownedConcepts)


class OperationalActivityPkg(FunctionPkg):

    ownedOperationalActivities = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedOperationalActivityPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedOperationalActivities=None, ownedOperationalActivityPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedOperationalActivities:
            self.ownedOperationalActivities.extend(ownedOperationalActivities)

        if ownedOperationalActivityPkgs:
            self.ownedOperationalActivityPkgs.extend(ownedOperationalActivityPkgs)


class DerivedInvolvingoperationalcapabilities(EDerivedCollection):
    pass


class OperationalProcess(FunctionalChain):

    involvingOperationalCapabilities = EReference(ordered=True, unique=True, containment=False,
                                                  derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingoperationalcapabilities)

    def __init__(self, *, involvingOperationalCapabilities=None, **kwargs):

        super().__init__(**kwargs)

        if involvingOperationalCapabilities:
            self.involvingOperationalCapabilities.extend(involvingOperationalCapabilities)


class OperationalCapabilityPkg(AbstractCapabilityPkg):

    ownedOperationalCapabilities = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedOperationalCapabilityPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedCapabilityConfigurations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConceptCompliances = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedOperationalCapabilities=None, ownedOperationalCapabilityPkgs=None, ownedCapabilityConfigurations=None, ownedConceptCompliances=None, **kwargs):

        super().__init__(**kwargs)

        if ownedOperationalCapabilities:
            self.ownedOperationalCapabilities.extend(ownedOperationalCapabilities)

        if ownedOperationalCapabilityPkgs:
            self.ownedOperationalCapabilityPkgs.extend(ownedOperationalCapabilityPkgs)

        if ownedCapabilityConfigurations:
            self.ownedCapabilityConfigurations.extend(ownedCapabilityConfigurations)

        if ownedConceptCompliances:
            self.ownedConceptCompliances.extend(ownedConceptCompliances)


class ActivityAllocation(Allocation):

    _role = EReference(ordered=True, unique=True, containment=False,
                       derived=True, name='role', transient=True)
    _activity = EReference(ordered=True, unique=True, containment=False,
                           derived=True, name='activity', transient=True)

    @property
    def role(self):
        raise NotImplementedError('Missing implementation for role')

    @property
    def activity(self):
        raise NotImplementedError('Missing implementation for activity')

    def __init__(self, *, role=None, activity=None, **kwargs):

        super().__init__(**kwargs)

        if role is not None:
            self.role = role

        if activity is not None:
            self.activity = activity


class RoleAllocation(Allocation):

    _role = EReference(ordered=True, unique=True, containment=False,
                       derived=True, name='role', transient=True)
    _entity = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='entity', transient=True)

    @property
    def role(self):
        raise NotImplementedError('Missing implementation for role')

    @property
    def entity(self):
        raise NotImplementedError('Missing implementation for entity')

    def __init__(self, *, role=None, entity=None, **kwargs):

        super().__init__(**kwargs)

        if role is not None:
            self.role = role

        if entity is not None:
            self.entity = entity


class EntityPkg(ComponentPkg):

    ownedEntities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedEntityPkgs = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedLocations = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    ownedCommunicationMeans = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedEntities=None, ownedEntityPkgs=None, ownedLocations=None, ownedCommunicationMeans=None, **kwargs):

        super().__init__(**kwargs)

        if ownedEntities:
            self.ownedEntities.extend(ownedEntities)

        if ownedEntityPkgs:
            self.ownedEntityPkgs.extend(ownedEntityPkgs)

        if ownedLocations:
            self.ownedLocations.extend(ownedLocations)

        if ownedCommunicationMeans:
            self.ownedCommunicationMeans.extend(ownedCommunicationMeans)


class Swimlane(NamedElement, ActivityPartition):

    _representedEntity = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='representedEntity', transient=True)

    @property
    def representedEntity(self):
        raise NotImplementedError('Missing implementation for representedEntity')

    def __init__(self, *, representedEntity=None, **kwargs):

        super().__init__(**kwargs)

        if representedEntity is not None:
            self.representedEntity = representedEntity


class DerivedAllocatingsystemanalyses(EDerivedCollection):
    pass


class OperationalAnalysis(BlockArchitecture):

    ownedRolePkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedEntityPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedConceptPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    _containedOperationalCapabilityPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedOperationalCapabilityPkg', transient=True)
    _containedOperationalActivityPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedOperationalActivityPkg', transient=True)
    allocatingSystemAnalyses = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingsystemanalyses)

    @property
    def containedOperationalCapabilityPkg(self):
        raise NotImplementedError('Missing implementation for containedOperationalCapabilityPkg')

    @property
    def containedOperationalActivityPkg(self):
        raise NotImplementedError('Missing implementation for containedOperationalActivityPkg')

    def __init__(self, *, ownedRolePkg=None, ownedEntityPkg=None, ownedConceptPkg=None, containedOperationalCapabilityPkg=None, containedOperationalActivityPkg=None, allocatingSystemAnalyses=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRolePkg is not None:
            self.ownedRolePkg = ownedRolePkg

        if ownedEntityPkg is not None:
            self.ownedEntityPkg = ownedEntityPkg

        if ownedConceptPkg is not None:
            self.ownedConceptPkg = ownedConceptPkg

        if containedOperationalCapabilityPkg is not None:
            self.containedOperationalCapabilityPkg = containedOperationalCapabilityPkg

        if containedOperationalActivityPkg is not None:
            self.containedOperationalActivityPkg = containedOperationalActivityPkg

        if allocatingSystemAnalyses:
            self.allocatingSystemAnalyses.extend(allocatingSystemAnalyses)


class DerivedRealizingcapabilities(EDerivedCollection):
    pass


class DerivedInvolvedentities(EDerivedCollection):
    pass


class OperationalCapability(AbstractCapability, Namespace):

    compliances = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    configurations = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    ownedEntityOperationalCapabilityInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizingCapabilities = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcapabilities)
    involvedEntities = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedentities)

    def __init__(self, *, compliances=None, configurations=None, ownedEntityOperationalCapabilityInvolvements=None, realizingCapabilities=None, involvedEntities=None, **kwargs):

        super().__init__(**kwargs)

        if compliances:
            self.compliances.extend(compliances)

        if configurations:
            self.configurations.extend(configurations)

        if ownedEntityOperationalCapabilityInvolvements:
            self.ownedEntityOperationalCapabilityInvolvements.extend(
                ownedEntityOperationalCapabilityInvolvements)

        if realizingCapabilities:
            self.realizingCapabilities.extend(realizingCapabilities)

        if involvedEntities:
            self.involvedEntities.extend(involvedEntities)


class DerivedRoleallocations(EDerivedCollection):
    pass


class DerivedActivityallocations(EDerivedCollection):
    pass


class DerivedAllocatingentities(EDerivedCollection):
    pass


class DerivedAllocatedoperationalactivities(EDerivedCollection):
    pass


class Role(AbstractInstance):

    ownedRoleAssemblyUsages = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedActivityAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    roleAllocations = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedRoleallocations)
    activityAllocations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedActivityallocations)
    allocatingEntities = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingentities)
    allocatedOperationalActivities = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedoperationalactivities)

    def __init__(self, *, ownedRoleAssemblyUsages=None, ownedActivityAllocations=None, roleAllocations=None, activityAllocations=None, allocatingEntities=None, allocatedOperationalActivities=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRoleAssemblyUsages:
            self.ownedRoleAssemblyUsages.extend(ownedRoleAssemblyUsages)

        if ownedActivityAllocations:
            self.ownedActivityAllocations.extend(ownedActivityAllocations)

        if roleAllocations:
            self.roleAllocations.extend(roleAllocations)

        if activityAllocations:
            self.activityAllocations.extend(activityAllocations)

        if allocatingEntities:
            self.allocatingEntities.extend(allocatingEntities)

        if allocatedOperationalActivities:
            self.allocatedOperationalActivities.extend(allocatedOperationalActivities)


@abstract
class AbstractConceptItem(Component):

    composingLinks = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)

    def __init__(self, *, composingLinks=None, **kwargs):

        super().__init__(**kwargs)

        if composingLinks:
            self.composingLinks.extend(composingLinks)


class CommunicationMean(NamedRelationship, ComponentExchange):

    _sourceEntity = EReference(ordered=True, unique=True, containment=False,
                               derived=True, name='sourceEntity', transient=True)
    _targetEntity = EReference(ordered=True, unique=True, containment=False,
                               derived=True, name='targetEntity', transient=True)

    @property
    def sourceEntity(self):
        raise NotImplementedError('Missing implementation for sourceEntity')

    @property
    def targetEntity(self):
        raise NotImplementedError('Missing implementation for targetEntity')

    def __init__(self, *, sourceEntity=None, targetEntity=None, **kwargs):

        super().__init__(**kwargs)

        if sourceEntity is not None:
            self.sourceEntity = sourceEntity

        if targetEntity is not None:
            self.targetEntity = targetEntity


class Location(AbstractConceptItem):

    locationDescription = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    locatedEntities = EReference(ordered=True, unique=True,
                                 containment=False, derived=False, upper=-1)

    def __init__(self, *, locationDescription=None, locatedEntities=None, **kwargs):

        super().__init__(**kwargs)

        if locationDescription is not None:
            self.locationDescription = locationDescription

        if locatedEntities:
            self.locatedEntities.extend(locatedEntities)


class CapabilityConfiguration(AbstractConceptItem):

    configuredCapability = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, configuredCapability=None, **kwargs):

        super().__init__(**kwargs)

        if configuredCapability is not None:
            self.configuredCapability = configuredCapability


class DerivedRoleallocations(EDerivedCollection):
    pass


class DerivedSubentities(EDerivedCollection):
    pass


class DerivedAllocatedoperationalactivities(EDerivedCollection):
    pass


class DerivedAllocatedroles(EDerivedCollection):
    pass


class DerivedInvolvingoperationalcapabilities(EDerivedCollection):
    pass


class DerivedRealizingsystemcomponents(EDerivedCollection):
    pass


class Entity(AbstractConceptItem, InformationsExchanger, InvolvedElement):

    roleAllocations = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedRoleallocations)
    organisationalUnitMemberships = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    actualLocation = EReference(ordered=True, unique=True, containment=False, derived=False)
    subEntities = EReference(ordered=True, unique=True, containment=False,
                             derived=True, upper=-1, transient=True, derived_class=DerivedSubentities)
    ownedEntities = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedCommunicationMeans = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedRoleAllocations = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    allocatedOperationalActivities = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedoperationalactivities)
    allocatedRoles = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedroles)
    involvingOperationalCapabilities = EReference(ordered=True, unique=True, containment=False,
                                                  derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingoperationalcapabilities)
    realizingSystemComponents = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizingsystemcomponents)

    def __init__(self, *, roleAllocations=None, organisationalUnitMemberships=None, actualLocation=None, subEntities=None, ownedEntities=None, ownedCommunicationMeans=None, ownedRoleAllocations=None, allocatedOperationalActivities=None, allocatedRoles=None, involvingOperationalCapabilities=None, realizingSystemComponents=None, **kwargs):

        super().__init__(**kwargs)

        if roleAllocations:
            self.roleAllocations.extend(roleAllocations)

        if organisationalUnitMemberships:
            self.organisationalUnitMemberships.extend(organisationalUnitMemberships)

        if actualLocation is not None:
            self.actualLocation = actualLocation

        if subEntities:
            self.subEntities.extend(subEntities)

        if ownedEntities:
            self.ownedEntities.extend(ownedEntities)

        if ownedCommunicationMeans:
            self.ownedCommunicationMeans.extend(ownedCommunicationMeans)

        if ownedRoleAllocations:
            self.ownedRoleAllocations.extend(ownedRoleAllocations)

        if allocatedOperationalActivities:
            self.allocatedOperationalActivities.extend(allocatedOperationalActivities)

        if allocatedRoles:
            self.allocatedRoles.extend(allocatedRoles)

        if involvingOperationalCapabilities:
            self.involvingOperationalCapabilities.extend(involvingOperationalCapabilities)

        if realizingSystemComponents:
            self.realizingSystemComponents.extend(realizingSystemComponents)


class DerivedActivityallocations(EDerivedCollection):
    pass


class DerivedOwnedswimlanes(EDerivedCollection):
    pass


class DerivedOwnedprocess(EDerivedCollection):
    pass


class DerivedAllocatorentities(EDerivedCollection):
    pass


class DerivedRealizingsystemfunctions(EDerivedCollection):
    pass


class DerivedAllocatingroles(EDerivedCollection):
    pass


class DerivedContainedoperationalactivities(EDerivedCollection):
    pass


class DerivedChildrenoperationalactivities(EDerivedCollection):
    pass


class OperationalActivity(AbstractFunction):

    ownedOperationalActivityPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    activityAllocations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedActivityallocations)
    ownedSwimlanes = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedOwnedswimlanes)
    ownedProcess = EReference(ordered=True, unique=True, containment=False,
                              derived=True, upper=-1, transient=True, derived_class=DerivedOwnedprocess)
    allocatorEntities = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedAllocatorentities)
    realizingSystemFunctions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedRealizingsystemfunctions)
    allocatingRoles = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingroles)
    containedOperationalActivities = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedContainedoperationalactivities)
    childrenOperationalActivities = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedChildrenoperationalactivities)

    def __init__(self, *, ownedOperationalActivityPkgs=None, activityAllocations=None, ownedSwimlanes=None, ownedProcess=None, allocatorEntities=None, realizingSystemFunctions=None, allocatingRoles=None, containedOperationalActivities=None, childrenOperationalActivities=None, **kwargs):

        super().__init__(**kwargs)

        if ownedOperationalActivityPkgs:
            self.ownedOperationalActivityPkgs.extend(ownedOperationalActivityPkgs)

        if activityAllocations:
            self.activityAllocations.extend(activityAllocations)

        if ownedSwimlanes:
            self.ownedSwimlanes.extend(ownedSwimlanes)

        if ownedProcess:
            self.ownedProcess.extend(ownedProcess)

        if allocatorEntities:
            self.allocatorEntities.extend(allocatorEntities)

        if realizingSystemFunctions:
            self.realizingSystemFunctions.extend(realizingSystemFunctions)

        if allocatingRoles:
            self.allocatingRoles.extend(allocatingRoles)

        if containedOperationalActivities:
            self.containedOperationalActivities.extend(containedOperationalActivities)

        if childrenOperationalActivities:
            self.childrenOperationalActivities.extend(childrenOperationalActivities)
