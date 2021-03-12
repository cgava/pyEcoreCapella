print('pyEcoreCapelle.__init__ loading')
print('pyEcoreCapelle.__init__ 01 importing activity')
from activity import *
print('pyEcoreCapelle.__init__ 02 importing behavior')
from behavior import *
print('pyEcoreCapelle.__init__ 03 importing modellingcore')
from modellingcore import *
print('pyEcoreCapelle.__init__ 04 importing emde')
from emde import *
print('pyEcoreCapelle.__init__ 05 importing capellacommon')
from capellacommon import *
print('pyEcoreCapelle.__init__ 06 importing capellacore')
from capellacore import *
print('pyEcoreCapelle.__init__ 07 importing capellamodeller')
from capellamodeller import *
print('pyEcoreCapelle.__init__ 08 importing cs')
from cs import *
print('pyEcoreCapelle.__init__ 09 importing ctx')
from ctx import *
print('pyEcoreCapelle.__init__ 10 importing epbs')
from epbs import *
print('pyEcoreCapelle.__init__ 11 importing fa')
from fa import *
print('pyEcoreCapelle.__init__ 12.1 importing information.communication')
from information.communication import *
print('pyEcoreCapelle.__init__ 12.2 importing information.datavalue')
from information.datavalue import *
print('pyEcoreCapelle.__init__ 12.3 importing information.datatype')
from information.datatype import *
print('pyEcoreCapelle.__init__ 12.4 importing information')
from information import *
print('pyEcoreCapelle.__init__ 13 importing interaction')
from interaction import *
print('pyEcoreCapelle.__init__ 14 importing la')
from la import *
print('pyEcoreCapelle.__init__ 15 importing libraries')
from libraries import *
print('pyEcoreCapelle.__init__ 16 importing oa')
from oa import *
print('pyEcoreCapelle.__init__ 17.1 importing pa.deployment')
from pa.deployment import *
print('pyEcoreCapelle.__init__ 17.2 importing pa')
from pa import *
print('pyEcoreCapelle.__init__ 18 importing requirement')
from requirement import *
print('pyEcoreCapelle.__init__ 19 importing sharedmodel')
from sharedmodel import *

print('pyEcoreCapelle.__init__ loaded')
print('activity.cross_init starting')


AbstractActivity.ownedNodes.eType = ActivityNode
AbstractActivity.ownedEdges.eType = ActivityEdge
AbstractActivity.ownedGroups.eType = ActivityGroup
AbstractActivity.ownedStructuredNodes.eType = StructuredActivityNode
ExceptionHandler.handlerBody.eType = ExecutableNode
ExceptionHandler.exceptionInput.eType = ObjectNode
ExceptionHandler.exceptionTypes.eType = AbstractType
ActivityGroup.ownedNodes.eType = ActivityNode
ActivityGroup.ownedEdges.eType = ActivityEdge
ActivityEdge._inActivityPartition.eType = ActivityPartition
ActivityEdge._inInterruptibleRegion.eType = InterruptibleActivityRegion
ActivityEdge._inStructuredNode.eType = StructuredActivityNode
ActivityEdge.rate.eType = ValueSpecification
ActivityEdge.probability.eType = ValueSpecification
ActivityEdge.target.eType = ActivityNode
ActivityEdge.source.eType = ActivityNode
ActivityEdge.guard.eType = ValueSpecification
ActivityEdge.weight.eType = ValueSpecification
ObjectFlow.transformation.eType = AbstractBehavior
ObjectFlow.selection.eType = AbstractBehavior
ActivityPartition.representedElement.eType = AbstractType
ActivityPartition._superPartition.eType = ActivityPartition
ActivityPartition.subPartitions.eType = ActivityPartition
ActivityExchange.realizingActivityFlows.eType = ActivityEdge
ActivityNode._inActivityPartition.eType = ActivityPartition
ActivityNode._inInterruptibleRegion.eType = InterruptibleActivityRegion
ActivityNode._inStructuredNode.eType = InterruptibleActivityRegion
ActivityNode.outgoing.eType = ActivityEdge
ActivityNode.incoming.eType = ActivityEdge
AbstractAction.localPrecondition.eType = AbstractConstraint
AbstractAction.localPostcondition.eType = AbstractConstraint
AbstractAction.context.eType = AbstractType
AbstractAction.inputs.eType = InputPin
AbstractAction.outputs.eType = OutputPin
AcceptEventAction.result.eType = OutputPin
InvocationAction.arguments.eType = InputPin
SendSignalAction.target.eType = InputPin
SendSignalAction.signal.eType = AbstractSignal
CallAction.results.eType = OutputPin
CallBehaviorAction.behavior.eType = AbstractBehavior
ObjectNode.upperBound.eType = ValueSpecification
ObjectNode.inState.eType = IState
ObjectNode.selection.eType = AbstractBehavior
InputPin.inputEvaluationAction.eType = AbstractAction
ValuePin.value.eType = ValueSpecification
ExceptionHandler.protectedNode.eType = ExecutableNode
ActivityGroup.superGroup.eType = ActivityGroup
ActivityGroup.subGroups.eType = ActivityGroup
ActivityGroup.subGroups.eOpposite = ActivityGroup.superGroup
InterruptibleActivityRegion.interruptingEdges.eType = ActivityEdge
ActivityEdge.interrupts.eType = InterruptibleActivityRegion
ActivityEdge.interrupts.eOpposite = InterruptibleActivityRegion.interruptingEdges
ExecutableNode.ownedHandlers.eType = ExceptionHandler
ExecutableNode.ownedHandlers.eOpposite = ExceptionHandler.protectedNode

print('activity.cross_init done')

print('behavior.cross_init starting')


AbstractBehavior.ownedParameterSet.eType = AbstractParameterSet
AbstractBehavior.ownedParameter.eType = AbstractParameter
AbstractTimeEvent.when.eType = TimeExpression
AbstractSignalEvent.signal.eType = AbstractSignal
TimeExpression.observations.eType = AbstractNamedElement
TimeExpression.expression.eType = ValueSpecification

print('behavior.cross_init done')

print('capellacommon.cross_init starting')


GenericTrace.keyValuePairs.eType = KeyValue
GenericTrace._source.eType = TraceableElement
GenericTrace._target.eType = TraceableElement
CapabilityRealizationInvolvement._involvedCapabilityRealizationInvolvedElement.eType = CapabilityRealizationInvolvedElement
CapabilityRealizationInvolvedElement.capabilityRealizationInvolvements.eType = CapabilityRealizationInvolvement
CapabilityRealizationInvolvedElement.involvingCapabilityRealizations.eType = CapabilityRealization
StateMachine.ownedRegions.eType = Region
StateMachine.ownedConnectionPoints.eType = Pseudostate
Region.ownedStates.eType = AbstractState
Region.ownedTransitions.eType = StateTransition
Region.involvedStates.eType = AbstractState
State.ownedRegions.eType = Region
State.ownedConnectionPoints.eType = Pseudostate
State.availableAbstractFunctions.eType = AbstractFunction
State.availableFunctionalChains.eType = FunctionalChain
State.availableAbstractCapabilities.eType = AbstractCapability
State.entry.eType = AbstractEvent
State.doActivity.eType = AbstractEvent
State.exit.eType = AbstractEvent
State.stateInvariant.eType = AbstractConstraint
AbstractState.ownedAbstractStateRealizations.eType = AbstractStateRealization
AbstractState.realizedAbstractStates.eType = AbstractState
AbstractState.realizingAbstractStates.eType = AbstractState
AbstractState.outgoing.eType = StateTransition
AbstractState.incoming.eType = StateTransition
AbstractState.involverRegions.eType = Region
StateTransition.guard.eType = Constraint
StateTransition.source.eType = AbstractState
StateTransition.target.eType = AbstractState
StateTransition.effect.eType = AbstractEvent
StateTransition.triggers.eType = AbstractEvent
StateTransition.ownedStateTransitionRealizations.eType = StateTransitionRealization
StateTransition.realizedStateTransitions.eType = StateTransition
StateTransition.realizingStateTransitions.eType = StateTransition
AbstractStateRealization._realizedAbstractState.eType = AbstractState
AbstractStateRealization._realizingAbstractState.eType = AbstractState
StateTransitionRealization._realizedStateTransition.eType = StateTransition
StateTransitionRealization._realizingStateTransition.eType = StateTransition
StateEventRealization._realizedEvent.eType = StateEvent
StateEventRealization._realizingEvent.eType = StateEvent
StateEvent.expression.eType = Constraint
StateEvent.ownedStateEventRealizations.eType = StateEventRealization

