"""Definition of meta model 'cs'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import AbstractDependenciesPkg, NamedElement, Allocation, Relationship, AbstractExchangeItemPkg, GeneralClass, ModellingArchitecturePkg, InvolverElement, Type, CapellaElement, Involvement, Namespace, GeneralizableElement, Relationship, Structure, CapellaElement, ModellingBlock, Structure, ModellingArchitecture, Classifier, ModellingBlock, Structure, Classifier, NamedElement, Feature, NamedElement, CapellaElement, InvolvedElement, TypedElement, NamedElement
from information.communication import MessageReferencePkg, CommunicationLinkExchanger, CommunicationLinkProtocol
from modellingcore import TraceableElement, FinalizableElement, AbstractNamedElement, FinalizableElement, AbstractNamedElement, PublishableElement, ModelElement, FinalizableElement, InformationsExchanger, AbstractRelationship, AbstractTypedElement, AbstractTrace, AbstractType, TraceableElement
from fa import AbstractFunctionalBlock, AbstractFunctionalArchitecture, ComponentExchangeAllocator
from information import Property, MultiplicityElement, Port, AbstractEventOperation, Property, AbstractInstance
from emde import ExtensibleElement, Element


name = 'cs'
nsURI = 'http://www.polarsys.org/capella/core/cs/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.cs'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class DerivedProvisionedinterfaceallocations(EDerivedCollection):
    pass


class DerivedAllocatedinterfaces(EDerivedCollection):
    pass


@abstract
class InterfaceAllocator(CapellaElement):

    ownedInterfaceAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    provisionedInterfaceAllocations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedProvisionedinterfaceallocations)
    allocatedInterfaces = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedinterfaces)

    def __init__(self, *, ownedInterfaceAllocations=None, provisionedInterfaceAllocations=None, allocatedInterfaces=None, **kwargs):

        super().__init__(**kwargs)

        if ownedInterfaceAllocations:
            self.ownedInterfaceAllocations.extend(ownedInterfaceAllocations)

        if provisionedInterfaceAllocations:
            self.provisionedInterfaceAllocations.extend(provisionedInterfaceAllocations)

        if allocatedInterfaces:
            self.allocatedInterfaces.extend(allocatedInterfaces)


class DerivedAllocatorconfigurationitems(EDerivedCollection):
    pass


@abstract
class AbstractPhysicalArtifact(CapellaElement):

    allocatorConfigurationItems = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedAllocatorconfigurationitems)

    def __init__(self, *, allocatorConfigurationItems=None, **kwargs):

        super().__init__(**kwargs)

        if allocatorConfigurationItems:
            self.allocatorConfigurationItems.extend(allocatorConfigurationItems)


class DerivedInvolvedlinks(EDerivedCollection):
    pass


@abstract
class AbstractPhysicalLinkEnd(CapellaElement):

    involvedLinks = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedlinks)

    def __init__(self, *, involvedLinks=None, **kwargs):

        super().__init__(**kwargs)

        if involvedLinks:
            self.involvedLinks.extend(involvedLinks)


@abstract
class AbstractPathInvolvedElement(InvolvedElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PhysicalLinkEnd(AbstractPhysicalLinkEnd):

    port = EReference(ordered=True, unique=True, containment=False, derived=False)
    part = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, port=None, part=None, **kwargs):

        super().__init__(**kwargs)

        if port is not None:
            self.port = port

        if part is not None:
            self.part = part


class InterfaceImplementation(Relationship):

    _interfaceImplementor = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='interfaceImplementor', transient=True)
    implementedInterface = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def interfaceImplementor(self):
        raise NotImplementedError('Missing implementation for interfaceImplementor')

    def __init__(self, *, interfaceImplementor=None, implementedInterface=None, **kwargs):

        super().__init__(**kwargs)

        if interfaceImplementor is not None:
            self.interfaceImplementor = interfaceImplementor

        if implementedInterface is not None:
            self.implementedInterface = implementedInterface


class InterfaceUse(Relationship):

    _interfaceUser = EReference(ordered=True, unique=True, containment=False,
                                derived=True, name='interfaceUser', transient=True)
    usedInterface = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def interfaceUser(self):
        raise NotImplementedError('Missing implementation for interfaceUser')

    def __init__(self, *, interfaceUser=None, usedInterface=None, **kwargs):

        super().__init__(**kwargs)

        if interfaceUser is not None:
            self.interfaceUser = interfaceUser

        if usedInterface is not None:
            self.usedInterface = usedInterface


@abstract
class ProvidedInterfaceLink(Relationship):

    interface = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, interface=None, **kwargs):

        super().__init__(**kwargs)

        if interface is not None:
            self.interface = interface


@abstract
class RequiredInterfaceLink(Relationship):

    interface = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, interface=None, **kwargs):

        super().__init__(**kwargs)

        if interface is not None:
            self.interface = interface


class DerivedDeployinglinks(EDerivedCollection):
    pass


@abstract
class DeployableElement(NamedElement):

    deployingLinks = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedDeployinglinks)

    def __init__(self, *, deployingLinks=None, **kwargs):

        super().__init__(**kwargs)

        if deployingLinks:
            self.deployingLinks.extend(deployingLinks)


class DerivedDeploymentlinks(EDerivedCollection):
    pass


@abstract
class DeploymentTarget(NamedElement):

    deploymentLinks = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedDeploymentlinks)

    def __init__(self, *, deploymentLinks=None, **kwargs):

        super().__init__(**kwargs)

        if deploymentLinks:
            self.deploymentLinks.extend(deploymentLinks)


@abstract
class AbstractDeploymentLink(Relationship):

    deployedElement = EReference(ordered=True, unique=True, containment=False, derived=False)
    location = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, deployedElement=None, location=None, **kwargs):

        super().__init__(**kwargs)

        if deployedElement is not None:
            self.deployedElement = deployedElement

        if location is not None:
            self.location = location


class PhysicalLinkCategory(NamedElement):

    links = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, links=None, **kwargs):

        super().__init__(**kwargs)

        if links:
            self.links.extend(links)


@abstract
class AbstractPhysicalPathLink(ComponentExchangeAllocator):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedPreviousinvolvements(EDerivedCollection):
    pass


class PhysicalPathInvolvement(Involvement):

    nextInvolvements = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    previousInvolvements = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedPreviousinvolvements)
    _involvedElement = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='involvedElement', transient=True)
    _involvedComponent = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='involvedComponent', transient=True)

    @property
    def involvedElement(self):
        raise NotImplementedError('Missing implementation for involvedElement')

    @property
    def involvedComponent(self):
        raise NotImplementedError('Missing implementation for involvedComponent')

    def __init__(self, *, nextInvolvements=None, previousInvolvements=None, involvedElement=None, involvedComponent=None, **kwargs):

        super().__init__(**kwargs)

        if nextInvolvements:
            self.nextInvolvements.extend(nextInvolvements)

        if previousInvolvements:
            self.previousInvolvements.extend(previousInvolvements)

        if involvedElement is not None:
            self.involvedElement = involvedElement

        if involvedComponent is not None:
            self.involvedComponent = involvedComponent


class PhysicalPathReference(PhysicalPathInvolvement):

    _referencedPhysicalPath = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='referencedPhysicalPath', transient=True)

    @property
    def referencedPhysicalPath(self):
        raise NotImplementedError('Missing implementation for referencedPhysicalPath')

    def __init__(self, *, referencedPhysicalPath=None, **kwargs):

        super().__init__(**kwargs)

        if referencedPhysicalPath is not None:
            self.referencedPhysicalPath = referencedPhysicalPath


@abstract
class ComponentPkg(Structure):

    ownedParts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchanges = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeCategories = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFunctionalLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedFunctionalAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalLinks = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedPhysicalLinkCategories = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedStateMachines = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedParts=None, ownedComponentExchanges=None, ownedComponentExchangeCategories=None, ownedFunctionalLinks=None, ownedFunctionalAllocations=None, ownedComponentExchangeRealizations=None, ownedPhysicalLinks=None, ownedPhysicalLinkCategories=None, ownedStateMachines=None, **kwargs):

        super().__init__(**kwargs)

        if ownedParts:
            self.ownedParts.extend(ownedParts)

        if ownedComponentExchanges:
            self.ownedComponentExchanges.extend(ownedComponentExchanges)

        if ownedComponentExchangeCategories:
            self.ownedComponentExchangeCategories.extend(ownedComponentExchangeCategories)

        if ownedFunctionalLinks:
            self.ownedFunctionalLinks.extend(ownedFunctionalLinks)

        if ownedFunctionalAllocations:
            self.ownedFunctionalAllocations.extend(ownedFunctionalAllocations)

        if ownedComponentExchangeRealizations:
            self.ownedComponentExchangeRealizations.extend(ownedComponentExchangeRealizations)

        if ownedPhysicalLinks:
            self.ownedPhysicalLinks.extend(ownedPhysicalLinks)

        if ownedPhysicalLinkCategories:
            self.ownedPhysicalLinkCategories.extend(ownedPhysicalLinkCategories)

        if ownedStateMachines:
            self.ownedStateMachines.extend(ownedStateMachines)


@abstract
class BlockArchitecturePkg(ModellingArchitecturePkg):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ArchitectureAllocation(Allocation):

    _allocatedArchitecture = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedArchitecture', transient=True)
    _allocatingArchitecture = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingArchitecture', transient=True)

    @property
    def allocatedArchitecture(self):
        raise NotImplementedError('Missing implementation for allocatedArchitecture')

    @property
    def allocatingArchitecture(self):
        raise NotImplementedError('Missing implementation for allocatingArchitecture')

    def __init__(self, *, allocatedArchitecture=None, allocatingArchitecture=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedArchitecture is not None:
            self.allocatedArchitecture = allocatedArchitecture

        if allocatingArchitecture is not None:
            self.allocatingArchitecture = allocatingArchitecture


class ComponentRealization(Allocation):

    _realizedComponent = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedComponent', transient=True)
    _realizingComponent = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingComponent', transient=True)

    @property
    def realizedComponent(self):
        raise NotImplementedError('Missing implementation for realizedComponent')

    @property
    def realizingComponent(self):
        raise NotImplementedError('Missing implementation for realizingComponent')

    def __init__(self, *, realizedComponent=None, realizingComponent=None, **kwargs):

        super().__init__(**kwargs)

        if realizedComponent is not None:
            self.realizedComponent = realizedComponent

        if realizingComponent is not None:
            self.realizingComponent = realizingComponent


@abstract
class InterfaceAllocation(Allocation):

    _allocatedInterface = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedInterface', transient=True)
    _allocatingInterfaceAllocator = EReference(
        ordered=False, unique=True, containment=False, derived=True, name='allocatingInterfaceAllocator', transient=True)

    @property
    def allocatedInterface(self):
        raise NotImplementedError('Missing implementation for allocatedInterface')

    @property
    def allocatingInterfaceAllocator(self):
        raise NotImplementedError('Missing implementation for allocatingInterfaceAllocator')

    def __init__(self, *, allocatedInterface=None, allocatingInterfaceAllocator=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedInterface is not None:
            self.allocatedInterface = allocatedInterface

        if allocatingInterfaceAllocator is not None:
            self.allocatingInterfaceAllocator = allocatingInterfaceAllocator


class PhysicalLinkRealization(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PhysicalPathRealization(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PhysicalPortRealization(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedProvisionedarchitectureallocations(EDerivedCollection):
    pass


class DerivedProvisioningarchitectureallocations(EDerivedCollection):
    pass


class DerivedAllocatedarchitectures(EDerivedCollection):
    pass


class DerivedAllocatingarchitectures(EDerivedCollection):
    pass


@abstract
class BlockArchitecture(AbstractFunctionalArchitecture):

    ownedRequirementPkgs = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedAbstractCapabilityPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    ownedInterfacePkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedDataPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    provisionedArchitectureAllocations = EReference(ordered=True, unique=True, containment=False,
                                                    derived=True, upper=-1, transient=True, derived_class=DerivedProvisionedarchitectureallocations)
    provisioningArchitectureAllocations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedProvisioningarchitectureallocations)
    allocatedArchitectures = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedarchitectures)
    allocatingArchitectures = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingarchitectures)
    _system = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='system', transient=True)

    @property
    def system(self):
        raise NotImplementedError('Missing implementation for system')

    def __init__(self, *, ownedRequirementPkgs=None, ownedAbstractCapabilityPkg=None, ownedInterfacePkg=None, ownedDataPkg=None, provisionedArchitectureAllocations=None, provisioningArchitectureAllocations=None, allocatedArchitectures=None, allocatingArchitectures=None, system=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRequirementPkgs:
            self.ownedRequirementPkgs.extend(ownedRequirementPkgs)

        if ownedAbstractCapabilityPkg is not None:
            self.ownedAbstractCapabilityPkg = ownedAbstractCapabilityPkg

        if ownedInterfacePkg is not None:
            self.ownedInterfacePkg = ownedInterfacePkg

        if ownedDataPkg is not None:
            self.ownedDataPkg = ownedDataPkg

        if provisionedArchitectureAllocations:
            self.provisionedArchitectureAllocations.extend(provisionedArchitectureAllocations)

        if provisioningArchitectureAllocations:
            self.provisioningArchitectureAllocations.extend(provisioningArchitectureAllocations)

        if allocatedArchitectures:
            self.allocatedArchitectures.extend(allocatedArchitectures)

        if allocatingArchitectures:
            self.allocatingArchitectures.extend(allocatingArchitectures)

        if system is not None:
            self.system = system


class ExchangeItemAllocation(Relationship, AbstractEventOperation, FinalizableElement):

    sendProtocol = EAttribute(eType=CommunicationLinkProtocol,
                              unique=True, derived=False, changeable=True)
    receiveProtocol = EAttribute(eType=CommunicationLinkProtocol,
                                 unique=True, derived=False, changeable=True)
    allocatedItem = EReference(ordered=True, unique=True, containment=False, derived=False)
    _allocatingInterface = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingInterface', transient=True)

    @property
    def allocatingInterface(self):
        raise NotImplementedError('Missing implementation for allocatingInterface')

    def __init__(self, *, sendProtocol=None, receiveProtocol=None, allocatedItem=None, allocatingInterface=None, **kwargs):

        super().__init__(**kwargs)

        if sendProtocol is not None:
            self.sendProtocol = sendProtocol

        if receiveProtocol is not None:
            self.receiveProtocol = receiveProtocol

        if allocatedItem is not None:
            self.allocatedItem = allocatedItem

        if allocatingInterface is not None:
            self.allocatingInterface = allocatingInterface


@abstract
class ComponentArchitecture(BlockArchitecture):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedFirstphysicalpathinvolvements(EDerivedCollection):
    pass


class DerivedRealizedphysicalpaths(EDerivedCollection):
    pass


class DerivedRealizingphysicalpaths(EDerivedCollection):
    pass


class PhysicalPath(NamedElement, ComponentExchangeAllocator, AbstractPathInvolvedElement, InvolverElement):

    involvedLinks = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)
    ownedPhysicalPathInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    firstPhysicalPathInvolvements = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedFirstphysicalpathinvolvements)
    ownedPhysicalPathRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedPhysicalPaths = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedphysicalpaths)
    realizingPhysicalPaths = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicalpaths)

    def __init__(self, *, involvedLinks=None, ownedPhysicalPathInvolvements=None, firstPhysicalPathInvolvements=None, ownedPhysicalPathRealizations=None, realizedPhysicalPaths=None, realizingPhysicalPaths=None, **kwargs):

        super().__init__(**kwargs)

        if involvedLinks:
            self.involvedLinks.extend(involvedLinks)

        if ownedPhysicalPathInvolvements:
            self.ownedPhysicalPathInvolvements.extend(ownedPhysicalPathInvolvements)

        if firstPhysicalPathInvolvements:
            self.firstPhysicalPathInvolvements.extend(firstPhysicalPathInvolvements)

        if ownedPhysicalPathRealizations:
            self.ownedPhysicalPathRealizations.extend(ownedPhysicalPathRealizations)

        if realizedPhysicalPaths:
            self.realizedPhysicalPaths.extend(realizedPhysicalPaths)

        if realizingPhysicalPaths:
            self.realizingPhysicalPaths.extend(realizingPhysicalPaths)


class InterfacePkg(MessageReferencePkg, AbstractDependenciesPkg, AbstractExchangeItemPkg):

    ownedInterfaces = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedInterfacePkgs = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedInterfaces=None, ownedInterfacePkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedInterfaces:
            self.ownedInterfaces.extend(ownedInterfaces)

        if ownedInterfacePkgs:
            self.ownedInterfacePkgs.extend(ownedInterfacePkgs)


class DerivedCategories(EDerivedCollection):
    pass


class DerivedRealizedphysicallinks(EDerivedCollection):
    pass


class DerivedRealizingphysicallinks(EDerivedCollection):
    pass


class PhysicalLink(AbstractPhysicalPathLink, AbstractPhysicalArtifact, AbstractPathInvolvedElement):

    linkEnds = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownedComponentExchangeFunctionalExchangeAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalLinkEnds = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    ownedPhysicalLinkRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    categories = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedCategories)
    _sourcePhysicalPort = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='sourcePhysicalPort', transient=True)
    _targetPhysicalPort = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='targetPhysicalPort', transient=True)
    realizedPhysicalLinks = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedphysicallinks)
    realizingPhysicalLinks = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicallinks)

    @property
    def sourcePhysicalPort(self):
        raise NotImplementedError('Missing implementation for sourcePhysicalPort')

    @property
    def targetPhysicalPort(self):
        raise NotImplementedError('Missing implementation for targetPhysicalPort')

    def __init__(self, *, linkEnds=None, ownedComponentExchangeFunctionalExchangeAllocations=None, ownedPhysicalLinkEnds=None, ownedPhysicalLinkRealizations=None, categories=None, sourcePhysicalPort=None, targetPhysicalPort=None, realizedPhysicalLinks=None, realizingPhysicalLinks=None, **kwargs):

        super().__init__(**kwargs)

        if linkEnds:
            self.linkEnds.extend(linkEnds)

        if ownedComponentExchangeFunctionalExchangeAllocations:
            self.ownedComponentExchangeFunctionalExchangeAllocations.extend(
                ownedComponentExchangeFunctionalExchangeAllocations)

        if ownedPhysicalLinkEnds:
            self.ownedPhysicalLinkEnds.extend(ownedPhysicalLinkEnds)

        if ownedPhysicalLinkRealizations:
            self.ownedPhysicalLinkRealizations.extend(ownedPhysicalLinkRealizations)

        if categories:
            self.categories.extend(categories)

        if sourcePhysicalPort is not None:
            self.sourcePhysicalPort = sourcePhysicalPort

        if targetPhysicalPort is not None:
            self.targetPhysicalPort = targetPhysicalPort

        if realizedPhysicalLinks:
            self.realizedPhysicalLinks.extend(realizedPhysicalLinks)

        if realizingPhysicalLinks:
            self.realizingPhysicalLinks.extend(realizingPhysicalLinks)


@abstract
class Block(ModellingBlock, AbstractFunctionalBlock):

    ownedAbstractCapabilityPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    ownedInterfacePkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedDataPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedStateMachines = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedAbstractCapabilityPkg=None, ownedInterfacePkg=None, ownedDataPkg=None, ownedStateMachines=None, **kwargs):

        super().__init__(**kwargs)

        if ownedAbstractCapabilityPkg is not None:
            self.ownedAbstractCapabilityPkg = ownedAbstractCapabilityPkg

        if ownedInterfacePkg is not None:
            self.ownedInterfacePkg = ownedInterfacePkg

        if ownedDataPkg is not None:
            self.ownedDataPkg = ownedDataPkg

        if ownedStateMachines:
            self.ownedStateMachines.extend(ownedStateMachines)


class DerivedImplementorcomponents(EDerivedCollection):
    pass


class DerivedUsercomponents(EDerivedCollection):
    pass


class DerivedInterfaceimplementations(EDerivedCollection):
    pass


class DerivedInterfaceuses(EDerivedCollection):
    pass


class DerivedProvisioninginterfaceallocations(EDerivedCollection):
    pass


class DerivedAllocatinginterfaces(EDerivedCollection):
    pass


class DerivedAllocatingcomponents(EDerivedCollection):
    pass


class DerivedExchangeitems(EDerivedCollection):
    pass


class DerivedRequiringcomponents(EDerivedCollection):
    pass


class DerivedRequiringcomponentports(EDerivedCollection):
    pass


class DerivedProvidingcomponents(EDerivedCollection):
    pass


class DerivedProvidingcomponentports(EDerivedCollection):
    pass


class DerivedRealizinglogicalinterfaces(EDerivedCollection):
    pass


class DerivedRealizedcontextinterfaces(EDerivedCollection):
    pass


class DerivedRealizingphysicalinterfaces(EDerivedCollection):
    pass


class DerivedRealizedlogicalinterfaces(EDerivedCollection):
    pass


class Interface(GeneralClass, InterfaceAllocator):

    mechanism = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    structural = EAttribute(eType=EBoolean, unique=True, derived=False,
                            changeable=True, default_value=True)
    implementorComponents = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedImplementorcomponents)
    userComponents = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedUsercomponents)
    interfaceImplementations = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedInterfaceimplementations)
    interfaceUses = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedInterfaceuses)
    provisioningInterfaceAllocations = EReference(ordered=True, unique=True, containment=False,
                                                  derived=True, upper=-1, transient=True, derived_class=DerivedProvisioninginterfaceallocations)
    allocatingInterfaces = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedAllocatinginterfaces)
    allocatingComponents = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingcomponents)
    exchangeItems = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedExchangeitems)
    ownedExchangeItemAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    requiringComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedRequiringcomponents)
    requiringComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedRequiringcomponentports)
    providingComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedProvidingcomponents)
    providingComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedProvidingcomponentports)
    realizingLogicalInterfaces = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedRealizinglogicalinterfaces)
    realizedContextInterfaces = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcontextinterfaces)
    realizingPhysicalInterfaces = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicalinterfaces)
    realizedLogicalInterfaces = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizedlogicalinterfaces)

    def __init__(self, *, mechanism=None, structural=None, implementorComponents=None, userComponents=None, interfaceImplementations=None, interfaceUses=None, provisioningInterfaceAllocations=None, allocatingInterfaces=None, allocatingComponents=None, exchangeItems=None, ownedExchangeItemAllocations=None, requiringComponents=None, requiringComponentPorts=None, providingComponents=None, providingComponentPorts=None, realizingLogicalInterfaces=None, realizedContextInterfaces=None, realizingPhysicalInterfaces=None, realizedLogicalInterfaces=None, **kwargs):

        super().__init__(**kwargs)

        if mechanism is not None:
            self.mechanism = mechanism

        if structural is not None:
            self.structural = structural

        if implementorComponents:
            self.implementorComponents.extend(implementorComponents)

        if userComponents:
            self.userComponents.extend(userComponents)

        if interfaceImplementations:
            self.interfaceImplementations.extend(interfaceImplementations)

        if interfaceUses:
            self.interfaceUses.extend(interfaceUses)

        if provisioningInterfaceAllocations:
            self.provisioningInterfaceAllocations.extend(provisioningInterfaceAllocations)

        if allocatingInterfaces:
            self.allocatingInterfaces.extend(allocatingInterfaces)

        if allocatingComponents:
            self.allocatingComponents.extend(allocatingComponents)

        if exchangeItems:
            self.exchangeItems.extend(exchangeItems)

        if ownedExchangeItemAllocations:
            self.ownedExchangeItemAllocations.extend(ownedExchangeItemAllocations)

        if requiringComponents:
            self.requiringComponents.extend(requiringComponents)

        if requiringComponentPorts:
            self.requiringComponentPorts.extend(requiringComponentPorts)

        if providingComponents:
            self.providingComponents.extend(providingComponents)

        if providingComponentPorts:
            self.providingComponentPorts.extend(providingComponentPorts)

        if realizingLogicalInterfaces:
            self.realizingLogicalInterfaces.extend(realizingLogicalInterfaces)

        if realizedContextInterfaces:
            self.realizedContextInterfaces.extend(realizedContextInterfaces)

        if realizingPhysicalInterfaces:
            self.realizingPhysicalInterfaces.extend(realizingPhysicalInterfaces)

        if realizedLogicalInterfaces:
            self.realizedLogicalInterfaces.extend(realizedLogicalInterfaces)


class DerivedUsedinterfacelinks(EDerivedCollection):
    pass


class DerivedUsedinterfaces(EDerivedCollection):
    pass


class DerivedImplementedinterfacelinks(EDerivedCollection):
    pass


class DerivedImplementedinterfaces(EDerivedCollection):
    pass


class DerivedRealizedcomponents(EDerivedCollection):
    pass


class DerivedRealizingcomponents(EDerivedCollection):
    pass


class DerivedProvidedinterfaces(EDerivedCollection):
    pass


class DerivedRequiredinterfaces(EDerivedCollection):
    pass


class DerivedContainedcomponentports(EDerivedCollection):
    pass


class DerivedContainedparts(EDerivedCollection):
    pass


class DerivedContainedphysicalports(EDerivedCollection):
    pass


class DerivedRepresentingparts(EDerivedCollection):
    pass


@abstract
class Component(Block, Classifier, InterfaceAllocator, CommunicationLinkExchanger):

    actor = EAttribute(eType=EBoolean, unique=True, derived=False,
                       changeable=True, default_value=False)
    human = EAttribute(eType=EBoolean, unique=True, derived=False,
                       changeable=True, default_value=False)
    ownedInterfaceUses = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    usedInterfaceLinks = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedUsedinterfacelinks)
    usedInterfaces = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedUsedinterfaces)
    ownedInterfaceImplementations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    implementedInterfaceLinks = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedImplementedinterfacelinks)
    implementedInterfaces = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedImplementedinterfaces)
    ownedComponentRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedComponents = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcomponents)
    realizingComponents = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcomponents)
    providedInterfaces = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedProvidedinterfaces)
    requiredInterfaces = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedRequiredinterfaces)
    containedComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedContainedcomponentports)
    containedParts = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedContainedparts)
    containedPhysicalPorts = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedContainedphysicalports)
    ownedPhysicalPath = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    ownedPhysicalLinks = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedPhysicalLinkCategories = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    representingParts = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedRepresentingparts)

    def __init__(self, *, actor=None, human=None, ownedInterfaceUses=None, usedInterfaceLinks=None, usedInterfaces=None, ownedInterfaceImplementations=None, implementedInterfaceLinks=None, implementedInterfaces=None, ownedComponentRealizations=None, realizedComponents=None, realizingComponents=None, providedInterfaces=None, requiredInterfaces=None, containedComponentPorts=None, containedParts=None, containedPhysicalPorts=None, ownedPhysicalPath=None, ownedPhysicalLinks=None, ownedPhysicalLinkCategories=None, representingParts=None, **kwargs):

        super().__init__(**kwargs)

        if actor is not None:
            self.actor = actor

        if human is not None:
            self.human = human

        if ownedInterfaceUses:
            self.ownedInterfaceUses.extend(ownedInterfaceUses)

        if usedInterfaceLinks:
            self.usedInterfaceLinks.extend(usedInterfaceLinks)

        if usedInterfaces:
            self.usedInterfaces.extend(usedInterfaces)

        if ownedInterfaceImplementations:
            self.ownedInterfaceImplementations.extend(ownedInterfaceImplementations)

        if implementedInterfaceLinks:
            self.implementedInterfaceLinks.extend(implementedInterfaceLinks)

        if implementedInterfaces:
            self.implementedInterfaces.extend(implementedInterfaces)

        if ownedComponentRealizations:
            self.ownedComponentRealizations.extend(ownedComponentRealizations)

        if realizedComponents:
            self.realizedComponents.extend(realizedComponents)

        if realizingComponents:
            self.realizingComponents.extend(realizingComponents)

        if providedInterfaces:
            self.providedInterfaces.extend(providedInterfaces)

        if requiredInterfaces:
            self.requiredInterfaces.extend(requiredInterfaces)

        if containedComponentPorts:
            self.containedComponentPorts.extend(containedComponentPorts)

        if containedParts:
            self.containedParts.extend(containedParts)

        if containedPhysicalPorts:
            self.containedPhysicalPorts.extend(containedPhysicalPorts)

        if ownedPhysicalPath:
            self.ownedPhysicalPath.extend(ownedPhysicalPath)

        if ownedPhysicalLinks:
            self.ownedPhysicalLinks.extend(ownedPhysicalLinks)

        if ownedPhysicalLinkCategories:
            self.ownedPhysicalLinkCategories.extend(ownedPhysicalLinkCategories)

        if representingParts:
            self.representingParts.extend(representingParts)


class DerivedAllocatedcomponentports(EDerivedCollection):
    pass


class DerivedRealizedphysicalports(EDerivedCollection):
    pass


class DerivedRealizingphysicalports(EDerivedCollection):
    pass


class PhysicalPort(Port, AbstractPhysicalArtifact, InformationsExchanger, AbstractPhysicalLinkEnd, Property):

    ownedComponentPortAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalPortRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedcomponentports)
    realizedPhysicalPorts = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedphysicalports)
    realizingPhysicalPorts = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicalports)

    def __init__(self, *, ownedComponentPortAllocations=None, ownedPhysicalPortRealizations=None, allocatedComponentPorts=None, realizedPhysicalPorts=None, realizingPhysicalPorts=None, **kwargs):

        super().__init__(**kwargs)

        if ownedComponentPortAllocations:
            self.ownedComponentPortAllocations.extend(ownedComponentPortAllocations)

        if ownedPhysicalPortRealizations:
            self.ownedPhysicalPortRealizations.extend(ownedPhysicalPortRealizations)

        if allocatedComponentPorts:
            self.allocatedComponentPorts.extend(allocatedComponentPorts)

        if realizedPhysicalPorts:
            self.realizedPhysicalPorts.extend(realizedPhysicalPorts)

        if realizingPhysicalPorts:
            self.realizingPhysicalPorts.extend(realizingPhysicalPorts)


class DerivedProvidedinterfaces(EDerivedCollection):
    pass


class DerivedRequiredinterfaces(EDerivedCollection):
    pass


class DerivedDeployedparts(EDerivedCollection):
    pass


class DerivedDeployingparts(EDerivedCollection):
    pass


class Part(AbstractInstance, InformationsExchanger, DeployableElement, DeploymentTarget, AbstractPathInvolvedElement):

    providedInterfaces = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedProvidedinterfaces)
    requiredInterfaces = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedRequiredinterfaces)
    ownedDeploymentLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    deployedParts = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedDeployedparts)
    deployingParts = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedDeployingparts)
    ownedAbstractType = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, providedInterfaces=None, requiredInterfaces=None, ownedDeploymentLinks=None, deployedParts=None, deployingParts=None, ownedAbstractType=None, **kwargs):

        super().__init__(**kwargs)

        if providedInterfaces:
            self.providedInterfaces.extend(providedInterfaces)

        if requiredInterfaces:
            self.requiredInterfaces.extend(requiredInterfaces)

        if ownedDeploymentLinks:
            self.ownedDeploymentLinks.extend(ownedDeploymentLinks)

        if deployedParts:
            self.deployedParts.extend(deployedParts)

        if deployingParts:
            self.deployingParts.extend(deployingParts)

        if ownedAbstractType is not None:
            self.ownedAbstractType = ownedAbstractType
