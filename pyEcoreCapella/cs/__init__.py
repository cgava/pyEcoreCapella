
from .cs import getEClassifier, eClassifiers
from .cs import name, nsURI, nsPrefix, eClass
from .cs import BlockArchitecturePkg, BlockArchitecture, Block, ComponentArchitecture, Component, Part, ArchitectureAllocation, ComponentRealization, InterfacePkg, Interface, InterfaceImplementation, InterfaceUse, ProvidedInterfaceLink, RequiredInterfaceLink, InterfaceAllocation, InterfaceAllocator, ExchangeItemAllocation, DeployableElement, DeploymentTarget, AbstractDeploymentLink, AbstractPathInvolvedElement, AbstractPhysicalArtifact, AbstractPhysicalLinkEnd, AbstractPhysicalPathLink, PhysicalLink, PhysicalLinkCategory, PhysicalLinkEnd, PhysicalLinkRealization, PhysicalPath, PhysicalPathInvolvement, PhysicalPathReference, PhysicalPathRealization, PhysicalPort, PhysicalPortRealization, ComponentPkg

from fa import ExchangeLink, ComponentExchangeCategory, ComponentExchange, ExchangeLink, ComponentFunctionalAllocation, ComponentFunctionalAllocation, ComponentExchangeRealization, ComponentExchangeCategory, ComponentExchange, ComponentExchangeAllocation, AbstractFunction, FunctionPkg, ComponentExchangeFunctionalExchangeAllocation, ComponentExchangeRealization, ComponentPort, ComponentPortAllocation
from information import PortAllocation, Operation, DataPkg, Property, ExchangeItem, PortRealization, Association, ExchangeItem
from information.communication import CommunicationLink, MessageReference
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, GeneralClass, Trace, Generalization, InvolverElement, AbstractPropertyValue, TypedElement, InvolvedElement, EnumerationPropertyType, NamingRule, Type, Involvement, Feature, PropertyValueGroup, PropertyValuePkg
from modellingcore import AbstractConstraint, AbstractType, AbstractTrace, ModelElement, AbstractTypedElement, AbstractInformationFlow, AbstractType, TraceableElement
from capellacommon import GenericTrace, AbstractCapabilityPkg, StateMachine, StateMachine
from requirement import RequirementsPkg, RequirementsTrace, Requirement
from emde import ElementExtension
from information.datavalue import NumericValue, DataValue
from interaction import InstanceRole, SequenceMessage
from epbs import ConfigurationItem

from . import cs

__all__ = ['BlockArchitecturePkg', 'BlockArchitecture', 'Block', 'ComponentArchitecture', 'Component', 'Part', 'ArchitectureAllocation', 'ComponentRealization', 'InterfacePkg', 'Interface', 'InterfaceImplementation', 'InterfaceUse', 'ProvidedInterfaceLink', 'RequiredInterfaceLink', 'InterfaceAllocation', 'InterfaceAllocator', 'ExchangeItemAllocation', 'DeployableElement', 'DeploymentTarget',
           'AbstractDeploymentLink', 'AbstractPathInvolvedElement', 'AbstractPhysicalArtifact', 'AbstractPhysicalLinkEnd', 'AbstractPhysicalPathLink', 'PhysicalLink', 'PhysicalLinkCategory', 'PhysicalLinkEnd', 'PhysicalLinkRealization', 'PhysicalPath', 'PhysicalPathInvolvement', 'PhysicalPathReference', 'PhysicalPathRealization', 'PhysicalPort', 'PhysicalPortRealization', 'ComponentPkg']

eSubpackages = []
eSuperPackage = None
cs.eSubpackages = eSubpackages
cs.eSuperPackage = eSuperPackage