print('capellacommon.cross_init done')

print('capellacore.cross_init starting')


CapellaElement.ownedPropertyValues.eType = AbstractPropertyValue
CapellaElement.ownedEnumerationPropertyTypes.eType = EnumerationPropertyType
CapellaElement.appliedPropertyValues.eType = AbstractPropertyValue
CapellaElement.ownedPropertyValueGroups.eType = PropertyValueGroup
CapellaElement.appliedPropertyValueGroups.eType = PropertyValueGroup
CapellaElement.status.eType = EnumerationPropertyLiteral
CapellaElement.features.eType = EnumerationPropertyLiteral
CapellaElement.appliedRequirements.eType = Requirement
Namespace.ownedTraces.eType = Trace
Namespace.containedGenericTraces.eType = GenericTrace
Namespace.containedRequirementsTraces.eType = RequirementsTrace
Namespace.namingRules.eType = NamingRule
NamedRelationship.namingRules.eType = NamingRule
Structure.ownedPropertyValuePkgs.eType = PropertyValuePkg
AbstractModellingStructure.ownedArchitectures.eType = ModellingArchitecture
AbstractModellingStructure.ownedArchitecturePkgs.eType = ModellingArchitecturePkg
Type.typedElements.eType = TypedElement
TypedElement._type.eType = Type
ReuseLink.reused.eType = ReuseableStructure
ReuseLink.reuser.eType = ReuserStructure
ReuseableStructure.reuseLinks.eType = ReuseLink
ReuserStructure.reuseLinks.eType = ReuseLink
ReuserStructure.ownedReuseLinks.eType = ReuseLink
GeneralizableElement.ownedGeneralizations.eType = Generalization
GeneralizableElement.superGeneralizations.eType = Generalization
GeneralizableElement.subGeneralizations.eType = Generalization
Classifier.ownedFeatures.eType = Feature
Classifier.containedProperties.eType = Property
GeneralClass.containedOperations.eType = Operation
GeneralClass.nestedGeneralClasses.eType = GeneralClass
Generalization.super.eType = GeneralizableElement
Generalization.sub.eType = GeneralizableElement
AbstractExchangeItemPkg.ownedExchangeItems.eType = ExchangeItem
Involvement._involver.eType = InvolverElement
Involvement.involved.eType = InvolvedElement
InvolverElement.involvedInvolvements.eType = Involvement
InvolvedElement.involvingInvolvements.eType = Involvement
AbstractPropertyValue.involvedElements.eType = CapellaElement
AbstractPropertyValue.valuedElements.eType = CapellaElement
EnumerationPropertyValue.type.eType = EnumerationPropertyType
EnumerationPropertyValue.value.eType = EnumerationPropertyLiteral
EnumerationPropertyType.ownedLiterals.eType = EnumerationPropertyLiteral
PropertyValueGroup.valuedElements.eType = CapellaElement
GeneralizableElement.super.eType = GeneralizableElement
GeneralizableElement.sub.eType = GeneralizableElement
GeneralizableElement.sub.eOpposite = GeneralizableElement.super

print('capellacore.cross_init done')

print('capellamodeller.cross_init starting')


Project.keyValuePairs.eType = KeyValue
Project.ownedFolders.eType = Folder
Project.ownedModelRoots.eType = ModelRoot
Folder.ownedFolders.eType = Folder
Folder.ownedModelRoots.eType = ModelRoot
SystemEngineering.containedOperationalAnalysis.eType = OperationalAnalysis
SystemEngineering.containedSystemAnalysis.eType = SystemAnalysis
SystemEngineering.containedLogicalArchitectures.eType = LogicalArchitecture
SystemEngineering.containedPhysicalArchitectures.eType = PhysicalArchitecture
SystemEngineering.containedEPBSArchitectures.eType = EPBSArchitecture
SystemEngineering.containedSharedPkgs.eType = SharedPkg
SystemEngineeringPkg.ownedSystemEngineerings.eType = SystemEngineering

print('capellamodeller.cross_init done')

print('cs.cross_init starting')


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
#InterfaceAllocator.provisionedInterfaceAllocations.eOpposite = InterfaceAllocation.allocatingInterfaceAllocator
AbstractPhysicalArtifact.allocatorConfigurationItems.eType = ConfigurationItem
PhysicalPort.allocatedComponentPorts.eType = ComponentPort

print('cs.cross_init done')

print('ctx.cross_init starting')


SystemAnalysis.ownedSystemComponentPkg.eType = SystemComponentPkg
SystemAnalysis.ownedMissionPkg.eType = MissionPkg
SystemAnalysis._containedCapabilityPkg.eType = CapabilityPkg
SystemAnalysis._containedSystemFunctionPkg.eType = SystemFunctionPkg
SystemAnalysis.ownedOperationalAnalysisRealizations.eType = OperationalAnalysisRealization
SystemAnalysis.allocatedOperationalAnalysisRealizations.eType = OperationalAnalysisRealization
SystemFunction.ownedSystemFunctionPkgs.eType = SystemFunctionPkg
SystemFunction.allocatingSystemComponents.eType = SystemComponent
SystemFunction.containedSystemFunctions.eType = SystemFunction
SystemFunction.childrenSystemFunctions.eType = SystemFunction
SystemFunctionPkg.ownedSystemFunctions.eType = SystemFunction
SystemFunctionPkg.ownedSystemFunctionPkgs.eType = SystemFunctionPkg
SystemCommunicationHook.communication.eType = SystemCommunication
SystemCommunicationHook.type.eType = Component
SystemCommunication.ends.eType = SystemCommunicationHook
CapabilityInvolvement._systemComponent.eType = SystemComponent
CapabilityInvolvement._capability.eType = Capability
MissionInvolvement._systemComponent.eType = SystemComponent
MissionInvolvement._mission.eType = Mission
Mission.ownedMissionInvolvements.eType = MissionInvolvement
Mission.involvedSystemComponents.eType = SystemComponent
Mission.ownedCapabilityExploitations.eType = CapabilityExploitation
MissionPkg.ownedMissionPkgs.eType = MissionPkg
MissionPkg.ownedMissions.eType = Mission
Capability.ownedCapabilityInvolvements.eType = CapabilityInvolvement
Capability.involvedSystemComponents.eType = SystemComponent
Capability.purposes.eType = CapabilityExploitation
CapabilityExploitation._mission.eType = Mission
CapabilityExploitation.capability.eType = Capability
CapabilityPkg.ownedCapabilities.eType = Capability
CapabilityPkg.ownedCapabilityPkgs.eType = CapabilityPkg
SystemComponentPkg.ownedSystemComponents.eType = SystemComponent
SystemComponentPkg.ownedSystemComponentPkgs.eType = SystemComponentPkg
SystemComponent.ownedSystemComponents.eType = SystemComponent
SystemComponent.ownedSystemComponentPkgs.eType = SystemComponentPkg
SystemComponent.dataType.eType = Classifier
SystemComponent.involvingCapabilities.eType = Capability
SystemComponent.capabilityInvolvements.eType = CapabilityInvolvement
SystemComponent.involvingMissions.eType = Mission
SystemComponent.missionInvolvements.eType = MissionInvolvement
SystemComponent.realizedEntities.eType = Entity
SystemComponent.realizingLogicalComponents.eType = LogicalComponent
SystemComponent.allocatedSystemFunctions.eType = SystemFunction
SystemAnalysis.allocatedOperationalAnalyses.eType = OperationalAnalysis
SystemAnalysis.allocatingLogicalArchitectures.eType = LogicalArchitecture
SystemFunction.realizedOperationalActivities.eType = OperationalActivity
SystemFunction.realizingLogicalFunctions.eType = LogicalFunction
Mission.exploitedCapabilities.eType = Capability
Capability.purposeMissions.eType = Mission
Capability.purposeMissions.eOpposite = Mission.exploitedCapabilities
Capability.realizedOperationalCapabilities.eType = OperationalCapability
Capability.realizingCapabilityRealizations.eType = CapabilityRealization

print('ctx.cross_init done')

print('emde.cross_init starting')


ExtensibleElement.ownedExtensions.eType = ElementExtension

print('emde.cross_init done')

print('epbs.cross_init starting')


EPBSArchitecturePkg.ownedEPBSArchitectures.eType = EPBSArchitecture
EPBSArchitecture.ownedConfigurationItemPkg.eType = ConfigurationItemPkg
EPBSArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
EPBSArchitecture.ownedPhysicalArchitectureRealizations.eType = PhysicalArchitectureRealization
EPBSArchitecture.allocatedPhysicalArchitectureRealizations.eType = PhysicalArchitectureRealization
ConfigurationItemPkg.ownedConfigurationItems.eType = ConfigurationItem
ConfigurationItemPkg.ownedConfigurationItemPkgs.eType = ConfigurationItemPkg
ConfigurationItem.ownedConfigurationItems.eType = ConfigurationItem
ConfigurationItem.ownedConfigurationItemPkgs.eType = ConfigurationItemPkg
ConfigurationItem.ownedPhysicalArtifactRealizations.eType = PhysicalArtifactRealization
PhysicalArtifactRealization._realizedPhysicalArtifact.eType = AbstractPhysicalArtifact
PhysicalArtifactRealization._realizingConfigurationItem.eType = ConfigurationItem
EPBSArchitecture.allocatedPhysicalArchitectures.eType = PhysicalArchitecture
ConfigurationItem.allocatedPhysicalArtifacts.eType = AbstractPhysicalArtifact

print('epbs.cross_init done')

print('fa.cross_init starting')