BlockArchitecture.ownedRequirementPkgs.eType = RequirementsPkg
BlockArchitecture.ownedAbstractCapabilityPkg.eType = AbstractCapabilityPkg
BlockArchitecture.ownedInterfacePkg.eType = InterfacePkg
BlockArchitecture.ownedDataPkg.eType = DataPkg
BlockArchitecture.allocatedArchitectures.eType = BlockArchitecture
BlockArchitecture.allocatingArchitectures.eType = BlockArchitecture
BlockArchitecture._system.eType = Component
Block.ownedAbstractCapabilityPkg.eType = AbstractCapabilityPkg
Block.ownedInterfacePkg.eType = InterfacePkg
Block.ownedDataPkg.eType = DataPkg
Block.ownedStateMachines.eType = StateMachine
Component.ownedInterfaceUses.eType = InterfaceUse
Component.ownedInterfaceImplementations.eType = InterfaceImplementation
Component.ownedComponentRealizations.eType = ComponentRealization
Component.realizedComponents.eType = Component
Component.realizingComponents.eType = Component
Component.providedInterfaces.eType = Interface
Component.requiredInterfaces.eType = Interface
Component.containedComponentPorts.eType = ComponentPort
Component.containedParts.eType = Part
Component.containedPhysicalPorts.eType = PhysicalPort
Component.ownedPhysicalPath.eType = PhysicalPath
Component.ownedPhysicalLinks.eType = PhysicalLink
Component.ownedPhysicalLinkCategories.eType = PhysicalLinkCategory
Component.representingParts.eType = Part
Part.providedInterfaces.eType = Interface
Part.requiredInterfaces.eType = Interface
Part.ownedDeploymentLinks.eType = AbstractDeploymentLink
Part.deployedParts.eType = Part
Part.deployingParts.eType = Part
Part.ownedAbstractType.eType = AbstractType
ComponentRealization._realizedComponent.eType = Component
ComponentRealization._realizingComponent.eType = Component
InterfacePkg.ownedInterfaces.eType = Interface
InterfacePkg.ownedInterfacePkgs.eType = InterfacePkg
Interface.interfaceImplementations.eType = InterfaceImplementation
Interface.interfaceUses.eType = InterfaceUse
Interface.allocatingInterfaces.eType = Interface
Interface.allocatingComponents.eType = Component
Interface.exchangeItems.eType = ExchangeItem
Interface.ownedExchangeItemAllocations.eType = ExchangeItemAllocation
Interface.requiringComponents.eType = Component
Interface.requiringComponentPorts.eType = ComponentPort
Interface.providingComponents.eType = Component
Interface.providingComponentPorts.eType = ComponentPort
Interface.realizingLogicalInterfaces.eType = Interface
Interface.realizedContextInterfaces.eType = Interface
Interface.realizingPhysicalInterfaces.eType = Interface
Interface.realizedLogicalInterfaces.eType = Interface
InterfaceImplementation.implementedInterface.eType = Interface
InterfaceUse.usedInterface.eType = Interface
ProvidedInterfaceLink.interface.eType = Interface
RequiredInterfaceLink.interface.eType = Interface
InterfaceAllocator.ownedInterfaceAllocations.eType = InterfaceAllocation
InterfaceAllocator.allocatedInterfaces.eType = Interface
ExchangeItemAllocation.allocatedItem.eType = ExchangeItem
ExchangeItemAllocation._allocatingInterface.eType = Interface
DeployableElement.deployingLinks.eType = AbstractDeploymentLink
DeploymentTarget.deploymentLinks.eType = AbstractDeploymentLink
AbstractDeploymentLink.deployedElement.eType = DeployableElement
AbstractDeploymentLink.location.eType = DeploymentTarget
AbstractPhysicalLinkEnd.involvedLinks.eType = PhysicalLink
PhysicalLink.linkEnds.eType = AbstractPhysicalLinkEnd
PhysicalLink.ownedComponentExchangeFunctionalExchangeAllocations.eType = ComponentExchangeFunctionalExchangeAllocation
PhysicalLink.ownedPhysicalLinkEnds.eType = PhysicalLinkEnd
PhysicalLink.ownedPhysicalLinkRealizations.eType = PhysicalLinkRealization
PhysicalLink.categories.eType = PhysicalLinkCategory
PhysicalLink._sourcePhysicalPort.eType = PhysicalPort
PhysicalLink._targetPhysicalPort.eType = PhysicalPort
PhysicalLink.realizedPhysicalLinks.eType = PhysicalLink
PhysicalLink.realizingPhysicalLinks.eType = PhysicalLink
PhysicalLinkCategory.links.eType = PhysicalLink
PhysicalLinkEnd.port.eType = PhysicalPort
PhysicalLinkEnd.part.eType = Part
PhysicalPath.involvedLinks.eType = AbstractPhysicalPathLink
PhysicalPath.ownedPhysicalPathInvolvements.eType = PhysicalPathInvolvement
PhysicalPath.firstPhysicalPathInvolvements.eType = PhysicalPathInvolvement
PhysicalPath.ownedPhysicalPathRealizations.eType = PhysicalPathRealization
PhysicalPath.realizedPhysicalPaths.eType = PhysicalPath
PhysicalPath.realizingPhysicalPaths.eType = PhysicalPath
PhysicalPathInvolvement.nextInvolvements.eType = PhysicalPathInvolvement
PhysicalPathInvolvement.previousInvolvements.eType = PhysicalPathInvolvement
PhysicalPathInvolvement._involvedElement.eType = AbstractPathInvolvedElement
PhysicalPathInvolvement._involvedComponent.eType = Component
PhysicalPathReference._referencedPhysicalPath.eType = PhysicalPath
PhysicalPort.ownedComponentPortAllocations.eType = ComponentPortAllocation
PhysicalPort.ownedPhysicalPortRealizations.eType = PhysicalPortRealization
PhysicalPort.realizedPhysicalPorts.eType = PhysicalPort
PhysicalPort.realizingPhysicalPorts.eType = PhysicalPort
ComponentPkg.ownedParts.eType = Part
ComponentPkg.ownedComponentExchanges.eType = ComponentExchange
ComponentPkg.ownedComponentExchangeCategories.eType = ComponentExchangeCategory
ComponentPkg.ownedFunctionalLinks.eType = ExchangeLink
ComponentPkg.ownedFunctionalAllocations.eType = ComponentFunctionalAllocation
ComponentPkg.ownedComponentExchangeRealizations.eType = ComponentExchangeRealization
ComponentPkg.ownedPhysicalLinks.eType = PhysicalLink
ComponentPkg.ownedPhysicalLinkCategories.eType = PhysicalLinkCategory
ComponentPkg.ownedStateMachines.eType = StateMachine
BlockArchitecture.provisionedArchitectureAllocations.eType = ArchitectureAllocation
BlockArchitecture.provisioningArchitectureAllocations.eType = ArchitectureAllocation
Component.usedInterfaceLinks.eType = InterfaceUse
Component.usedInterfaces.eType = Interface
Component.implementedInterfaceLinks.eType = InterfaceImplementation
Component.implementedInterfaces.eType = Interface
ArchitectureAllocation._allocatedArchitecture.eType = BlockArchitecture
ArchitectureAllocation._allocatedArchitecture.eOpposite = BlockArchitecture.provisioningArchitectureAllocations
ArchitectureAllocation._allocatingArchitecture.eType = BlockArchitecture
ArchitectureAllocation._allocatingArchitecture.eOpposite = BlockArchitecture.provisionedArchitectureAllocations
Interface.implementorComponents.eType = Component
Interface.implementorComponents.eOpposite = Component.implementedInterfaces
Interface.userComponents.eType = Component
Interface.userComponents.eOpposite = Component.usedInterfaces
Interface.provisioningInterfaceAllocations.eType = InterfaceAllocation
InterfaceImplementation._interfaceImplementor.eType = Component
InterfaceImplementation._interfaceImplementor.eOpposite = Component.implementedInterfaceLinks
InterfaceUse._interfaceUser.eType = Component
InterfaceUse._interfaceUser.eOpposite = Component.usedInterfaceLinks
InterfaceAllocation._allocatedInterface.eType = Interface
InterfaceAllocation._allocatedInterface.eOpposite = Interface.provisioningInterfaceAllocations
InterfaceAllocation._allocatingInterfaceAllocator.eType = InterfaceAllocator
InterfaceAllocator.provisionedInterfaceAllocations.eType = InterfaceAllocation
InterfaceAllocator.provisionedInterfaceAllocations.eOpposite = InterfaceAllocation.allocatingInterfaceAllocator
AbstractPhysicalArtifact.allocatorConfigurationItems.eType = ConfigurationItem
PhysicalPort.allocatedComponentPorts.eType = ComponentPort

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