AbstractFunctionalArchitecture.ownedFunctionPkg.eType = FunctionPkg
AbstractFunctionalArchitecture.ownedComponentExchanges.eType = ComponentExchange
AbstractFunctionalArchitecture.ownedComponentExchangeCategories.eType = ComponentExchangeCategory
AbstractFunctionalArchitecture.ownedFunctionalLinks.eType = ExchangeLink
AbstractFunctionalArchitecture.ownedFunctionalAllocations.eType = ComponentFunctionalAllocation
AbstractFunctionalArchitecture.ownedComponentExchangeRealizations.eType = ComponentExchangeRealization
AbstractFunctionalBlock.ownedFunctionalAllocation.eType = ComponentFunctionalAllocation
AbstractFunctionalBlock.ownedComponentExchanges.eType = ComponentExchange
AbstractFunctionalBlock.ownedComponentExchangeCategories.eType = ComponentExchangeCategory
AbstractFunctionalBlock.inExchangeLinks.eType = ExchangeLink
AbstractFunctionalBlock.outExchangeLinks.eType = ExchangeLink
FunctionPkg.ownedFunctionalLinks.eType = ExchangeLink
FunctionPkg.ownedExchanges.eType = FunctionalExchangeSpecification
FunctionPkg.ownedExchangeSpecificationRealizations.eType = ExchangeSpecificationRealization
FunctionPkg.ownedCategories.eType = ExchangeCategory
FunctionPkg.ownedFunctionSpecifications.eType = FunctionSpecification
FunctionSpecification.inExchangeLinks.eType = ExchangeLink
FunctionSpecification.outExchangeLinks.eType = ExchangeLink
FunctionSpecification.ownedFunctionPorts.eType = FunctionPort
FunctionSpecification.subFunctionSpecifications.eType = FunctionSpecification
ExchangeCategory.exchanges.eType = FunctionalExchange
ExchangeLink.exchanges.eType = ExchangeSpecification
ExchangeLink.ownedExchangeContainments.eType = ExchangeContainment
ExchangeLink.sources.eType = FunctionSpecification
ExchangeLink.destinations.eType = FunctionSpecification
ExchangeSpecification._containingLink.eType = ExchangeLink
FunctionalExchangeSpecification.functionalExchanges.eType = FunctionalExchange
FunctionalChain.ownedFunctionalChainInvolvements.eType = FunctionalChainInvolvement
FunctionalChain.ownedFunctionalChainRealizations.eType = FunctionalChainRealization
FunctionalChain.involvedFunctionalChainInvolvements.eType = FunctionalChainInvolvement
FunctionalChain.involvedElements.eType = InvolvedElement
FunctionalChain.enactedFunctions.eType = AbstractFunction
FunctionalChain.enactedFunctionalBlocks.eType = AbstractFunctionalBlock
FunctionalChain.availableInStates.eType = State
FunctionalChain.firstFunctionalChainInvolvements.eType = FunctionalChainInvolvement
FunctionalChain.involvingCapabilities.eType = Capability
FunctionalChain.involvingCapabilityRealizations.eType = CapabilityRealization
FunctionalChain.realizedFunctionalChains.eType = FunctionalChain
FunctionalChain.realizingFunctionalChains.eType = FunctionalChain
FunctionalChain.preCondition.eType = Constraint
FunctionalChain.postCondition.eType = Constraint
FunctionalChain.ownedSequenceNodes.eType = ControlNode
FunctionalChain.ownedSequenceLinks.eType = SequenceLink
AbstractFunctionalChainContainer.ownedFunctionalChains.eType = FunctionalChain
FunctionalChainInvolvement.nextFunctionalChainInvolvements.eType = FunctionalChainInvolvement
FunctionalChainInvolvement.previousFunctionalChainInvolvements.eType = FunctionalChainInvolvement
FunctionalChainInvolvement._involvedElement.eType = InvolvedElement
FunctionalChainReference._referencedFunctionalChain.eType = FunctionalChain
FunctionInputPort.incomingExchangeItems.eType = ExchangeItem
FunctionInputPort.incomingFunctionalExchanges.eType = FunctionalExchange
FunctionOutputPort.outgoingExchangeItems.eType = ExchangeItem
FunctionOutputPort.outgoingFunctionalExchanges.eType = FunctionalExchange
FunctionalExchange.exchangeSpecifications.eType = FunctionalExchangeSpecification
FunctionalExchange.exchangedItems.eType = ExchangeItem
FunctionalExchange.categories.eType = ExchangeCategory
FunctionalExchange.ownedFunctionalExchangeRealizations.eType = FunctionalExchangeRealization
FunctionalExchange._sourceFunctionOutputPort.eType = FunctionOutputPort
FunctionalExchange._targetFunctionInputPort.eType = FunctionInputPort
AbstractFunction.ownedFunctions.eType = AbstractFunction
AbstractFunction.ownedFunctionRealizations.eType = FunctionRealization
AbstractFunction.ownedFunctionalExchanges.eType = FunctionalExchange
AbstractFunction.subFunctions.eType = AbstractFunction
AbstractFunction.availableInStates.eType = State
AbstractFunction.involvingCapabilities.eType = Capability
AbstractFunction.involvingCapabilityRealizations.eType = CapabilityRealization
AbstractFunction._linkedStateMachine.eType = StateMachine
AbstractFunction._linkedFunctionSpecification.eType = FunctionSpecification
FunctionPort.representedComponentPort.eType = ComponentPort
FunctionPort.realizedFunctionPorts.eType = FunctionPort
FunctionPort.realizingFunctionPorts.eType = FunctionPort
ComponentExchange.ownedComponentExchangeFunctionalExchangeAllocations.eType = ComponentExchangeFunctionalExchangeAllocation
ComponentExchange.ownedComponentExchangeRealizations.eType = ComponentExchangeRealization
ComponentExchange.ownedComponentExchangeEnds.eType = ComponentExchangeEnd
ComponentExchange._sourcePort.eType = Port
ComponentExchange._sourcePart.eType = Part
ComponentExchange._targetPort.eType = Port
ComponentExchange._targetPart.eType = Part
ComponentExchange.categories.eType = ComponentExchangeCategory
ComponentExchange.allocatorPhysicalLinks.eType = PhysicalLink
ComponentExchangeAllocation._componentExchangeAllocated.eType = ComponentExchange
ComponentExchangeAllocation._componentExchangeAllocator.eType = ComponentExchangeAllocator
ComponentExchangeAllocator.ownedComponentExchangeAllocations.eType = ComponentExchangeAllocation
ComponentExchangeAllocator.allocatedComponentExchanges.eType = ComponentExchange
ComponentExchangeCategory.exchanges.eType = ComponentExchange
ComponentExchangeEnd.port.eType = Port
ComponentExchangeEnd.part.eType = Part
ComponentPort.componentExchanges.eType = ComponentExchange
ComponentPortAllocation.ownedComponentPortAllocationEnds.eType = ComponentPortAllocationEnd
ComponentPortAllocation._allocatedPort.eType = Port
ComponentPortAllocation._allocatingPort.eType = Port
ComponentPortAllocationEnd.port.eType = Port
ComponentPortAllocationEnd.part.eType = Part
ComponentPortAllocationEnd._owningComponentPortAllocation.eType = ComponentPortAllocation
FunctionalChainInvolvementLink.exchangeContext.eType = Constraint
FunctionalChainInvolvementLink.exchangedItems.eType = ExchangeItem
FunctionalChainInvolvementLink.source.eType = FunctionalChainInvolvementFunction
FunctionalChainInvolvementLink.target.eType = FunctionalChainInvolvementFunction
SequenceLink.condition.eType = Constraint
SequenceLink.links.eType = FunctionalChainInvolvementLink
SequenceLink.source.eType = SequenceLinkEnd
SequenceLink.target.eType = SequenceLinkEnd
FunctionalChainInvolvementFunction.outgoingInvolvementLinks.eType = FunctionalChainInvolvementLink
FunctionalChainInvolvementFunction.incomingInvolvementLinks.eType = FunctionalChainInvolvementLink
ReferenceHierarchyContext.sourceReferenceHierarchy.eType = FunctionalChainReference
ReferenceHierarchyContext.targetReferenceHierarchy.eType = FunctionalChainReference
AbstractFunctionalBlock.functionalAllocations.eType = ComponentFunctionalAllocation
AbstractFunctionalBlock.allocatedFunctions.eType = AbstractFunction
ExchangeLink.exchangeContainmentLinks.eType = ExchangeContainment
ExchangeContainment.exchange.eType = ExchangeSpecification
ExchangeContainment.link.eType = ExchangeLink
ExchangeContainment.link.eOpposite = ExchangeLink.exchangeContainmentLinks
ExchangeSpecification.link.eType = ExchangeContainment
ExchangeSpecification.link.eOpposite = ExchangeContainment.exchange
ExchangeSpecification.outgoingExchangeSpecificationRealizations.eType = ExchangeSpecificationRealization
ExchangeSpecification.incomingExchangeSpecificationRealizations.eType = ExchangeSpecificationRealization
FunctionalChain.involvedFunctions.eType = AbstractFunction
FunctionalChain.involvedFunctionalExchanges.eType = FunctionalExchange
ComponentFunctionalAllocation._function.eType = AbstractFunction
ComponentFunctionalAllocation._block.eType = AbstractFunctionalBlock
ComponentFunctionalAllocation._block.eOpposite = AbstractFunctionalBlock.functionalAllocations
ExchangeSpecificationRealization._realizedExchangeSpecification.eType = ExchangeSpecification
ExchangeSpecificationRealization._realizedExchangeSpecification.eOpposite = ExchangeSpecification.incomingExchangeSpecificationRealizations
ExchangeSpecificationRealization._realizingExchangeSpecification.eType = ExchangeSpecification
ExchangeSpecificationRealization._realizingExchangeSpecification.eOpposite = ExchangeSpecification.outgoingExchangeSpecificationRealizations
FunctionalExchangeRealization._realizedFunctionalExchange.eType = FunctionalExchange
FunctionalExchangeRealization._realizingFunctionalExchange.eType = FunctionalExchange
FunctionRealization._allocatedFunction.eType = AbstractFunction
FunctionRealization._allocatingFunction.eType = AbstractFunction
FunctionalExchange.involvingFunctionalChains.eType = FunctionalChain
FunctionalExchange.involvingFunctionalChains.eOpposite = FunctionalChain.involvedFunctionalExchanges
FunctionalExchange.allocatingComponentExchanges.eType = ComponentExchange
FunctionalExchange.incomingComponentExchangeFunctionalExchangeRealizations.eType = ComponentExchangeFunctionalExchangeAllocation
FunctionalExchange.incomingFunctionalExchangeRealizations.eType = FunctionalExchangeRealization
#FunctionalExchange.incomingFunctionalExchangeRealizations.eOpposite = FunctionalExchangeRealization.realizedFunctionalExchange
FunctionalExchange.outgoingFunctionalExchangeRealizations.eType = FunctionalExchangeRealization
#FunctionalExchange.outgoingFunctionalExchangeRealizations.eOpposite = FunctionalExchangeRealization.realizingFunctionalExchange
FunctionalExchange.realizedFunctionalExchanges.eType = FunctionalExchange
FunctionalExchange.realizingFunctionalExchanges.eType = FunctionalExchange
FunctionalExchange.realizingFunctionalExchanges.eOpposite = FunctionalExchange.realizedFunctionalExchanges
AbstractFunction.outFunctionRealizations.eType = FunctionRealization
#AbstractFunction.outFunctionRealizations.eOpposite = FunctionRealization.allocatingFunction
AbstractFunction.inFunctionRealizations.eType = FunctionRealization
#AbstractFunction.inFunctionRealizations.eOpposite = FunctionRealization.allocatedFunction
AbstractFunction.componentFunctionalAllocations.eType = ComponentFunctionalAllocation
#AbstractFunction.componentFunctionalAllocations.eOpposite = ComponentFunctionalAllocation.function
AbstractFunction.allocationBlocks.eType = AbstractFunctionalBlock
AbstractFunction.allocationBlocks.eOpposite = AbstractFunctionalBlock.allocatedFunctions
AbstractFunction.involvingFunctionalChains.eType = FunctionalChain
AbstractFunction.involvingFunctionalChains.eOpposite = FunctionalChain.involvedFunctions
FunctionPort.allocatorComponentPorts.eType = ComponentPort
ComponentExchange.allocatedFunctionalExchanges.eType = FunctionalExchange
ComponentExchange.allocatedFunctionalExchanges.eOpposite = FunctionalExchange.allocatingComponentExchanges
ComponentExchange.incomingComponentExchangeRealizations.eType = ComponentExchangeRealization
ComponentExchange.outgoingComponentExchangeRealizations.eType = ComponentExchangeRealization
ComponentExchange.outgoingComponentExchangeFunctionalExchangeAllocations.eType = ComponentExchangeFunctionalExchangeAllocation
ComponentExchange.realizedComponentExchanges.eType = ComponentExchange
ComponentExchange.realizingComponentExchanges.eType = ComponentExchange
ComponentExchange.realizingComponentExchanges.eOpposite = ComponentExchange.realizedComponentExchanges
ComponentExchangeFunctionalExchangeAllocation._allocatedFunctionalExchange.eType = FunctionalExchange
ComponentExchangeFunctionalExchangeAllocation._allocatedFunctionalExchange.eOpposite = FunctionalExchange.incomingComponentExchangeFunctionalExchangeRealizations
ComponentExchangeFunctionalExchangeAllocation._allocatingComponentExchange.eType = ComponentExchange
ComponentExchangeFunctionalExchangeAllocation._allocatingComponentExchange.eOpposite = ComponentExchange.outgoingComponentExchangeFunctionalExchangeAllocations
ComponentExchangeRealization._allocatedComponentExchange.eType = ComponentExchange
ComponentExchangeRealization._allocatedComponentExchange.eOpposite = ComponentExchange.incomingComponentExchangeRealizations
ComponentExchangeRealization._allocatingComponentExchange.eType = ComponentExchange
ComponentExchangeRealization._allocatingComponentExchange.eOpposite = ComponentExchange.outgoingComponentExchangeRealizations
ComponentPort.allocatedFunctionPorts.eType = FunctionPort
ComponentPort.allocatedFunctionPorts.eOpposite = FunctionPort.allocatorComponentPorts
ComponentPort.delegatedComponentPorts.eType = ComponentPort
ComponentPort.delegatingComponentPorts.eType = ComponentPort
ComponentPort.delegatingComponentPorts.eOpposite = ComponentPort.delegatedComponentPorts
ComponentPort.allocatingPhysicalPorts.eType = PhysicalPort
ComponentPort.realizedComponentPorts.eType = ComponentPort
ComponentPort.realizingComponentPorts.eType = ComponentPort
ComponentPort.realizingComponentPorts.eOpposite = ComponentPort.realizedComponentPorts

print('fa.cross_init done')

print('communication.cross_init starting')


print('communication.cross_init done')

print('datatype.cross_init starting')


print('datatype.cross_init done')

print('datavalue.cross_init starting')


print('datavalue.cross_init done')

print('information.cross_init starting')


CommunicationItem.ownedStateMachines.eType = StateMachine
CommunicationItem.properties.eType = Property
MessageReference.message.eType = Message
MessageReferencePkg.ownedMessageReferences.eType = MessageReference
Signal.signalInstances.eType = SignalInstance
CommunicationLink.exchangeItem.eType = ExchangeItem
CommunicationLinkExchanger.ownedCommunicationLinks.eType = CommunicationLink
CommunicationLinkExchanger.produce.eType = CommunicationLink
CommunicationLinkExchanger.consume.eType = CommunicationLink
CommunicationLinkExchanger.send.eType = CommunicationLink
CommunicationLinkExchanger.receive.eType = CommunicationLink
CommunicationLinkExchanger.call.eType = CommunicationLink
CommunicationLinkExchanger.execute.eType = CommunicationLink
CommunicationLinkExchanger.write.eType = CommunicationLink
CommunicationLinkExchanger.access.eType = CommunicationLink
CommunicationLinkExchanger.acquire.eType = CommunicationLink
CommunicationLinkExchanger.transmit.eType = CommunicationLink
DataType._defaultValue.eType = DataValue
DataType._nullValue.eType = DataValue
DataType.ownedInformationRealizations.eType = InformationRealization
BooleanType.ownedLiterals.eType = LiteralBooleanValue
BooleanType.ownedDefaultValue.eType = AbstractBooleanValue
Enumeration.ownedLiterals.eType = EnumerationLiteral
Enumeration.ownedDefaultValue.eType = AbstractEnumerationValue
Enumeration.ownedNullValue.eType = AbstractEnumerationValue
Enumeration.ownedMinValue.eType = AbstractEnumerationValue
Enumeration.ownedMaxValue.eType = AbstractEnumerationValue
Enumeration.domainType.eType = DataType
StringType.ownedDefaultValue.eType = AbstractStringValue
StringType.ownedNullValue.eType = AbstractStringValue
StringType.ownedMinLength.eType = NumericValue
StringType.ownedMaxLength.eType = NumericValue
NumericType.ownedDefaultValue.eType = NumericValue
NumericType.ownedNullValue.eType = NumericValue
NumericType.ownedMinValue.eType = NumericValue
NumericType.ownedMaxValue.eType = NumericValue
PhysicalQuantity.unit.eType = Unit
DataValue._type.eType = Type
DataValueContainer.ownedDataValues.eType = DataValue
AbstractBooleanValue._booleanType.eType = BooleanType
BooleanReference.referencedValue.eType = AbstractBooleanValue
BooleanReference.referencedProperty.eType = Property
AbstractEnumerationValue._enumerationType.eType = Enumeration
EnumerationLiteral.domainValue.eType = DataValue
EnumerationReference.referencedValue.eType = AbstractEnumerationValue
EnumerationReference.referencedProperty.eType = Property
AbstractStringValue._stringType.eType = StringType
StringReference.referencedValue.eType = AbstractStringValue
StringReference.referencedProperty.eType = Property
NumericValue.unit.eType = Unit
NumericValue._numericType.eType = NumericType
NumericReference.referencedValue.eType = NumericValue
NumericReference.referencedProperty.eType = Property
AbstractComplexValue._complexType.eType = Classifier
ComplexValue.ownedParts.eType = ValuePart
ComplexValueReference.referencedValue.eType = AbstractComplexValue
ComplexValueReference.referencedProperty.eType = Property
ValuePart.referencedProperty.eType = Property
ValuePart.ownedValue.eType = DataValue
AbstractExpressionValue._expressionType.eType = DataType
BinaryExpression.ownedLeftOperand.eType = DataValue
BinaryExpression.ownedRightOperand.eType = DataValue
UnaryExpression.ownedOperand.eType = DataValue
AbstractInstance.representingInstanceRoles.eType = InstanceRole
AssociationPkg.ownedAssociations.eType = Association
Association.ownedMembers.eType = Property
Association.navigableMembers.eType = Property
Class.keyParts.eType = KeyPart
Class.ownedStateMachines.eType = StateMachine
Class.ownedDataValues.eType = DataValue
Class.ownedInformationRealizations.eType = InformationRealization
Collection.type.eType = Type
Collection.index.eType = DataType
Collection.containedOperations.eType = Operation
CollectionValue.ownedElements.eType = DataValue
CollectionValue.ownedDefaultElement.eType = DataValue
CollectionValueReference.referencedValue.eType = AbstractCollectionValue
CollectionValueReference.referencedProperty.eType = Property
DataPkg.ownedDataPkgs.eType = DataPkg
DataPkg.ownedClasses.eType = Class
DataPkg.ownedKeyParts.eType = KeyPart
DataPkg.ownedCollections.eType = Collection
DataPkg.ownedUnits.eType = Unit
DataPkg.ownedDataTypes.eType = DataType
DataPkg.ownedSignals.eType = Signal
DataPkg.ownedMessages.eType = Message
DataPkg.ownedExceptions.eType = Exception
DataPkg.ownedStateEvents.eType = StateEvent
KeyPart.property.eType = Property
MultiplicityElement.ownedDefaultValue.eType = DataValue
MultiplicityElement.ownedMinValue.eType = DataValue
MultiplicityElement.ownedMaxValue.eType = DataValue
MultiplicityElement.ownedNullValue.eType = DataValue
MultiplicityElement.ownedMinCard.eType = NumericValue
MultiplicityElement.ownedMinLength.eType = NumericValue
MultiplicityElement.ownedMaxCard.eType = NumericValue
MultiplicityElement.ownedMaxLength.eType = NumericValue
Operation.ownedParameters.eType = Parameter
Operation.ownedOperationAllocation.eType = OperationAllocation
Operation.ownedExchangeItemRealizations.eType = ExchangeItemRealization
OperationAllocation._allocatedOperation.eType = Operation
OperationAllocation._allocatingOperation.eType = Operation
Property._association.eType = Association
Service.thrownExceptions.eType = Exception
Service.messages.eType = Message
Service.messageReferences.eType = MessageReference
Union.discriminant.eType = UnionProperty
Union.defaultProperty.eType = UnionProperty
Union.containedUnionProperties.eType = UnionProperty
UnionProperty.qualifier.eType = DataValue
Port.ownedProtocols.eType = StateMachine
Port.providedInterfaces.eType = Interface
Port.requiredInterfaces.eType = Interface
Port.ownedPortRealizations.eType = PortRealization
Port.ownedPortAllocations.eType = PortAllocation
ExchangeItem.ownedElements.eType = ExchangeItemElement
ExchangeItem.ownedInformationRealizations.eType = InformationRealization
ExchangeItem.ownedExchangeItemInstances.eType = ExchangeItemInstance
ExchangeItem.allocatorInterfaces.eType = Interface
ExchangeItemElement.referencedProperties.eType = Property
ExchangeItemRealization._realizedItem.eType = AbstractExchangeItem
ExchangeItemRealization._realizingOperation.eType = Operation
AbstractEventOperation.invokingSequenceMessages.eType = SequenceMessage
DataType.realizedDataTypes.eType = DataType
DataType.realizingDataTypes.eType = DataType
DataType.realizingDataTypes.eOpposite = DataType.realizedDataTypes
Class.realizedClasses.eType = Class
Class.realizingClasses.eType = Class
Class.realizingClasses.eOpposite = Class.realizedClasses
Operation.allocatingOperations.eType = Operation
Operation.allocatedOperations.eType = Operation
Operation.allocatedOperations.eOpposite = Operation.allocatingOperations
Operation.realizedExchangeItems.eType = ExchangeItem
Port.incomingPortRealizations.eType = PortRealization
Port.outgoingPortRealizations.eType = PortRealization
Port.incomingPortAllocations.eType = PortAllocation
Port.outgoingPortAllocations.eType = PortAllocation
PortRealization._realizedPort.eType = Port
PortRealization._realizedPort.eOpposite = Port.incomingPortRealizations
PortRealization._realizingPort.eType = Port
PortRealization._realizingPort.eOpposite = Port.outgoingPortRealizations
PortAllocation._allocatedPort.eType = Port
PortAllocation._allocatedPort.eOpposite = Port.incomingPortAllocations
PortAllocation._allocatingPort.eType = Port
PortAllocation._allocatingPort.eOpposite = Port.outgoingPortAllocations
ExchangeItem.realizedExchangeItems.eType = ExchangeItem
ExchangeItem.realizingExchangeItems.eType = ExchangeItem
ExchangeItem.realizingExchangeItems.eOpposite = ExchangeItem.realizedExchangeItems
ExchangeItem.realizingOperations.eType = Operation
ExchangeItem.realizingOperations.eOpposite = Operation.realizedExchangeItems

print('information.cross_init done')

print('interaction.cross_init starting')


SequenceMessage.exchangeContext.eType = Constraint
SequenceMessage.sendingEnd.eType = MessageEnd
SequenceMessage.receivingEnd.eType = MessageEnd
SequenceMessage._invokedOperation.eType = AbstractEventOperation
SequenceMessage.exchangedItems.eType = ExchangeItem
SequenceMessage._sendingPart.eType = Part
SequenceMessage._receivingPart.eType = Part
SequenceMessage._sendingFunction.eType = AbstractFunction
SequenceMessage._receivingFunction.eType = AbstractFunction
SequenceMessage.ownedSequenceMessageValuations.eType = SequenceMessageValuation
Scenario.preCondition.eType = Constraint
Scenario.postCondition.eType = Constraint
Scenario.ownedInstanceRoles.eType = InstanceRole
Scenario.ownedMessages.eType = SequenceMessage
Scenario.ownedInteractionFragments.eType = InteractionFragment
Scenario.ownedTimeLapses.eType = TimeLapse
Scenario.ownedEvents.eType = Event
Scenario.ownedFormalGates.eType = Gate
Scenario.ownedScenarioRealization.eType = ScenarioRealization
Scenario.ownedConstraintDurations.eType = ConstraintDuration
Scenario.containedFunctions.eType = AbstractFunction
Scenario.containedParts.eType = Part
Scenario.referencedScenarios.eType = Scenario
MessageEnd._message.eType = SequenceMessage
Execution._covered.eType = InstanceRole
ExecutionEnd._execution.eType = Execution
InstanceRole.representedInstance.eType = AbstractInstance
AbstractEnd.event.eType = Event
EventReceiptOperation.operation.eType = AbstractEventOperation
EventSentOperation.operation.eType = AbstractEventOperation
AbstractCapability.preCondition.eType = Constraint
AbstractCapability.postCondition.eType = Constraint
AbstractCapability.ownedScenarios.eType = Scenario
AbstractCapability.extends.eType = AbstractCapabilityExtend
AbstractCapability.extending.eType = AbstractCapabilityExtend
AbstractCapability.abstractCapabilityExtensionPoints.eType = AbstractCapabilityExtensionPoint
AbstractCapability.superGeneralizations.eType = AbstractCapabilityGeneralization
AbstractCapability.subGeneralizations.eType = AbstractCapabilityGeneralization
AbstractCapability.includes.eType = AbstractCapabilityInclude
AbstractCapability.including.eType = AbstractCapabilityInclude
AbstractCapability.super.eType = AbstractCapability
AbstractCapability.sub.eType = AbstractCapability
AbstractCapability.includedAbstractCapabilities.eType = AbstractCapability
AbstractCapability.includingAbstractCapabilities.eType = AbstractCapability
AbstractCapability.extendedAbstractCapabilities.eType = AbstractCapability
AbstractCapability.extendingAbstractCapabilities.eType = AbstractCapability
AbstractCapability.ownedFunctionalChainAbstractCapabilityInvolvements.eType = FunctionalChainAbstractCapabilityInvolvement
AbstractCapability.ownedAbstractFunctionAbstractCapabilityInvolvements.eType = AbstractFunctionAbstractCapabilityInvolvement
AbstractCapability.availableInStates.eType = State
AbstractCapability.ownedAbstractCapabilityRealizations.eType = AbstractCapabilityRealization
AbstractCapability.involvedAbstractFunctions.eType = AbstractFunction
AbstractCapability.involvedFunctionalChains.eType = FunctionalChain
AbstractCapabilityExtend.extended.eType = AbstractCapability
AbstractCapabilityExtend._extension.eType = AbstractCapability
AbstractCapabilityExtensionPoint._abstractCapability.eType = AbstractCapability
AbstractCapabilityGeneralization.super.eType = AbstractCapability
AbstractCapabilityGeneralization._sub.eType = AbstractCapability
AbstractCapabilityInclude.included.eType = AbstractCapability
AbstractCapabilityInclude._inclusion.eType = AbstractCapability
InteractionFragment.coveredInstanceRoles.eType = InstanceRole
InteractionState.relatedAbstractState.eType = AbstractState
InteractionState.relatedAbstractFunction.eType = AbstractFunction
InteractionState._covered.eType = InstanceRole
InteractionUse.referencedScenario.eType = Scenario
InteractionUse.actualGates.eType = Gate
CombinedFragment.referencedOperands.eType = InteractionOperand
CombinedFragment.expressionGates.eType = Gate
InteractionOperand.referencedInteractionFragments.eType = InteractionFragment
InteractionOperand.guard.eType = Constraint
TimeLapse.start.eType = InteractionFragment
TimeLapse.finish.eType = InteractionFragment
AbstractFragment.ownedGates.eType = Gate
FragmentEnd._abstractFragment.eType = AbstractFragment
FunctionalChainAbstractCapabilityInvolvement._capability.eType = AbstractCapability
FunctionalChainAbstractCapabilityInvolvement._functionalChain.eType = FunctionalChain
AbstractFunctionAbstractCapabilityInvolvement._capability.eType = AbstractCapability
AbstractFunctionAbstractCapabilityInvolvement._function.eType = AbstractFunction
ScenarioRealization._realizedScenario.eType = Scenario
ScenarioRealization._realizingScenario.eType = Scenario
StateFragment.relatedAbstractState.eType = AbstractState
StateFragment.relatedAbstractFunction.eType = AbstractFunction
ConstraintDuration.start.eType = InteractionFragment
ConstraintDuration.finish.eType = InteractionFragment
SequenceMessageValuation.exchangeItemElement.eType = ExchangeItemElement
SequenceMessageValuation.value.eType = ValueSpecification
Scenario.realizedScenarios.eType = Scenario
Scenario.realizingScenarios.eType = Scenario
Scenario.realizingScenarios.eOpposite = Scenario.realizedScenarios
InstanceRole.abstractEnds.eType = AbstractEnd
AbstractEnd._covered.eType = InstanceRole
AbstractEnd._covered.eOpposite = InstanceRole.abstractEnds
AbstractCapabilityRealization._realizedCapability.eType = AbstractCapability
AbstractCapabilityRealization._realizingCapability.eType = AbstractCapability
AbstractCapability.incomingCapabilityAllocation.eType = AbstractCapabilityRealization
#AbstractCapability.incomingCapabilityAllocation.eOpposite = AbstractCapabilityRealization.realizedCapability
AbstractCapability.outgoingCapabilityAllocation.eType = AbstractCapabilityRealization
#AbstractCapability.outgoingCapabilityAllocation.eOpposite = AbstractCapabilityRealization.realizingCapability
AbstractCapabilityExtend.extensionLocation.eType = AbstractCapabilityExtensionPoint
AbstractCapabilityExtensionPoint.extendLinks.eType = AbstractCapabilityExtend
AbstractCapabilityExtensionPoint.extendLinks.eOpposite = AbstractCapabilityExtend.extensionLocation

print('interaction.cross_init done')

print('la.cross_init starting')


LogicalArchitecturePkg.ownedLogicalArchitectures.eType = LogicalArchitecture
LogicalArchitecture.ownedLogicalComponentPkg.eType = LogicalComponentPkg
LogicalArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
LogicalArchitecture._containedLogicalFunctionPkg.eType = LogicalFunctionPkg
LogicalArchitecture.ownedSystemAnalysisRealizations.eType = SystemAnalysisRealization
LogicalArchitecture.allocatedSystemAnalysisRealizations.eType = SystemAnalysisRealization
LogicalFunction.ownedLogicalFunctionPkgs.eType = LogicalFunctionPkg
LogicalFunction.containedLogicalFunctions.eType = LogicalFunction
LogicalFunction.childrenLogicalFunctions.eType = LogicalFunction
LogicalFunctionPkg.ownedLogicalFunctions.eType = LogicalFunction
LogicalFunctionPkg.ownedLogicalFunctionPkgs.eType = LogicalFunctionPkg
LogicalComponent.ownedLogicalComponents.eType = LogicalComponent
LogicalComponent.ownedLogicalArchitectures.eType = LogicalArchitecture
LogicalComponent.ownedLogicalComponentPkgs.eType = LogicalComponentPkg
LogicalComponent.subLogicalComponents.eType = LogicalComponent
LogicalComponent.realizedSystemComponents.eType = SystemComponent
LogicalComponentPkg.ownedLogicalComponents.eType = LogicalComponent
LogicalComponentPkg.ownedLogicalComponentPkgs.eType = LogicalComponentPkg
CapabilityRealization.ownedCapabilityRealizationInvolvements.eType = CapabilityRealizationInvolvement
CapabilityRealization.involvedComponents.eType = CapabilityRealizationInvolvedElement
CapabilityRealizationPkg.ownedCapabilityRealizations.eType = CapabilityRealization
CapabilityRealizationPkg.ownedCapabilityRealizationPkgs.eType = CapabilityRealizationPkg
LogicalArchitecture.allocatedSystemAnalyses.eType = SystemAnalysis
LogicalArchitecture.allocatingPhysicalArchitectures.eType = PhysicalArchitecture
LogicalFunction.allocatingLogicalComponents.eType = LogicalComponent
LogicalFunction.realizedSystemFunctions.eType = SystemFunction
LogicalFunction.realizingPhysicalFunctions.eType = PhysicalFunction
LogicalComponent.allocatedLogicalFunctions.eType = LogicalFunction
LogicalComponent.allocatedLogicalFunctions.eOpposite = LogicalFunction.allocatingLogicalComponents
LogicalComponent.realizingPhysicalComponents.eType = PhysicalComponent
CapabilityRealization.realizedCapabilities.eType = Capability
CapabilityRealization.realizedCapabilityRealizations.eType = CapabilityRealization
CapabilityRealization.realizingCapabilityRealizations.eType = CapabilityRealization
CapabilityRealization.realizingCapabilityRealizations.eOpposite = CapabilityRealization.realizedCapabilityRealizations

print('la.cross_init done')

print('libraries.cross_init starting')


ModelInformation.ownedReferences.eType = LibraryReference
ModelInformation.version.eType = ModelVersion
LibraryReference.library.eType = ModelInformation
LibraryReference.version.eType = ModelVersion

print('libraries.cross_init done')

print('modellingcore.cross_init starting')


ModelElement.constraints.eType = AbstractConstraint
ModelElement.ownedConstraints.eType = AbstractConstraint
ModelElement.ownedMigratedElements.eType = ModelElement
InformationsExchanger.incomingInformationFlows.eType = AbstractInformationFlow
InformationsExchanger.outgoingInformationFlows.eType = AbstractInformationFlow
InformationsExchanger.informationFlows.eType = AbstractInformationFlow
TraceableElement.incomingTraces.eType = AbstractTrace
TraceableElement.outgoingTraces.eType = AbstractTrace
AbstractType.abstractTypedElements.eType = AbstractTypedElement
AbstractTypedElement.abstractType.eType = AbstractType
AbstractTrace.targetElement.eType = TraceableElement
AbstractTrace.sourceElement.eType = TraceableElement
AbstractConstraint.constrainedElements.eType = ModelElement
AbstractConstraint.ownedSpecification.eType = ValueSpecification
AbstractConstraint._context.eType = ModelElement
AbstractParameter.rate.eType = ValueSpecification
AbstractParameter.probability.eType = ValueSpecification
AbstractParameterSet.ownedConditions.eType = AbstractConstraint
AbstractParameterSet.probability.eType = ValueSpecification
AbstractInformationFlow.convoyedInformations.eType = AbstractExchangeItem
AbstractInformationFlow.source.eType = InformationsExchanger
AbstractInformationFlow.target.eType = InformationsExchanger
IState.referencedStates.eType = IState
IState.exploitedStates.eType = IState
AbstractRelationship.realizedFlow.eType = AbstractInformationFlow
AbstractParameter.parameterSet.eType = AbstractParameterSet
AbstractParameterSet.parameters.eType = AbstractParameter
AbstractParameterSet.parameters.eOpposite = AbstractParameter.parameterSet
AbstractInformationFlow.realizations.eType = AbstractRelationship
AbstractInformationFlow.realizations.eOpposite = AbstractRelationship.realizedFlow

print('modellingcore.cross_init done')

print('oa.cross_init starting')


OperationalAnalysis.ownedRolePkg.eType = RolePkg
OperationalAnalysis.ownedEntityPkg.eType = EntityPkg
OperationalAnalysis.ownedConceptPkg.eType = ConceptPkg
OperationalAnalysis._containedOperationalCapabilityPkg.eType = OperationalCapabilityPkg
OperationalAnalysis._containedOperationalActivityPkg.eType = OperationalActivityPkg
OperationalActivityPkg.ownedOperationalActivities.eType = OperationalActivity
OperationalActivityPkg.ownedOperationalActivityPkgs.eType = OperationalActivityPkg
OperationalActivity.ownedOperationalActivityPkgs.eType = OperationalActivityPkg
OperationalActivity.ownedSwimlanes.eType = Swimlane
OperationalActivity.ownedProcess.eType = OperationalProcess
OperationalActivity.allocatingRoles.eType = Role
OperationalActivity.containedOperationalActivities.eType = OperationalActivity
OperationalActivity.childrenOperationalActivities.eType = OperationalActivity
OperationalProcess.involvingOperationalCapabilities.eType = OperationalCapability
Swimlane._representedEntity.eType = Entity
OperationalCapabilityPkg.ownedOperationalCapabilities.eType = OperationalCapability
OperationalCapabilityPkg.ownedOperationalCapabilityPkgs.eType = OperationalCapabilityPkg
OperationalCapabilityPkg.ownedCapabilityConfigurations.eType = CapabilityConfiguration
OperationalCapabilityPkg.ownedConceptCompliances.eType = ConceptCompliance
OperationalCapability.compliances.eType = ConceptCompliance
OperationalCapability.configurations.eType = CapabilityConfiguration
OperationalCapability.ownedEntityOperationalCapabilityInvolvements.eType = EntityOperationalCapabilityInvolvement
OperationalCapability.involvedEntities.eType = Entity
RolePkg.ownedRolePkgs.eType = RolePkg
RolePkg.ownedRoles.eType = Role
Role.ownedRoleAssemblyUsages.eType = RoleAssemblyUsage
Role.ownedActivityAllocations.eType = ActivityAllocation
Role.allocatingEntities.eType = Entity
Role.allocatedOperationalActivities.eType = OperationalActivity
RoleAssemblyUsage.child.eType = Role
EntityPkg.ownedEntities.eType = Entity
EntityPkg.ownedEntityPkgs.eType = EntityPkg
EntityPkg.ownedLocations.eType = Location
EntityPkg.ownedCommunicationMeans.eType = CommunicationMean
Entity.organisationalUnitMemberships.eType = OrganisationalUnitComposition
Entity.actualLocation.eType = Location
Entity.subEntities.eType = Entity
Entity.ownedEntities.eType = Entity
Entity.ownedCommunicationMeans.eType = CommunicationMean
Entity.ownedRoleAllocations.eType = RoleAllocation
Entity.allocatedRoles.eType = Role
Entity.involvingOperationalCapabilities.eType = OperationalCapability
Entity.realizingSystemComponents.eType = SystemComponent
ConceptPkg.ownedConceptPkgs.eType = ConceptPkg
ConceptPkg.ownedConcepts.eType = Concept
Concept.compliances.eType = ConceptCompliance
Concept.compositeLinks.eType = ItemInConcept
ConceptCompliance.complyWithConcept.eType = Concept
ConceptCompliance.compliantCapability.eType = OperationalCapability
ItemInConcept.concept.eType = Concept
ItemInConcept.item.eType = AbstractConceptItem
AbstractConceptItem.composingLinks.eType = ItemInConcept
CommunityOfInterest.communityOfInterestCompositions.eType = CommunityOfInterestComposition
CommunityOfInterestComposition.communityOfInterest.eType = CommunityOfInterest
CommunityOfInterestComposition.interestedOrganisationUnit.eType = OrganisationalUnit
OrganisationalUnit.organisationalUnitCompositions.eType = OrganisationalUnitComposition
OrganisationalUnit.communityOfInterestMemberships.eType = CommunityOfInterestComposition
OrganisationalUnitComposition.organisationalUnit.eType = OrganisationalUnit
OrganisationalUnitComposition.participatingEntity.eType = Entity
Location.locatedEntities.eType = Entity
CapabilityConfiguration.configuredCapability.eType = OperationalCapability
CommunicationMean._sourceEntity.eType = Entity
CommunicationMean._targetEntity.eType = Entity
EntityOperationalCapabilityInvolvement._entity.eType = Entity
EntityOperationalCapabilityInvolvement._capability.eType = OperationalCapability
OperationalAnalysis.allocatingSystemAnalyses.eType = SystemAnalysis
OperationalActivity.activityAllocations.eType = ActivityAllocation
OperationalActivity.allocatorEntities.eType = Entity
OperationalActivity.realizingSystemFunctions.eType = SystemFunction
OperationalCapability.realizingCapabilities.eType = Capability
ActivityAllocation._role.eType = Role
ActivityAllocation._activity.eType = OperationalActivity
ActivityAllocation._activity.eOpposite = OperationalActivity.activityAllocations
Role.roleAllocations.eType = RoleAllocation
Role.activityAllocations.eType = ActivityAllocation
#Role.activityAllocations.eOpposite = ActivityAllocation.role
RoleAllocation._role.eType = Role
RoleAllocation._role.eOpposite = Role.roleAllocations
RoleAllocation._entity.eType = Entity
Entity.roleAllocations.eType = RoleAllocation
#Entity.roleAllocations.eOpposite = RoleAllocation.entity
Entity.allocatedOperationalActivities.eType = OperationalActivity
Entity.allocatedOperationalActivities.eOpposite = OperationalActivity.allocatorEntities

print('oa.cross_init done')

print('pa.cross_init starting')


ComponentInstance.portInstances.eType = PortInstance
ComponentInstance.ownedAbstractPhysicalInstances.eType = AbstractPhysicalInstance
ComponentInstance.ownedInstanceDeploymentLinks.eType = InstanceDeploymentLink
ComponentInstance.type.eType = PhysicalComponent
ConnectionInstance.type.eType = ComponentExchange
DeploymentAspect.ownedConfigurations.eType = DeploymentConfiguration
DeploymentAspect.ownedDeploymentAspects.eType = DeploymentAspect
DeploymentConfiguration.ownedDeploymentLinks.eType = AbstractDeploymentLink
DeploymentConfiguration.ownedPhysicalInstances.eType = AbstractPhysicalInstance
PortInstance._component.eType = ComponentInstance
PortInstance.type.eType = ComponentPort
PhysicalArchitecturePkg.ownedPhysicalArchitecturePkgs.eType = PhysicalArchitecturePkg
PhysicalArchitecturePkg.ownedPhysicalArchitectures.eType = PhysicalArchitecture
PhysicalArchitecture.ownedPhysicalComponentPkg.eType = PhysicalComponentPkg
PhysicalArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
PhysicalArchitecture._containedPhysicalFunctionPkg.eType = PhysicalFunctionPkg
PhysicalArchitecture.ownedDeployments.eType = AbstractDeploymentLink
PhysicalArchitecture.ownedLogicalArchitectureRealizations.eType = LogicalArchitectureRealization
PhysicalArchitecture.allocatedLogicalArchitectureRealizations.eType = LogicalArchitectureRealization
PhysicalFunction.ownedPhysicalFunctionPkgs.eType = PhysicalFunctionPkg
PhysicalFunction.containedPhysicalFunctions.eType = PhysicalFunction
PhysicalFunction.childrenPhysicalFunctions.eType = PhysicalFunction
PhysicalFunctionPkg.ownedPhysicalFunctions.eType = PhysicalFunction
PhysicalFunctionPkg.ownedPhysicalFunctionPkgs.eType = PhysicalFunctionPkg
PhysicalComponent.ownedDeploymentLinks.eType = AbstractDeploymentLink
PhysicalComponent.ownedPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.ownedPhysicalComponentPkgs.eType = PhysicalComponentPkg
PhysicalComponent.logicalInterfaceRealizations.eType = LogicalInterfaceRealization
PhysicalComponent.subPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.deployedPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.deployingPhysicalComponents.eType = PhysicalComponent
PhysicalComponentPkg.ownedPhysicalComponents.eType = PhysicalComponent
PhysicalComponentPkg.ownedPhysicalComponentPkgs.eType = PhysicalComponentPkg
PhysicalComponentPkg.ownedKeyParts.eType = KeyPart
PhysicalComponentPkg.ownedDeployments.eType = AbstractDeploymentLink
PhysicalNode.subPhysicalNodes.eType = PhysicalNode
ConnectionInstance.connectionEnds.eType = PortInstance
PortInstance.connections.eType = ConnectionInstance
PortInstance.connections.eOpposite = ConnectionInstance.connectionEnds
PhysicalArchitecture.allocatedLogicalArchitectures.eType = LogicalArchitecture
PhysicalArchitecture.allocatingEpbsArchitectures.eType = EPBSArchitecture
PhysicalFunction.allocatingPhysicalComponents.eType = PhysicalComponent
PhysicalFunction.realizedLogicalFunctions.eType = LogicalFunction
PhysicalComponent.realizedLogicalComponents.eType = LogicalComponent
PhysicalComponent.allocatedPhysicalFunctions.eType = PhysicalFunction
PhysicalComponent.allocatedPhysicalFunctions.eOpposite = PhysicalFunction.allocatingPhysicalComponents

print('pa.cross_init done')

print('deployment.cross_init starting')


print('deployment.cross_init done')

print('requirement.cross_init starting')


RequirementsPkg.ownedRequirements.eType = Requirement
RequirementsPkg.ownedRequirementPkgs.eType = RequirementsPkg
RequirementsTrace._source.eType = TraceableElement
RequirementsTrace._target.eType = TraceableElement
Requirement.relatedCapellaElements.eType = CapellaElement

print('requirement.cross_init done')

print('sharedmodel.cross_init starting')


SharedPkg.ownedDataPkg.eType = DataPkg
SharedPkg.ownedGenericPkg.eType = GenericPkg
GenericPkg.subGenericPkgs.eType = GenericPkg
GenericPkg.capellaElements.eType = CapellaElement

print('sharedmodel.cross_init done')
