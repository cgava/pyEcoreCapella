import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import behavior
import modellingcore
import activity
import capellacommon
import capellacore
import capellamodeller
import cs
import ctx
import epbs
import fa
import information
import information.communication
import information.datatype
import information.datavalue
import interaction
import la
import oa
import pa
import pa.deployment
import requirement
import sharedmodel
import libraries
import emde

#print('behavior.cross_init starting')


behavior.AbstractBehavior.ownedParameterSet.eType = modellingcore.AbstractParameterSet
behavior.AbstractBehavior.ownedParameter.eType = modellingcore.AbstractParameter
behavior.AbstractTimeEvent.when.eType = behavior.TimeExpression
behavior.AbstractSignalEvent.signal.eType = behavior.AbstractSignal
behavior.TimeExpression.observations.eType = modellingcore.AbstractNamedElement
behavior.TimeExpression.expression.eType = modellingcore.ValueSpecification

#print('behavior.cross_init done')

#print('modellingcore.cross_init starting')


modellingcore.ModelElement.constraints.eType = modellingcore.AbstractConstraint
modellingcore.ModelElement.ownedConstraints.eType = modellingcore.AbstractConstraint
modellingcore.ModelElement.ownedMigratedElements.eType = modellingcore.ModelElement
modellingcore.InformationsExchanger.incomingInformationFlows.eType = modellingcore.AbstractInformationFlow
modellingcore.InformationsExchanger.outgoingInformationFlows.eType = modellingcore.AbstractInformationFlow
modellingcore.InformationsExchanger.informationFlows.eType = modellingcore.AbstractInformationFlow
modellingcore.TraceableElement.incomingTraces.eType = modellingcore.AbstractTrace
modellingcore.TraceableElement.outgoingTraces.eType = modellingcore.AbstractTrace
modellingcore.AbstractType.abstractTypedElements.eType = modellingcore.AbstractTypedElement
modellingcore.AbstractTypedElement.abstractType.eType = modellingcore.AbstractType
modellingcore.AbstractTrace.targetElement.eType = modellingcore.TraceableElement
modellingcore.AbstractTrace.sourceElement.eType = modellingcore.TraceableElement
modellingcore.AbstractConstraint.constrainedElements.eType = modellingcore.ModelElement
modellingcore.AbstractConstraint.ownedSpecification.eType = modellingcore.ValueSpecification
modellingcore.AbstractConstraint._context.eType = modellingcore.ModelElement
modellingcore.AbstractParameter.rate.eType = modellingcore.ValueSpecification
modellingcore.AbstractParameter.probability.eType = modellingcore.ValueSpecification
modellingcore.AbstractParameterSet.ownedConditions.eType = modellingcore.AbstractConstraint
modellingcore.AbstractParameterSet.probability.eType = modellingcore.ValueSpecification
modellingcore.AbstractInformationFlow.convoyedInformations.eType = modellingcore.AbstractExchangeItem
modellingcore.AbstractInformationFlow.source.eType = modellingcore.InformationsExchanger
modellingcore.AbstractInformationFlow.target.eType = modellingcore.InformationsExchanger
modellingcore.IState.referencedStates.eType = modellingcore.IState
modellingcore.IState.exploitedStates.eType = modellingcore.IState
modellingcore.AbstractRelationship.realizedFlow.eType = modellingcore.AbstractInformationFlow
modellingcore.AbstractParameter.parameterSet.eType = modellingcore.AbstractParameterSet
modellingcore.AbstractParameterSet.parameters.eType = modellingcore.AbstractParameter
modellingcore.AbstractParameterSet.parameters.eOpposite = modellingcore.AbstractParameter.parameterSet
modellingcore.AbstractInformationFlow.realizations.eType = modellingcore.AbstractRelationship
modellingcore.AbstractInformationFlow.realizations.eOpposite = modellingcore.AbstractRelationship.realizedFlow

#print('modellingcore.cross_init done')

#print('activity.cross_init starting')


activity.AbstractActivity.ownedNodes.eType = activity.ActivityNode
activity.AbstractActivity.ownedEdges.eType = activity.ActivityEdge
activity.AbstractActivity.ownedGroups.eType = activity.ActivityGroup
activity.AbstractActivity.ownedStructuredNodes.eType = activity.StructuredActivityNode
activity.ExceptionHandler.handlerBody.eType = activity.ExecutableNode
activity.ExceptionHandler.exceptionInput.eType = activity.ObjectNode
activity.ExceptionHandler.exceptionTypes.eType = modellingcore.AbstractType
activity.ActivityGroup.ownedNodes.eType = activity.ActivityNode
activity.ActivityGroup.ownedEdges.eType = activity.ActivityEdge
activity.ActivityEdge._inActivityPartition.eType = activity.ActivityPartition
activity.ActivityEdge._inInterruptibleRegion.eType = activity.InterruptibleActivityRegion
activity.ActivityEdge._inStructuredNode.eType = activity.StructuredActivityNode
activity.ActivityEdge.rate.eType = modellingcore.ValueSpecification
activity.ActivityEdge.probability.eType = modellingcore.ValueSpecification
activity.ActivityEdge.target.eType = activity.ActivityNode
activity.ActivityEdge.source.eType = activity.ActivityNode
activity.ActivityEdge.guard.eType = modellingcore.ValueSpecification
activity.ActivityEdge.weight.eType = modellingcore.ValueSpecification
activity.ObjectFlow.transformation.eType = behavior.AbstractBehavior
activity.ObjectFlow.selection.eType = behavior.AbstractBehavior
activity.ActivityPartition.representedElement.eType = modellingcore.AbstractType
activity.ActivityPartition._superPartition.eType = activity.ActivityPartition
activity.ActivityPartition.subPartitions.eType = activity.ActivityPartition
activity.ActivityExchange.realizingActivityFlows.eType = activity.ActivityEdge
activity.ActivityNode._inActivityPartition.eType = activity.ActivityPartition
activity.ActivityNode._inInterruptibleRegion.eType = activity.InterruptibleActivityRegion
activity.ActivityNode._inStructuredNode.eType = activity.InterruptibleActivityRegion
activity.ActivityNode.outgoing.eType = activity.ActivityEdge
activity.ActivityNode.incoming.eType = activity.ActivityEdge
activity.AbstractAction.localPrecondition.eType = modellingcore.AbstractConstraint
activity.AbstractAction.localPostcondition.eType = modellingcore.AbstractConstraint
activity.AbstractAction.context.eType = modellingcore.AbstractType
activity.AbstractAction.inputs.eType = activity.InputPin
activity.AbstractAction.outputs.eType = activity.OutputPin
activity.AcceptEventAction.result.eType = activity.OutputPin
activity.InvocationAction.arguments.eType = activity.InputPin
activity.SendSignalAction.target.eType = activity.InputPin
activity.SendSignalAction.signal.eType = behavior.AbstractSignal
activity.CallAction.results.eType = activity.OutputPin
activity.CallBehaviorAction.behavior.eType = behavior.AbstractBehavior
activity.ObjectNode.upperBound.eType = modellingcore.ValueSpecification
activity.ObjectNode.inState.eType = modellingcore.IState
activity.ObjectNode.selection.eType = behavior.AbstractBehavior
activity.InputPin.inputEvaluationAction.eType = activity.AbstractAction
activity.ValuePin.value.eType = modellingcore.ValueSpecification
activity.ExceptionHandler.protectedNode.eType = activity.ExecutableNode
activity.ActivityGroup.superGroup.eType = activity.ActivityGroup
activity.ActivityGroup.subGroups.eType = activity.ActivityGroup
activity.ActivityGroup.subGroups.eOpposite = activity.ActivityGroup.superGroup
activity.InterruptibleActivityRegion.interruptingEdges.eType = activity.ActivityEdge
activity.ActivityEdge.interrupts.eType = activity.InterruptibleActivityRegion
activity.ActivityEdge.interrupts.eOpposite = activity.InterruptibleActivityRegion.interruptingEdges
activity.ExecutableNode.ownedHandlers.eType = activity.ExceptionHandler
activity.ExecutableNode.ownedHandlers.eOpposite = activity.ExceptionHandler.protectedNode

#print('activity.cross_init done')

#print('capellacommon.cross_init starting')


capellacommon.GenericTrace.keyValuePairs.eType = capellacore.KeyValue
capellacommon.GenericTrace._source.eType = modellingcore.TraceableElement
capellacommon.GenericTrace._target.eType = modellingcore.TraceableElement
capellacommon.CapabilityRealizationInvolvement._involvedCapabilityRealizationInvolvedElement.eType = capellacommon.CapabilityRealizationInvolvedElement
capellacommon.CapabilityRealizationInvolvedElement.capabilityRealizationInvolvements.eType = capellacommon.CapabilityRealizationInvolvement
capellacommon.CapabilityRealizationInvolvedElement.involvingCapabilityRealizations.eType = la.CapabilityRealization
capellacommon.StateMachine.ownedRegions.eType = capellacommon.Region
capellacommon.StateMachine.ownedConnectionPoints.eType = capellacommon.Pseudostate
capellacommon.Region.ownedStates.eType = capellacommon.AbstractState
capellacommon.Region.ownedTransitions.eType = capellacommon.StateTransition
capellacommon.Region.involvedStates.eType = capellacommon.AbstractState
capellacommon.State.ownedRegions.eType = capellacommon.Region
capellacommon.State.ownedConnectionPoints.eType = capellacommon.Pseudostate
capellacommon.State.availableAbstractFunctions.eType = fa.AbstractFunction
capellacommon.State.availableFunctionalChains.eType = fa.FunctionalChain
capellacommon.State.availableAbstractCapabilities.eType = interaction.AbstractCapability
capellacommon.State.entry.eType = behavior.AbstractEvent
capellacommon.State.doActivity.eType = behavior.AbstractEvent
capellacommon.State.exit.eType = behavior.AbstractEvent
capellacommon.State.stateInvariant.eType = modellingcore.AbstractConstraint
capellacommon.AbstractState.ownedAbstractStateRealizations.eType = capellacommon.AbstractStateRealization
capellacommon.AbstractState.realizedAbstractStates.eType = capellacommon.AbstractState
capellacommon.AbstractState.realizingAbstractStates.eType = capellacommon.AbstractState
capellacommon.AbstractState.outgoing.eType = capellacommon.StateTransition
capellacommon.AbstractState.incoming.eType = capellacommon.StateTransition
capellacommon.AbstractState.involverRegions.eType = capellacommon.Region
capellacommon.StateTransition.guard.eType = capellacore.Constraint
capellacommon.StateTransition.source.eType = capellacommon.AbstractState
capellacommon.StateTransition.target.eType = capellacommon.AbstractState
capellacommon.StateTransition.effect.eType = behavior.AbstractEvent
capellacommon.StateTransition.triggers.eType = behavior.AbstractEvent
capellacommon.StateTransition.ownedStateTransitionRealizations.eType = capellacommon.StateTransitionRealization
capellacommon.StateTransition.realizedStateTransitions.eType = capellacommon.StateTransition
capellacommon.StateTransition.realizingStateTransitions.eType = capellacommon.StateTransition
capellacommon.AbstractStateRealization._realizedAbstractState.eType = capellacommon.AbstractState
capellacommon.AbstractStateRealization._realizingAbstractState.eType = capellacommon.AbstractState
capellacommon.StateTransitionRealization._realizedStateTransition.eType = capellacommon.StateTransition
capellacommon.StateTransitionRealization._realizingStateTransition.eType = capellacommon.StateTransition
capellacommon.StateEventRealization._realizedEvent.eType = capellacommon.StateEvent
capellacommon.StateEventRealization._realizingEvent.eType = capellacommon.StateEvent
capellacommon.StateEvent.expression.eType = capellacore.Constraint
capellacommon.StateEvent.ownedStateEventRealizations.eType = capellacommon.StateEventRealization

#print('capellacommon.cross_init done')

#print('capellacore.cross_init starting')


capellacore.CapellaElement.ownedPropertyValues.eType = capellacore.AbstractPropertyValue
capellacore.CapellaElement.ownedEnumerationPropertyTypes.eType = capellacore.EnumerationPropertyType
capellacore.CapellaElement.appliedPropertyValues.eType = capellacore.AbstractPropertyValue
capellacore.CapellaElement.ownedPropertyValueGroups.eType = capellacore.PropertyValueGroup
capellacore.CapellaElement.appliedPropertyValueGroups.eType = capellacore.PropertyValueGroup
capellacore.CapellaElement.status.eType = capellacore.EnumerationPropertyLiteral
capellacore.CapellaElement.features.eType = capellacore.EnumerationPropertyLiteral
capellacore.CapellaElement.appliedRequirements.eType = requirement.Requirement
capellacore.Namespace.ownedTraces.eType = capellacore.Trace
capellacore.Namespace.containedGenericTraces.eType = capellacommon.GenericTrace
capellacore.Namespace.containedRequirementsTraces.eType = requirement.RequirementsTrace
capellacore.Namespace.namingRules.eType = capellacore.NamingRule
capellacore.NamedRelationship.namingRules.eType = capellacore.NamingRule
capellacore.Structure.ownedPropertyValuePkgs.eType = capellacore.PropertyValuePkg
capellacore.AbstractModellingStructure.ownedArchitectures.eType = capellacore.ModellingArchitecture
capellacore.AbstractModellingStructure.ownedArchitecturePkgs.eType = capellacore.ModellingArchitecturePkg
capellacore.Type.typedElements.eType = capellacore.TypedElement
capellacore.TypedElement._type.eType = capellacore.Type
capellacore.ReuseLink.reused.eType = capellacore.ReuseableStructure
capellacore.ReuseLink.reuser.eType = capellacore.ReuserStructure
capellacore.ReuseableStructure.reuseLinks.eType = capellacore.ReuseLink
capellacore.ReuserStructure.reuseLinks.eType = capellacore.ReuseLink
capellacore.ReuserStructure.ownedReuseLinks.eType = capellacore.ReuseLink
capellacore.GeneralizableElement.ownedGeneralizations.eType = capellacore.Generalization
capellacore.GeneralizableElement.superGeneralizations.eType = capellacore.Generalization
capellacore.GeneralizableElement.subGeneralizations.eType = capellacore.Generalization
capellacore.Classifier.ownedFeatures.eType = capellacore.Feature
capellacore.Classifier.containedProperties.eType = information.Property
capellacore.GeneralClass.containedOperations.eType = information.Operation
capellacore.GeneralClass.nestedGeneralClasses.eType = capellacore.GeneralClass
capellacore.Generalization.super_.eType = capellacore.GeneralizableElement
capellacore.Generalization.sub.eType = capellacore.GeneralizableElement
capellacore.AbstractExchangeItemPkg.ownedExchangeItems.eType = information.ExchangeItem
capellacore.Involvement._involver.eType = capellacore.InvolverElement
capellacore.Involvement.involved.eType = capellacore.InvolvedElement
capellacore.InvolverElement.involvedInvolvements.eType = capellacore.Involvement
capellacore.InvolvedElement.involvingInvolvements.eType = capellacore.Involvement
capellacore.AbstractPropertyValue.involvedElements.eType = capellacore.CapellaElement
capellacore.AbstractPropertyValue.valuedElements.eType = capellacore.CapellaElement
capellacore.EnumerationPropertyValue.type.eType = capellacore.EnumerationPropertyType
capellacore.EnumerationPropertyValue.value.eType = capellacore.EnumerationPropertyLiteral
capellacore.EnumerationPropertyType.ownedLiterals.eType = capellacore.EnumerationPropertyLiteral
capellacore.PropertyValueGroup.valuedElements.eType = capellacore.CapellaElement
capellacore.GeneralizableElement.super_.eType = capellacore.GeneralizableElement
capellacore.GeneralizableElement.sub.eType = capellacore.GeneralizableElement
capellacore.GeneralizableElement.sub.eOpposite = capellacore.GeneralizableElement.super_

#print('capellacore.cross_init done')

#print('capellamodeller.cross_init starting')


capellamodeller.Project.keyValuePairs.eType = capellacore.KeyValue
capellamodeller.Project.ownedFolders.eType = capellamodeller.Folder
capellamodeller.Project.ownedModelRoots.eType = capellamodeller.ModelRoot
capellamodeller.Folder.ownedFolders.eType = capellamodeller.Folder
capellamodeller.Folder.ownedModelRoots.eType = capellamodeller.ModelRoot
capellamodeller.SystemEngineering.containedOperationalAnalysis.eType = oa.OperationalAnalysis
capellamodeller.SystemEngineering.containedSystemAnalysis.eType = ctx.SystemAnalysis
capellamodeller.SystemEngineering.containedLogicalArchitectures.eType = la.LogicalArchitecture
capellamodeller.SystemEngineering.containedPhysicalArchitectures.eType = pa.PhysicalArchitecture
capellamodeller.SystemEngineering.containedEPBSArchitectures.eType = epbs.EPBSArchitecture
capellamodeller.SystemEngineering.containedSharedPkgs.eType = sharedmodel.SharedPkg
capellamodeller.SystemEngineeringPkg.ownedSystemEngineerings.eType = capellamodeller.SystemEngineering

#print('capellamodeller.cross_init done')

#print('cs.cross_init starting')


cs.BlockArchitecture.ownedRequirementPkgs.eType = requirement.RequirementsPkg
cs.BlockArchitecture.ownedAbstractCapabilityPkg.eType = capellacommon.AbstractCapabilityPkg
cs.BlockArchitecture.ownedInterfacePkg.eType = cs.InterfacePkg
cs.BlockArchitecture.ownedDataPkg.eType = information.DataPkg
cs.BlockArchitecture.allocatedArchitectures.eType = cs.BlockArchitecture
cs.BlockArchitecture.allocatingArchitectures.eType = cs.BlockArchitecture
cs.BlockArchitecture._system.eType = cs.Component
cs.Block.ownedAbstractCapabilityPkg.eType = capellacommon.AbstractCapabilityPkg
cs.Block.ownedInterfacePkg.eType = cs.InterfacePkg
cs.Block.ownedDataPkg.eType = information.DataPkg
cs.Block.ownedStateMachines.eType = capellacommon.StateMachine
cs.Component.ownedInterfaceUses.eType = cs.InterfaceUse
cs.Component.ownedInterfaceImplementations.eType = cs.InterfaceImplementation
cs.Component.ownedComponentRealizations.eType = cs.ComponentRealization
cs.Component.realizedComponents.eType = cs.Component
cs.Component.realizingComponents.eType = cs.Component
cs.Component.providedInterfaces.eType = cs.Interface
cs.Component.requiredInterfaces.eType = cs.Interface
cs.Component.containedComponentPorts.eType = fa.ComponentPort
cs.Component.containedParts.eType = cs.Part
cs.Component.containedPhysicalPorts.eType = cs.PhysicalPort
cs.Component.ownedPhysicalPath.eType = cs.PhysicalPath
cs.Component.ownedPhysicalLinks.eType = cs.PhysicalLink
cs.Component.ownedPhysicalLinkCategories.eType = cs.PhysicalLinkCategory
cs.Component.representingParts.eType = cs.Part
cs.Part.providedInterfaces.eType = cs.Interface
cs.Part.requiredInterfaces.eType = cs.Interface
cs.Part.ownedDeploymentLinks.eType = cs.AbstractDeploymentLink
cs.Part.deployedParts.eType = cs.Part
cs.Part.deployingParts.eType = cs.Part
cs.Part.ownedAbstractType.eType = modellingcore.AbstractType
cs.ComponentRealization._realizedComponent.eType = cs.Component
cs.ComponentRealization._realizingComponent.eType = cs.Component
cs.InterfacePkg.ownedInterfaces.eType = cs.Interface
cs.InterfacePkg.ownedInterfacePkgs.eType = cs.InterfacePkg
cs.Interface.interfaceImplementations.eType = cs.InterfaceImplementation
cs.Interface.interfaceUses.eType = cs.InterfaceUse
cs.Interface.allocatingInterfaces.eType = cs.Interface
cs.Interface.allocatingComponents.eType = cs.Component
cs.Interface.exchangeItems.eType = information.ExchangeItem
cs.Interface.ownedExchangeItemAllocations.eType = cs.ExchangeItemAllocation
cs.Interface.requiringComponents.eType = cs.Component
cs.Interface.requiringComponentPorts.eType = fa.ComponentPort
cs.Interface.providingComponents.eType = cs.Component
cs.Interface.providingComponentPorts.eType = fa.ComponentPort
cs.Interface.realizingLogicalInterfaces.eType = cs.Interface
cs.Interface.realizedContextInterfaces.eType = cs.Interface
cs.Interface.realizingPhysicalInterfaces.eType = cs.Interface
cs.Interface.realizedLogicalInterfaces.eType = cs.Interface
cs.InterfaceImplementation.implementedInterface.eType = cs.Interface
cs.InterfaceUse.usedInterface.eType = cs.Interface
cs.ProvidedInterfaceLink.interface.eType = cs.Interface
cs.RequiredInterfaceLink.interface.eType = cs.Interface
cs.InterfaceAllocator.ownedInterfaceAllocations.eType = cs.InterfaceAllocation
cs.InterfaceAllocator.allocatedInterfaces.eType = cs.Interface
cs.ExchangeItemAllocation.allocatedItem.eType = information.ExchangeItem
cs.ExchangeItemAllocation._allocatingInterface.eType = cs.Interface
cs.DeployableElement.deployingLinks.eType = cs.AbstractDeploymentLink
cs.DeploymentTarget.deploymentLinks.eType = cs.AbstractDeploymentLink
cs.AbstractDeploymentLink.deployedElement.eType = cs.DeployableElement
cs.AbstractDeploymentLink.location.eType = cs.DeploymentTarget
cs.AbstractPhysicalLinkEnd.involvedLinks.eType = cs.PhysicalLink
cs.PhysicalLink.linkEnds.eType = cs.AbstractPhysicalLinkEnd
cs.PhysicalLink.ownedComponentExchangeFunctionalExchangeAllocations.eType = fa.ComponentExchangeFunctionalExchangeAllocation
cs.PhysicalLink.ownedPhysicalLinkEnds.eType = cs.PhysicalLinkEnd
cs.PhysicalLink.ownedPhysicalLinkRealizations.eType = cs.PhysicalLinkRealization
cs.PhysicalLink.categories.eType = cs.PhysicalLinkCategory
cs.PhysicalLink._sourcePhysicalPort.eType = cs.PhysicalPort
cs.PhysicalLink._targetPhysicalPort.eType = cs.PhysicalPort
cs.PhysicalLink.realizedPhysicalLinks.eType = cs.PhysicalLink
cs.PhysicalLink.realizingPhysicalLinks.eType = cs.PhysicalLink
cs.PhysicalLinkCategory.links.eType = cs.PhysicalLink
cs.PhysicalLinkEnd.port.eType = cs.PhysicalPort
cs.PhysicalLinkEnd.part.eType = cs.Part
cs.PhysicalPath.involvedLinks.eType = cs.AbstractPhysicalPathLink
cs.PhysicalPath.ownedPhysicalPathInvolvements.eType = cs.PhysicalPathInvolvement
cs.PhysicalPath.firstPhysicalPathInvolvements.eType = cs.PhysicalPathInvolvement
cs.PhysicalPath.ownedPhysicalPathRealizations.eType = cs.PhysicalPathRealization
cs.PhysicalPath.realizedPhysicalPaths.eType = cs.PhysicalPath
cs.PhysicalPath.realizingPhysicalPaths.eType = cs.PhysicalPath
cs.PhysicalPathInvolvement.nextInvolvements.eType = cs.PhysicalPathInvolvement
cs.PhysicalPathInvolvement.previousInvolvements.eType = cs.PhysicalPathInvolvement
cs.PhysicalPathInvolvement._involvedElement.eType = cs.AbstractPathInvolvedElement
cs.PhysicalPathInvolvement._involvedComponent.eType = cs.Component
cs.PhysicalPathReference._referencedPhysicalPath.eType = cs.PhysicalPath
cs.PhysicalPort.ownedComponentPortAllocations.eType = fa.ComponentPortAllocation
cs.PhysicalPort.ownedPhysicalPortRealizations.eType = cs.PhysicalPortRealization
cs.PhysicalPort.realizedPhysicalPorts.eType = cs.PhysicalPort
cs.PhysicalPort.realizingPhysicalPorts.eType = cs.PhysicalPort
cs.ComponentPkg.ownedParts.eType = cs.Part
cs.ComponentPkg.ownedComponentExchanges.eType = fa.ComponentExchange
cs.ComponentPkg.ownedComponentExchangeCategories.eType = fa.ComponentExchangeCategory
cs.ComponentPkg.ownedFunctionalLinks.eType = fa.ExchangeLink
cs.ComponentPkg.ownedFunctionalAllocations.eType = fa.ComponentFunctionalAllocation
cs.ComponentPkg.ownedComponentExchangeRealizations.eType = fa.ComponentExchangeRealization
cs.ComponentPkg.ownedPhysicalLinks.eType = cs.PhysicalLink
cs.ComponentPkg.ownedPhysicalLinkCategories.eType = cs.PhysicalLinkCategory
cs.ComponentPkg.ownedStateMachines.eType = capellacommon.StateMachine
cs.BlockArchitecture.provisionedArchitectureAllocations.eType = cs.ArchitectureAllocation
cs.BlockArchitecture.provisioningArchitectureAllocations.eType = cs.ArchitectureAllocation
cs.Component.usedInterfaceLinks.eType = cs.InterfaceUse
cs.Component.usedInterfaces.eType = cs.Interface
cs.Component.implementedInterfaceLinks.eType = cs.InterfaceImplementation
cs.Component.implementedInterfaces.eType = cs.Interface
cs.ArchitectureAllocation._allocatedArchitecture.eType = cs.BlockArchitecture
cs.ArchitectureAllocation._allocatedArchitecture.eOpposite = cs.BlockArchitecture.provisioningArchitectureAllocations
cs.ArchitectureAllocation._allocatingArchitecture.eType = cs.BlockArchitecture
cs.ArchitectureAllocation._allocatingArchitecture.eOpposite = cs.BlockArchitecture.provisionedArchitectureAllocations
cs.Interface.implementorComponents.eType = cs.Component
cs.Interface.implementorComponents.eOpposite = cs.Component.implementedInterfaces
cs.Interface.userComponents.eType = cs.Component
cs.Interface.userComponents.eOpposite = cs.Component.usedInterfaces
cs.Interface.provisioningInterfaceAllocations.eType = cs.InterfaceAllocation
cs.InterfaceImplementation._interfaceImplementor.eType = cs.Component
cs.InterfaceImplementation._interfaceImplementor.eOpposite = cs.Component.implementedInterfaceLinks
cs.InterfaceUse._interfaceUser.eType = cs.Component
cs.InterfaceUse._interfaceUser.eOpposite = cs.Component.usedInterfaceLinks
cs.InterfaceAllocation._allocatedInterface.eType = cs.Interface
cs.InterfaceAllocation._allocatedInterface.eOpposite = cs.Interface.provisioningInterfaceAllocations
cs.InterfaceAllocation._allocatingInterfaceAllocator.eType = cs.InterfaceAllocator
cs.InterfaceAllocator.provisionedInterfaceAllocations.eType = cs.InterfaceAllocation
cs.InterfaceAllocator.provisionedInterfaceAllocations.eOpposite = cs.InterfaceAllocation._allocatingInterfaceAllocator
cs.AbstractPhysicalArtifact.allocatorConfigurationItems.eType = epbs.ConfigurationItem
cs.PhysicalPort.allocatedComponentPorts.eType = fa.ComponentPort

#print('cs.cross_init done')

#print('ctx.cross_init starting')


ctx.SystemAnalysis.ownedSystemComponentPkg.eType = ctx.SystemComponentPkg
ctx.SystemAnalysis.ownedMissionPkg.eType = ctx.MissionPkg
ctx.SystemAnalysis._containedCapabilityPkg.eType = ctx.CapabilityPkg
ctx.SystemAnalysis._containedSystemFunctionPkg.eType = ctx.SystemFunctionPkg
ctx.SystemAnalysis.ownedOperationalAnalysisRealizations.eType = ctx.OperationalAnalysisRealization
ctx.SystemAnalysis.allocatedOperationalAnalysisRealizations.eType = ctx.OperationalAnalysisRealization
ctx.SystemFunction.ownedSystemFunctionPkgs.eType = ctx.SystemFunctionPkg
ctx.SystemFunction.allocatingSystemComponents.eType = ctx.SystemComponent
ctx.SystemFunction.containedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunction.childrenSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunctionPkg.ownedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunctionPkg.ownedSystemFunctionPkgs.eType = ctx.SystemFunctionPkg
ctx.SystemCommunicationHook.communication.eType = ctx.SystemCommunication
ctx.SystemCommunicationHook.type.eType = cs.Component
ctx.SystemCommunication.ends.eType = ctx.SystemCommunicationHook
ctx.CapabilityInvolvement._systemComponent.eType = ctx.SystemComponent
ctx.CapabilityInvolvement._capability.eType = ctx.Capability
ctx.MissionInvolvement._systemComponent.eType = ctx.SystemComponent
ctx.MissionInvolvement._mission.eType = ctx.Mission
ctx.Mission.ownedMissionInvolvements.eType = ctx.MissionInvolvement
ctx.Mission.involvedSystemComponents.eType = ctx.SystemComponent
ctx.Mission.ownedCapabilityExploitations.eType = ctx.CapabilityExploitation
ctx.MissionPkg.ownedMissionPkgs.eType = ctx.MissionPkg
ctx.MissionPkg.ownedMissions.eType = ctx.Mission
ctx.Capability.ownedCapabilityInvolvements.eType = ctx.CapabilityInvolvement
ctx.Capability.involvedSystemComponents.eType = ctx.SystemComponent
ctx.Capability.purposes.eType = ctx.CapabilityExploitation
ctx.CapabilityExploitation._mission.eType = ctx.Mission
ctx.CapabilityExploitation.capability.eType = ctx.Capability
ctx.CapabilityPkg.ownedCapabilities.eType = ctx.Capability
ctx.CapabilityPkg.ownedCapabilityPkgs.eType = ctx.CapabilityPkg
ctx.SystemComponentPkg.ownedSystemComponents.eType = ctx.SystemComponent
ctx.SystemComponentPkg.ownedSystemComponentPkgs.eType = ctx.SystemComponentPkg
ctx.SystemComponent.ownedSystemComponents.eType = ctx.SystemComponent
ctx.SystemComponent.ownedSystemComponentPkgs.eType = ctx.SystemComponentPkg
ctx.SystemComponent.dataType.eType = capellacore.Classifier
ctx.SystemComponent.involvingCapabilities.eType = ctx.Capability
ctx.SystemComponent.capabilityInvolvements.eType = ctx.CapabilityInvolvement
ctx.SystemComponent.involvingMissions.eType = ctx.Mission
ctx.SystemComponent.missionInvolvements.eType = ctx.MissionInvolvement
ctx.SystemComponent.realizedEntities.eType = oa.Entity
ctx.SystemComponent.realizingLogicalComponents.eType = la.LogicalComponent
ctx.SystemComponent.allocatedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemAnalysis.allocatedOperationalAnalyses.eType = oa.OperationalAnalysis
ctx.SystemAnalysis.allocatingLogicalArchitectures.eType = la.LogicalArchitecture
ctx.SystemFunction.realizedOperationalActivities.eType = oa.OperationalActivity
ctx.SystemFunction.realizingLogicalFunctions.eType = la.LogicalFunction
ctx.Mission.exploitedCapabilities.eType = ctx.Capability
ctx.Capability.purposeMissions.eType = ctx.Mission
ctx.Capability.purposeMissions.eOpposite = ctx.Mission.exploitedCapabilities
ctx.Capability.realizedOperationalCapabilities.eType = oa.OperationalCapability
ctx.Capability.realizingCapabilityRealizations.eType = la.CapabilityRealization

#print('ctx.cross_init done')

#print('epbs.cross_init starting')


epbs.EPBSArchitecturePkg.ownedEPBSArchitectures.eType = epbs.EPBSArchitecture
epbs.EPBSArchitecture.ownedConfigurationItemPkg.eType = epbs.ConfigurationItemPkg
epbs.EPBSArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
epbs.EPBSArchitecture.ownedPhysicalArchitectureRealizations.eType = epbs.PhysicalArchitectureRealization
epbs.EPBSArchitecture.allocatedPhysicalArchitectureRealizations.eType = epbs.PhysicalArchitectureRealization
epbs.ConfigurationItemPkg.ownedConfigurationItems.eType = epbs.ConfigurationItem
epbs.ConfigurationItemPkg.ownedConfigurationItemPkgs.eType = epbs.ConfigurationItemPkg
epbs.ConfigurationItem.ownedConfigurationItems.eType = epbs.ConfigurationItem
epbs.ConfigurationItem.ownedConfigurationItemPkgs.eType = epbs.ConfigurationItemPkg
epbs.ConfigurationItem.ownedPhysicalArtifactRealizations.eType = epbs.PhysicalArtifactRealization
epbs.PhysicalArtifactRealization._realizedPhysicalArtifact.eType = cs.AbstractPhysicalArtifact
epbs.PhysicalArtifactRealization._realizingConfigurationItem.eType = epbs.ConfigurationItem
epbs.EPBSArchitecture.allocatedPhysicalArchitectures.eType = pa.PhysicalArchitecture
epbs.ConfigurationItem.allocatedPhysicalArtifacts.eType = cs.AbstractPhysicalArtifact

#print('epbs.cross_init done')

#print('fa.cross_init starting')


fa.AbstractFunctionalArchitecture.ownedFunctionPkg.eType = fa.FunctionPkg
fa.AbstractFunctionalArchitecture.ownedComponentExchanges.eType = fa.ComponentExchange
fa.AbstractFunctionalArchitecture.ownedComponentExchangeCategories.eType = fa.ComponentExchangeCategory
fa.AbstractFunctionalArchitecture.ownedFunctionalLinks.eType = fa.ExchangeLink
fa.AbstractFunctionalArchitecture.ownedFunctionalAllocations.eType = fa.ComponentFunctionalAllocation
fa.AbstractFunctionalArchitecture.ownedComponentExchangeRealizations.eType = fa.ComponentExchangeRealization
fa.AbstractFunctionalBlock.ownedFunctionalAllocation.eType = fa.ComponentFunctionalAllocation
fa.AbstractFunctionalBlock.ownedComponentExchanges.eType = fa.ComponentExchange
fa.AbstractFunctionalBlock.ownedComponentExchangeCategories.eType = fa.ComponentExchangeCategory
fa.AbstractFunctionalBlock.inExchangeLinks.eType = fa.ExchangeLink
fa.AbstractFunctionalBlock.outExchangeLinks.eType = fa.ExchangeLink
fa.FunctionPkg.ownedFunctionalLinks.eType = fa.ExchangeLink
fa.FunctionPkg.ownedExchanges.eType = fa.FunctionalExchangeSpecification
fa.FunctionPkg.ownedExchangeSpecificationRealizations.eType = fa.ExchangeSpecificationRealization
fa.FunctionPkg.ownedCategories.eType = fa.ExchangeCategory
fa.FunctionPkg.ownedFunctionSpecifications.eType = fa.FunctionSpecification
fa.FunctionSpecification.inExchangeLinks.eType = fa.ExchangeLink
fa.FunctionSpecification.outExchangeLinks.eType = fa.ExchangeLink
fa.FunctionSpecification.ownedFunctionPorts.eType = fa.FunctionPort
fa.FunctionSpecification.subFunctionSpecifications.eType = fa.FunctionSpecification
fa.ExchangeCategory.exchanges.eType = fa.FunctionalExchange
fa.ExchangeLink.exchanges.eType = fa.ExchangeSpecification
fa.ExchangeLink.ownedExchangeContainments.eType = fa.ExchangeContainment
fa.ExchangeLink.sources.eType = fa.FunctionSpecification
fa.ExchangeLink.destinations.eType = fa.FunctionSpecification
fa.ExchangeSpecification._containingLink.eType = fa.ExchangeLink
fa.FunctionalExchangeSpecification.functionalExchanges.eType = fa.FunctionalExchange
fa.FunctionalChain.ownedFunctionalChainInvolvements.eType = fa.FunctionalChainInvolvement
fa.FunctionalChain.ownedFunctionalChainRealizations.eType = fa.FunctionalChainRealization
fa.FunctionalChain.involvedFunctionalChainInvolvements.eType = fa.FunctionalChainInvolvement
fa.FunctionalChain.involvedElements.eType = capellacore.InvolvedElement
fa.FunctionalChain.enactedFunctions.eType = fa.AbstractFunction
fa.FunctionalChain.enactedFunctionalBlocks.eType = fa.AbstractFunctionalBlock
fa.FunctionalChain.availableInStates.eType = capellacommon.State
fa.FunctionalChain.firstFunctionalChainInvolvements.eType = fa.FunctionalChainInvolvement
fa.FunctionalChain.involvingCapabilities.eType = ctx.Capability
fa.FunctionalChain.involvingCapabilityRealizations.eType = la.CapabilityRealization
fa.FunctionalChain.realizedFunctionalChains.eType = fa.FunctionalChain
fa.FunctionalChain.realizingFunctionalChains.eType = fa.FunctionalChain
fa.FunctionalChain.preCondition.eType = capellacore.Constraint
fa.FunctionalChain.postCondition.eType = capellacore.Constraint
fa.FunctionalChain.ownedSequenceNodes.eType = fa.ControlNode
fa.FunctionalChain.ownedSequenceLinks.eType = fa.SequenceLink
fa.AbstractFunctionalChainContainer.ownedFunctionalChains.eType = fa.FunctionalChain
fa.FunctionalChainInvolvement.nextFunctionalChainInvolvements.eType = fa.FunctionalChainInvolvement
fa.FunctionalChainInvolvement.previousFunctionalChainInvolvements.eType = fa.FunctionalChainInvolvement
fa.FunctionalChainInvolvement._involvedElement.eType = capellacore.InvolvedElement
fa.FunctionalChainReference._referencedFunctionalChain.eType = fa.FunctionalChain
fa.FunctionInputPort.incomingExchangeItems.eType = information.ExchangeItem
fa.FunctionInputPort.incomingFunctionalExchanges.eType = fa.FunctionalExchange
fa.FunctionOutputPort.outgoingExchangeItems.eType = information.ExchangeItem
fa.FunctionOutputPort.outgoingFunctionalExchanges.eType = fa.FunctionalExchange
fa.FunctionalExchange.exchangeSpecifications.eType = fa.FunctionalExchangeSpecification
fa.FunctionalExchange.exchangedItems.eType = information.ExchangeItem
fa.FunctionalExchange.categories.eType = fa.ExchangeCategory
fa.FunctionalExchange.ownedFunctionalExchangeRealizations.eType = fa.FunctionalExchangeRealization
fa.FunctionalExchange._sourceFunctionOutputPort.eType = fa.FunctionOutputPort
fa.FunctionalExchange._targetFunctionInputPort.eType = fa.FunctionInputPort
fa.AbstractFunction.ownedFunctions.eType = fa.AbstractFunction
fa.AbstractFunction.ownedFunctionRealizations.eType = fa.FunctionRealization
fa.AbstractFunction.ownedFunctionalExchanges.eType = fa.FunctionalExchange
fa.AbstractFunction.subFunctions.eType = fa.AbstractFunction
fa.AbstractFunction.availableInStates.eType = capellacommon.State
fa.AbstractFunction.involvingCapabilities.eType = ctx.Capability
fa.AbstractFunction.involvingCapabilityRealizations.eType = la.CapabilityRealization
fa.AbstractFunction._linkedStateMachine.eType = capellacommon.StateMachine
fa.AbstractFunction._linkedFunctionSpecification.eType = fa.FunctionSpecification
fa.FunctionPort.representedComponentPort.eType = fa.ComponentPort
fa.FunctionPort.realizedFunctionPorts.eType = fa.FunctionPort
fa.FunctionPort.realizingFunctionPorts.eType = fa.FunctionPort
fa.ComponentExchange.ownedComponentExchangeFunctionalExchangeAllocations.eType = fa.ComponentExchangeFunctionalExchangeAllocation
fa.ComponentExchange.ownedComponentExchangeRealizations.eType = fa.ComponentExchangeRealization
fa.ComponentExchange.ownedComponentExchangeEnds.eType = fa.ComponentExchangeEnd
fa.ComponentExchange._sourcePort.eType = information.Port
fa.ComponentExchange._sourcePart.eType = cs.Part
fa.ComponentExchange._targetPort.eType = information.Port
fa.ComponentExchange._targetPart.eType = cs.Part
fa.ComponentExchange.categories.eType = fa.ComponentExchangeCategory
fa.ComponentExchange.allocatorPhysicalLinks.eType = cs.PhysicalLink
fa.ComponentExchangeAllocation._componentExchangeAllocated.eType = fa.ComponentExchange
fa.ComponentExchangeAllocation._componentExchangeAllocator.eType = fa.ComponentExchangeAllocator
fa.ComponentExchangeAllocator.ownedComponentExchangeAllocations.eType = fa.ComponentExchangeAllocation
fa.ComponentExchangeAllocator.allocatedComponentExchanges.eType = fa.ComponentExchange
fa.ComponentExchangeCategory.exchanges.eType = fa.ComponentExchange
fa.ComponentExchangeEnd.port.eType = information.Port
fa.ComponentExchangeEnd.part.eType = cs.Part
fa.ComponentPort.componentExchanges.eType = fa.ComponentExchange
fa.ComponentPortAllocation.ownedComponentPortAllocationEnds.eType = fa.ComponentPortAllocationEnd
fa.ComponentPortAllocation._allocatedPort.eType = information.Port
fa.ComponentPortAllocation._allocatingPort.eType = information.Port
fa.ComponentPortAllocationEnd.port.eType = information.Port
fa.ComponentPortAllocationEnd.part.eType = cs.Part
fa.ComponentPortAllocationEnd._owningComponentPortAllocation.eType = fa.ComponentPortAllocation
fa.FunctionalChainInvolvementLink.exchangeContext.eType = capellacore.Constraint
fa.FunctionalChainInvolvementLink.exchangedItems.eType = information.ExchangeItem
fa.FunctionalChainInvolvementLink.source.eType = fa.FunctionalChainInvolvementFunction
fa.FunctionalChainInvolvementLink.target.eType = fa.FunctionalChainInvolvementFunction
fa.SequenceLink.condition.eType = capellacore.Constraint
fa.SequenceLink.links.eType = fa.FunctionalChainInvolvementLink
fa.SequenceLink.source.eType = fa.SequenceLinkEnd
fa.SequenceLink.target.eType = fa.SequenceLinkEnd
fa.FunctionalChainInvolvementFunction.outgoingInvolvementLinks.eType = fa.FunctionalChainInvolvementLink
fa.FunctionalChainInvolvementFunction.incomingInvolvementLinks.eType = fa.FunctionalChainInvolvementLink
fa.ReferenceHierarchyContext.sourceReferenceHierarchy.eType = fa.FunctionalChainReference
fa.ReferenceHierarchyContext.targetReferenceHierarchy.eType = fa.FunctionalChainReference
fa.AbstractFunctionalBlock.functionalAllocations.eType = fa.ComponentFunctionalAllocation
fa.AbstractFunctionalBlock.allocatedFunctions.eType = fa.AbstractFunction
fa.ExchangeLink.exchangeContainmentLinks.eType = fa.ExchangeContainment
fa.ExchangeContainment.exchange.eType = fa.ExchangeSpecification
fa.ExchangeContainment.link.eType = fa.ExchangeLink
fa.ExchangeContainment.link.eOpposite = fa.ExchangeLink.exchangeContainmentLinks
fa.ExchangeSpecification.link.eType = fa.ExchangeContainment
fa.ExchangeSpecification.link.eOpposite = fa.ExchangeContainment.exchange
fa.ExchangeSpecification.outgoingExchangeSpecificationRealizations.eType = fa.ExchangeSpecificationRealization
fa.ExchangeSpecification.incomingExchangeSpecificationRealizations.eType = fa.ExchangeSpecificationRealization
fa.FunctionalChain.involvedFunctions.eType = fa.AbstractFunction
fa.FunctionalChain.involvedFunctionalExchanges.eType = fa.FunctionalExchange
fa.ComponentFunctionalAllocation._function.eType = fa.AbstractFunction
fa.ComponentFunctionalAllocation._block.eType = fa.AbstractFunctionalBlock
fa.ComponentFunctionalAllocation._block.eOpposite = fa.AbstractFunctionalBlock.functionalAllocations
fa.ExchangeSpecificationRealization._realizedExchangeSpecification.eType = fa.ExchangeSpecification
fa.ExchangeSpecificationRealization._realizedExchangeSpecification.eOpposite = fa.ExchangeSpecification.incomingExchangeSpecificationRealizations
fa.ExchangeSpecificationRealization._realizingExchangeSpecification.eType = fa.ExchangeSpecification
fa.ExchangeSpecificationRealization._realizingExchangeSpecification.eOpposite = fa.ExchangeSpecification.outgoingExchangeSpecificationRealizations
fa.FunctionalExchangeRealization._realizedFunctionalExchange.eType = fa.FunctionalExchange
fa.FunctionalExchangeRealization._realizingFunctionalExchange.eType = fa.FunctionalExchange
fa.FunctionRealization._allocatedFunction.eType = fa.AbstractFunction
fa.FunctionRealization._allocatingFunction.eType = fa.AbstractFunction
fa.FunctionalExchange.involvingFunctionalChains.eType = fa.FunctionalChain
fa.FunctionalExchange.involvingFunctionalChains.eOpposite = fa.FunctionalChain.involvedFunctionalExchanges
fa.FunctionalExchange.allocatingComponentExchanges.eType = fa.ComponentExchange
fa.FunctionalExchange.incomingComponentExchangeFunctionalExchangeRealizations.eType = fa.ComponentExchangeFunctionalExchangeAllocation
fa.FunctionalExchange.incomingFunctionalExchangeRealizations.eType = fa.FunctionalExchangeRealization
fa.FunctionalExchange.incomingFunctionalExchangeRealizations.eOpposite = fa.FunctionalExchangeRealization._realizedFunctionalExchange
fa.FunctionalExchange.outgoingFunctionalExchangeRealizations.eType = fa.FunctionalExchangeRealization
fa.FunctionalExchange.outgoingFunctionalExchangeRealizations.eOpposite = fa.FunctionalExchangeRealization._realizingFunctionalExchange
fa.FunctionalExchange.realizedFunctionalExchanges.eType = fa.FunctionalExchange
fa.FunctionalExchange.realizingFunctionalExchanges.eType = fa.FunctionalExchange
fa.FunctionalExchange.realizingFunctionalExchanges.eOpposite = fa.FunctionalExchange.realizedFunctionalExchanges
fa.AbstractFunction.outFunctionRealizations.eType = fa.FunctionRealization
fa.AbstractFunction.outFunctionRealizations.eOpposite = fa.FunctionRealization._allocatingFunction
fa.AbstractFunction.inFunctionRealizations.eType = fa.FunctionRealization
fa.AbstractFunction.inFunctionRealizations.eOpposite = fa.FunctionRealization._allocatedFunction
fa.AbstractFunction.componentFunctionalAllocations.eType = fa.ComponentFunctionalAllocation
fa.AbstractFunction.componentFunctionalAllocations.eOpposite = fa.ComponentFunctionalAllocation._function
fa.AbstractFunction.allocationBlocks.eType = fa.AbstractFunctionalBlock
fa.AbstractFunction.allocationBlocks.eOpposite = fa.AbstractFunctionalBlock.allocatedFunctions
fa.AbstractFunction.involvingFunctionalChains.eType = fa.FunctionalChain
fa.AbstractFunction.involvingFunctionalChains.eOpposite = fa.FunctionalChain.involvedFunctions
fa.FunctionPort.allocatorComponentPorts.eType = fa.ComponentPort
fa.ComponentExchange.allocatedFunctionalExchanges.eType = fa.FunctionalExchange
fa.ComponentExchange.allocatedFunctionalExchanges.eOpposite = fa.FunctionalExchange.allocatingComponentExchanges
fa.ComponentExchange.incomingComponentExchangeRealizations.eType = fa.ComponentExchangeRealization
fa.ComponentExchange.outgoingComponentExchangeRealizations.eType = fa.ComponentExchangeRealization
fa.ComponentExchange.outgoingComponentExchangeFunctionalExchangeAllocations.eType = fa.ComponentExchangeFunctionalExchangeAllocation
fa.ComponentExchange.realizedComponentExchanges.eType = fa.ComponentExchange
fa.ComponentExchange.realizingComponentExchanges.eType = fa.ComponentExchange
fa.ComponentExchange.realizingComponentExchanges.eOpposite = fa.ComponentExchange.realizedComponentExchanges
fa.ComponentExchangeFunctionalExchangeAllocation._allocatedFunctionalExchange.eType = fa.FunctionalExchange
fa.ComponentExchangeFunctionalExchangeAllocation._allocatedFunctionalExchange.eOpposite = fa.FunctionalExchange.incomingComponentExchangeFunctionalExchangeRealizations
fa.ComponentExchangeFunctionalExchangeAllocation._allocatingComponentExchange.eType = fa.ComponentExchange
fa.ComponentExchangeFunctionalExchangeAllocation._allocatingComponentExchange.eOpposite = fa.ComponentExchange.outgoingComponentExchangeFunctionalExchangeAllocations
fa.ComponentExchangeRealization._allocatedComponentExchange.eType = fa.ComponentExchange
fa.ComponentExchangeRealization._allocatedComponentExchange.eOpposite = fa.ComponentExchange.incomingComponentExchangeRealizations
fa.ComponentExchangeRealization._allocatingComponentExchange.eType = fa.ComponentExchange
fa.ComponentExchangeRealization._allocatingComponentExchange.eOpposite = fa.ComponentExchange.outgoingComponentExchangeRealizations
fa.ComponentPort.allocatedFunctionPorts.eType = fa.FunctionPort
fa.ComponentPort.allocatedFunctionPorts.eOpposite = fa.FunctionPort.allocatorComponentPorts
fa.ComponentPort.delegatedComponentPorts.eType = fa.ComponentPort
fa.ComponentPort.delegatingComponentPorts.eType = fa.ComponentPort
fa.ComponentPort.delegatingComponentPorts.eOpposite = fa.ComponentPort.delegatedComponentPorts
fa.ComponentPort.allocatingPhysicalPorts.eType = cs.PhysicalPort
fa.ComponentPort.realizedComponentPorts.eType = fa.ComponentPort
fa.ComponentPort.realizingComponentPorts.eType = fa.ComponentPort
fa.ComponentPort.realizingComponentPorts.eOpposite = fa.ComponentPort.realizedComponentPorts

#print('fa.cross_init done')

#print('information.cross_init starting')


information.communication.CommunicationItem.ownedStateMachines.eType = capellacommon.StateMachine
information.communication.CommunicationItem.properties.eType = information.Property
information.communication.MessageReference.message.eType = information.communication.Message
information.communication.MessageReferencePkg.ownedMessageReferences.eType = information.communication.MessageReference
information.communication.Signal.signalInstances.eType = information.communication.SignalInstance
information.communication.CommunicationLink.exchangeItem.eType = information.ExchangeItem
information.communication.CommunicationLinkExchanger.ownedCommunicationLinks.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.produce.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.consume.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.send.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.receive.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.call.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.execute.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.write.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.access.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.acquire.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.transmit.eType = information.communication.CommunicationLink
information.datatype.DataType._defaultValue.eType = information.datavalue.DataValue
information.datatype.DataType._nullValue.eType = information.datavalue.DataValue
information.datatype.DataType.ownedInformationRealizations.eType = information.InformationRealization
information.datatype.BooleanType.ownedLiterals.eType = information.datavalue.LiteralBooleanValue
information.datatype.BooleanType.ownedDefaultValue.eType = information.datavalue.AbstractBooleanValue
information.datatype.Enumeration.ownedLiterals.eType = information.datavalue.EnumerationLiteral
information.datatype.Enumeration.ownedDefaultValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedNullValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedMinValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedMaxValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.domainType.eType = information.datatype.DataType
information.datatype.StringType.ownedDefaultValue.eType = information.datavalue.AbstractStringValue
information.datatype.StringType.ownedNullValue.eType = information.datavalue.AbstractStringValue
information.datatype.StringType.ownedMinLength.eType = information.datavalue.NumericValue
information.datatype.StringType.ownedMaxLength.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedDefaultValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedNullValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedMinValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedMaxValue.eType = information.datavalue.NumericValue
information.datatype.PhysicalQuantity.unit.eType = information.Unit
information.datavalue.DataValue._type.eType = capellacore.Type
information.datavalue.DataValueContainer.ownedDataValues.eType = information.datavalue.DataValue
information.datavalue.AbstractBooleanValue._booleanType.eType = information.datatype.BooleanType
information.datavalue.BooleanReference.referencedValue.eType = information.datavalue.AbstractBooleanValue
information.datavalue.BooleanReference.referencedProperty.eType = information.Property
information.datavalue.AbstractEnumerationValue._enumerationType.eType = information.datatype.Enumeration
information.datavalue.EnumerationLiteral.domainValue.eType = information.datavalue.DataValue
information.datavalue.EnumerationReference.referencedValue.eType = information.datavalue.AbstractEnumerationValue
information.datavalue.EnumerationReference.referencedProperty.eType = information.Property
information.datavalue.AbstractStringValue._stringType.eType = information.datatype.StringType
information.datavalue.StringReference.referencedValue.eType = information.datavalue.AbstractStringValue
information.datavalue.StringReference.referencedProperty.eType = information.Property
information.datavalue.NumericValue.unit.eType = information.Unit
information.datavalue.NumericValue._numericType.eType = information.datatype.NumericType
information.datavalue.NumericReference.referencedValue.eType = information.datavalue.NumericValue
information.datavalue.NumericReference.referencedProperty.eType = information.Property
information.datavalue.AbstractComplexValue._complexType.eType = capellacore.Classifier
information.datavalue.ComplexValue.ownedParts.eType = information.datavalue.ValuePart
information.datavalue.ComplexValueReference.referencedValue.eType = information.datavalue.AbstractComplexValue
information.datavalue.ComplexValueReference.referencedProperty.eType = information.Property
information.datavalue.ValuePart.referencedProperty.eType = information.Property
information.datavalue.ValuePart.ownedValue.eType = information.datavalue.DataValue
information.datavalue.AbstractExpressionValue._expressionType.eType = information.datatype.DataType
information.datavalue.BinaryExpression.ownedLeftOperand.eType = information.datavalue.DataValue
information.datavalue.BinaryExpression.ownedRightOperand.eType = information.datavalue.DataValue
information.datavalue.UnaryExpression.ownedOperand.eType = information.datavalue.DataValue
information.AbstractInstance.representingInstanceRoles.eType = interaction.InstanceRole
information.AssociationPkg.ownedAssociations.eType = information.Association
information.Association.ownedMembers.eType = information.Property
information.Association.navigableMembers.eType = information.Property
information.Class.keyParts.eType = information.KeyPart
information.Class.ownedStateMachines.eType = capellacommon.StateMachine
information.Class.ownedDataValues.eType = information.datavalue.DataValue
information.Class.ownedInformationRealizations.eType = information.InformationRealization
information.Collection.type.eType = capellacore.Type
information.Collection.index.eType = information.datatype.DataType
information.Collection.containedOperations.eType = information.Operation
information.CollectionValue.ownedElements.eType = information.datavalue.DataValue
information.CollectionValue.ownedDefaultElement.eType = information.datavalue.DataValue
information.CollectionValueReference.referencedValue.eType = information.AbstractCollectionValue
information.CollectionValueReference.referencedProperty.eType = information.Property
information.DataPkg.ownedDataPkgs.eType = information.DataPkg
information.DataPkg.ownedClasses.eType = information.Class
information.DataPkg.ownedKeyParts.eType = information.KeyPart
information.DataPkg.ownedCollections.eType = information.Collection
information.DataPkg.ownedUnits.eType = information.Unit
information.DataPkg.ownedDataTypes.eType = information.datatype.DataType
information.DataPkg.ownedSignals.eType = information.communication.Signal
information.DataPkg.ownedMessages.eType = information.communication.Message
information.DataPkg.ownedExceptions.eType = information.communication.Exception
information.DataPkg.ownedStateEvents.eType = capellacommon.StateEvent
information.KeyPart.property.eType = information.Property
information.MultiplicityElement.ownedDefaultValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMinValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMaxValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedNullValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMinCard.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMinLength.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMaxCard.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMaxLength.eType = information.datavalue.NumericValue
information.Operation.ownedParameters.eType = information.Parameter
information.Operation.ownedOperationAllocation.eType = information.OperationAllocation
information.Operation.ownedExchangeItemRealizations.eType = information.ExchangeItemRealization
information.OperationAllocation._allocatedOperation.eType = information.Operation
information.OperationAllocation._allocatingOperation.eType = information.Operation
information.Property._association.eType = information.Association
information.Service.thrownExceptions.eType = information.communication.Exception
information.Service.messages.eType = information.communication.Message
information.Service.messageReferences.eType = information.communication.MessageReference
information.Union.discriminant.eType = information.UnionProperty
information.Union.defaultProperty.eType = information.UnionProperty
information.Union.containedUnionProperties.eType = information.UnionProperty
information.UnionProperty.qualifier.eType = information.datavalue.DataValue
information.Port.ownedProtocols.eType = capellacommon.StateMachine
information.Port.providedInterfaces.eType = cs.Interface
information.Port.requiredInterfaces.eType = cs.Interface
information.Port.ownedPortRealizations.eType = information.PortRealization
information.Port.ownedPortAllocations.eType = information.PortAllocation
information.ExchangeItem.ownedElements.eType = information.ExchangeItemElement
information.ExchangeItem.ownedInformationRealizations.eType = information.InformationRealization
information.ExchangeItem.ownedExchangeItemInstances.eType = information.ExchangeItemInstance
information.ExchangeItem.allocatorInterfaces.eType = cs.Interface
information.ExchangeItemElement.referencedProperties.eType = information.Property
information.ExchangeItemRealization._realizedItem.eType = modellingcore.AbstractExchangeItem
information.ExchangeItemRealization._realizingOperation.eType = information.Operation
information.AbstractEventOperation.invokingSequenceMessages.eType = interaction.SequenceMessage
information.datatype.DataType.realizedDataTypes.eType = information.datatype.DataType
information.datatype.DataType.realizingDataTypes.eType = information.datatype.DataType
information.datatype.DataType.realizingDataTypes.eOpposite = information.datatype.DataType.realizedDataTypes
information.Class.realizedClasses.eType = information.Class
information.Class.realizingClasses.eType = information.Class
information.Class.realizingClasses.eOpposite = information.Class.realizedClasses
information.Operation.allocatingOperations.eType = information.Operation
information.Operation.allocatedOperations.eType = information.Operation
information.Operation.allocatedOperations.eOpposite = information.Operation.allocatingOperations
information.Operation.realizedExchangeItems.eType = information.ExchangeItem
information.Port.incomingPortRealizations.eType = information.PortRealization
information.Port.outgoingPortRealizations.eType = information.PortRealization
information.Port.incomingPortAllocations.eType = information.PortAllocation
information.Port.outgoingPortAllocations.eType = information.PortAllocation
information.PortRealization._realizedPort.eType = information.Port
information.PortRealization._realizedPort.eOpposite = information.Port.incomingPortRealizations
information.PortRealization._realizingPort.eType = information.Port
information.PortRealization._realizingPort.eOpposite = information.Port.outgoingPortRealizations
information.PortAllocation._allocatedPort.eType = information.Port
information.PortAllocation._allocatedPort.eOpposite = information.Port.incomingPortAllocations
information.PortAllocation._allocatingPort.eType = information.Port
information.PortAllocation._allocatingPort.eOpposite = information.Port.outgoingPortAllocations
information.ExchangeItem.realizedExchangeItems.eType = information.ExchangeItem
information.ExchangeItem.realizingExchangeItems.eType = information.ExchangeItem
information.ExchangeItem.realizingExchangeItems.eOpposite = information.ExchangeItem.realizedExchangeItems
information.ExchangeItem.realizingOperations.eType = information.Operation
information.ExchangeItem.realizingOperations.eOpposite = information.Operation.realizedExchangeItems

#print('information.cross_init done')

#print('interaction.cross_init starting')


interaction.SequenceMessage.exchangeContext.eType = capellacore.Constraint
interaction.SequenceMessage.sendingEnd.eType = interaction.MessageEnd
interaction.SequenceMessage.receivingEnd.eType = interaction.MessageEnd
interaction.SequenceMessage._invokedOperation.eType = information.AbstractEventOperation
interaction.SequenceMessage.exchangedItems.eType = information.ExchangeItem
interaction.SequenceMessage._sendingPart.eType = cs.Part
interaction.SequenceMessage._receivingPart.eType = cs.Part
interaction.SequenceMessage._sendingFunction.eType = fa.AbstractFunction
interaction.SequenceMessage._receivingFunction.eType = fa.AbstractFunction
interaction.SequenceMessage.ownedSequenceMessageValuations.eType = interaction.SequenceMessageValuation
interaction.Scenario.preCondition.eType = capellacore.Constraint
interaction.Scenario.postCondition.eType = capellacore.Constraint
interaction.Scenario.ownedInstanceRoles.eType = interaction.InstanceRole
interaction.Scenario.ownedMessages.eType = interaction.SequenceMessage
interaction.Scenario.ownedInteractionFragments.eType = interaction.InteractionFragment
interaction.Scenario.ownedTimeLapses.eType = interaction.TimeLapse
interaction.Scenario.ownedEvents.eType = interaction.Event
interaction.Scenario.ownedFormalGates.eType = interaction.Gate
interaction.Scenario.ownedScenarioRealization.eType = interaction.ScenarioRealization
interaction.Scenario.ownedConstraintDurations.eType = interaction.ConstraintDuration
interaction.Scenario.containedFunctions.eType = fa.AbstractFunction
interaction.Scenario.containedParts.eType = cs.Part
interaction.Scenario.referencedScenarios.eType = interaction.Scenario
interaction.MessageEnd._message.eType = interaction.SequenceMessage
interaction.Execution._covered.eType = interaction.InstanceRole
interaction.ExecutionEnd._execution.eType = interaction.Execution
interaction.InstanceRole.representedInstance.eType = information.AbstractInstance
interaction.AbstractEnd.event.eType = interaction.Event
interaction.EventReceiptOperation.operation.eType = information.AbstractEventOperation
interaction.EventSentOperation.operation.eType = information.AbstractEventOperation
interaction.AbstractCapability.preCondition.eType = capellacore.Constraint
interaction.AbstractCapability.postCondition.eType = capellacore.Constraint
interaction.AbstractCapability.ownedScenarios.eType = interaction.Scenario
interaction.AbstractCapability.extends.eType = interaction.AbstractCapabilityExtend
interaction.AbstractCapability.extending.eType = interaction.AbstractCapabilityExtend
interaction.AbstractCapability.abstractCapabilityExtensionPoints.eType = interaction.AbstractCapabilityExtensionPoint
interaction.AbstractCapability.superGeneralizations.eType = interaction.AbstractCapabilityGeneralization
interaction.AbstractCapability.subGeneralizations.eType = interaction.AbstractCapabilityGeneralization
interaction.AbstractCapability.includes.eType = interaction.AbstractCapabilityInclude
interaction.AbstractCapability.including.eType = interaction.AbstractCapabilityInclude
interaction.AbstractCapability.super_.eType = interaction.AbstractCapability
interaction.AbstractCapability.sub.eType = interaction.AbstractCapability
interaction.AbstractCapability.includedAbstractCapabilities.eType = interaction.AbstractCapability
interaction.AbstractCapability.includingAbstractCapabilities.eType = interaction.AbstractCapability
interaction.AbstractCapability.extendedAbstractCapabilities.eType = interaction.AbstractCapability
interaction.AbstractCapability.extendingAbstractCapabilities.eType = interaction.AbstractCapability
interaction.AbstractCapability.ownedFunctionalChainAbstractCapabilityInvolvements.eType = interaction.FunctionalChainAbstractCapabilityInvolvement
interaction.AbstractCapability.ownedAbstractFunctionAbstractCapabilityInvolvements.eType = interaction.AbstractFunctionAbstractCapabilityInvolvement
interaction.AbstractCapability.availableInStates.eType = capellacommon.State
interaction.AbstractCapability.ownedAbstractCapabilityRealizations.eType = interaction.AbstractCapabilityRealization
interaction.AbstractCapability.involvedAbstractFunctions.eType = fa.AbstractFunction
interaction.AbstractCapability.involvedFunctionalChains.eType = fa.FunctionalChain
interaction.AbstractCapabilityExtend.extended.eType = interaction.AbstractCapability
interaction.AbstractCapabilityExtend._extension.eType = interaction.AbstractCapability
interaction.AbstractCapabilityExtensionPoint._abstractCapability.eType = interaction.AbstractCapability
interaction.AbstractCapabilityGeneralization.super_.eType = interaction.AbstractCapability
interaction.AbstractCapabilityGeneralization._sub.eType = interaction.AbstractCapability
interaction.AbstractCapabilityInclude.included.eType = interaction.AbstractCapability
interaction.AbstractCapabilityInclude._inclusion.eType = interaction.AbstractCapability
interaction.InteractionFragment.coveredInstanceRoles.eType = interaction.InstanceRole
interaction.InteractionState.relatedAbstractState.eType = capellacommon.AbstractState
interaction.InteractionState.relatedAbstractFunction.eType = fa.AbstractFunction
interaction.InteractionState._covered.eType = interaction.InstanceRole
interaction.InteractionUse.referencedScenario.eType = interaction.Scenario
interaction.InteractionUse.actualGates.eType = interaction.Gate
interaction.CombinedFragment.referencedOperands.eType = interaction.InteractionOperand
interaction.CombinedFragment.expressionGates.eType = interaction.Gate
interaction.InteractionOperand.referencedInteractionFragments.eType = interaction.InteractionFragment
interaction.InteractionOperand.guard.eType = capellacore.Constraint
interaction.TimeLapse.start.eType = interaction.InteractionFragment
interaction.TimeLapse.finish.eType = interaction.InteractionFragment
interaction.AbstractFragment.ownedGates.eType = interaction.Gate
interaction.FragmentEnd._abstractFragment.eType = interaction.AbstractFragment
interaction.FunctionalChainAbstractCapabilityInvolvement._capability.eType = interaction.AbstractCapability
interaction.FunctionalChainAbstractCapabilityInvolvement._functionalChain.eType = fa.FunctionalChain
interaction.AbstractFunctionAbstractCapabilityInvolvement._capability.eType = interaction.AbstractCapability
interaction.AbstractFunctionAbstractCapabilityInvolvement._function.eType = fa.AbstractFunction
interaction.ScenarioRealization._realizedScenario.eType = interaction.Scenario
interaction.ScenarioRealization._realizingScenario.eType = interaction.Scenario
interaction.StateFragment.relatedAbstractState.eType = capellacommon.AbstractState
interaction.StateFragment.relatedAbstractFunction.eType = fa.AbstractFunction
interaction.ConstraintDuration.start.eType = interaction.InteractionFragment
interaction.ConstraintDuration.finish.eType = interaction.InteractionFragment
interaction.SequenceMessageValuation.exchangeItemElement.eType = information.ExchangeItemElement
interaction.SequenceMessageValuation.value.eType = modellingcore.ValueSpecification
interaction.Scenario.realizedScenarios.eType = interaction.Scenario
interaction.Scenario.realizingScenarios.eType = interaction.Scenario
interaction.Scenario.realizingScenarios.eOpposite = interaction.Scenario.realizedScenarios
interaction.InstanceRole.abstractEnds.eType = interaction.AbstractEnd
interaction.AbstractEnd._covered.eType = interaction.InstanceRole
interaction.AbstractEnd._covered.eOpposite = interaction.InstanceRole.abstractEnds
interaction.AbstractCapabilityRealization._realizedCapability.eType = interaction.AbstractCapability
interaction.AbstractCapabilityRealization._realizingCapability.eType = interaction.AbstractCapability
interaction.AbstractCapability.incomingCapabilityAllocation.eType = interaction.AbstractCapabilityRealization
interaction.AbstractCapability.incomingCapabilityAllocation.eOpposite = interaction.AbstractCapabilityRealization._realizedCapability
interaction.AbstractCapability.outgoingCapabilityAllocation.eType = interaction.AbstractCapabilityRealization
interaction.AbstractCapability.outgoingCapabilityAllocation.eOpposite = interaction.AbstractCapabilityRealization._realizingCapability
interaction.AbstractCapabilityExtend.extensionLocation.eType = interaction.AbstractCapabilityExtensionPoint
interaction.AbstractCapabilityExtensionPoint.extendLinks.eType = interaction.AbstractCapabilityExtend
interaction.AbstractCapabilityExtensionPoint.extendLinks.eOpposite = interaction.AbstractCapabilityExtend.extensionLocation

#print('interaction.cross_init done')

#print('la.cross_init starting')


la.LogicalArchitecturePkg.ownedLogicalArchitectures.eType = la.LogicalArchitecture
la.LogicalArchitecture.ownedLogicalComponentPkg.eType = la.LogicalComponentPkg
la.LogicalArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
la.LogicalArchitecture._containedLogicalFunctionPkg.eType = la.LogicalFunctionPkg
la.LogicalArchitecture.ownedSystemAnalysisRealizations.eType = la.SystemAnalysisRealization
la.LogicalArchitecture.allocatedSystemAnalysisRealizations.eType = la.SystemAnalysisRealization
la.LogicalFunction.ownedLogicalFunctionPkgs.eType = la.LogicalFunctionPkg
la.LogicalFunction.containedLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunction.childrenLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunctionPkg.ownedLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunctionPkg.ownedLogicalFunctionPkgs.eType = la.LogicalFunctionPkg
la.LogicalComponent.ownedLogicalComponents.eType = la.LogicalComponent
la.LogicalComponent.ownedLogicalArchitectures.eType = la.LogicalArchitecture
la.LogicalComponent.ownedLogicalComponentPkgs.eType = la.LogicalComponentPkg
la.LogicalComponent.subLogicalComponents.eType = la.LogicalComponent
la.LogicalComponent.realizedSystemComponents.eType = ctx.SystemComponent
la.LogicalComponentPkg.ownedLogicalComponents.eType = la.LogicalComponent
la.LogicalComponentPkg.ownedLogicalComponentPkgs.eType = la.LogicalComponentPkg
la.CapabilityRealization.ownedCapabilityRealizationInvolvements.eType = capellacommon.CapabilityRealizationInvolvement
la.CapabilityRealization.involvedComponents.eType = capellacommon.CapabilityRealizationInvolvedElement
la.CapabilityRealizationPkg.ownedCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealizationPkg.ownedCapabilityRealizationPkgs.eType = la.CapabilityRealizationPkg
la.LogicalArchitecture.allocatedSystemAnalyses.eType = ctx.SystemAnalysis
la.LogicalArchitecture.allocatingPhysicalArchitectures.eType = pa.PhysicalArchitecture
la.LogicalFunction.allocatingLogicalComponents.eType = la.LogicalComponent
la.LogicalFunction.realizedSystemFunctions.eType = ctx.SystemFunction
la.LogicalFunction.realizingPhysicalFunctions.eType = pa.PhysicalFunction
la.LogicalComponent.allocatedLogicalFunctions.eType = la.LogicalFunction
la.LogicalComponent.allocatedLogicalFunctions.eOpposite = la.LogicalFunction.allocatingLogicalComponents
la.LogicalComponent.realizingPhysicalComponents.eType = pa.PhysicalComponent
la.CapabilityRealization.realizedCapabilities.eType = ctx.Capability
la.CapabilityRealization.realizedCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealization.realizingCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealization.realizingCapabilityRealizations.eOpposite = la.CapabilityRealization.realizedCapabilityRealizations

#print('la.cross_init done')

#print('oa.cross_init starting')


oa.OperationalAnalysis.ownedRolePkg.eType = oa.RolePkg
oa.OperationalAnalysis.ownedEntityPkg.eType = oa.EntityPkg
oa.OperationalAnalysis.ownedConceptPkg.eType = oa.ConceptPkg
oa.OperationalAnalysis._containedOperationalCapabilityPkg.eType = oa.OperationalCapabilityPkg
oa.OperationalAnalysis._containedOperationalActivityPkg.eType = oa.OperationalActivityPkg
oa.OperationalActivityPkg.ownedOperationalActivities.eType = oa.OperationalActivity
oa.OperationalActivityPkg.ownedOperationalActivityPkgs.eType = oa.OperationalActivityPkg
oa.OperationalActivity.ownedOperationalActivityPkgs.eType = oa.OperationalActivityPkg
oa.OperationalActivity.ownedSwimlanes.eType = oa.Swimlane
oa.OperationalActivity.ownedProcess.eType = oa.OperationalProcess
oa.OperationalActivity.allocatingRoles.eType = oa.Role
oa.OperationalActivity.containedOperationalActivities.eType = oa.OperationalActivity
oa.OperationalActivity.childrenOperationalActivities.eType = oa.OperationalActivity
oa.OperationalProcess.involvingOperationalCapabilities.eType = oa.OperationalCapability
oa.Swimlane._representedEntity.eType = oa.Entity
oa.OperationalCapabilityPkg.ownedOperationalCapabilities.eType = oa.OperationalCapability
oa.OperationalCapabilityPkg.ownedOperationalCapabilityPkgs.eType = oa.OperationalCapabilityPkg
oa.OperationalCapabilityPkg.ownedCapabilityConfigurations.eType = oa.CapabilityConfiguration
oa.OperationalCapabilityPkg.ownedConceptCompliances.eType = oa.ConceptCompliance
oa.OperationalCapability.compliances.eType = oa.ConceptCompliance
oa.OperationalCapability.configurations.eType = oa.CapabilityConfiguration
oa.OperationalCapability.ownedEntityOperationalCapabilityInvolvements.eType = oa.EntityOperationalCapabilityInvolvement
oa.OperationalCapability.involvedEntities.eType = oa.Entity
oa.RolePkg.ownedRolePkgs.eType = oa.RolePkg
oa.RolePkg.ownedRoles.eType = oa.Role
oa.Role.ownedRoleAssemblyUsages.eType = oa.RoleAssemblyUsage
oa.Role.ownedActivityAllocations.eType = oa.ActivityAllocation
oa.Role.allocatingEntities.eType = oa.Entity
oa.Role.allocatedOperationalActivities.eType = oa.OperationalActivity
oa.RoleAssemblyUsage.child.eType = oa.Role
oa.EntityPkg.ownedEntities.eType = oa.Entity
oa.EntityPkg.ownedEntityPkgs.eType = oa.EntityPkg
oa.EntityPkg.ownedLocations.eType = oa.Location
oa.EntityPkg.ownedCommunicationMeans.eType = oa.CommunicationMean
oa.Entity.organisationalUnitMemberships.eType = oa.OrganisationalUnitComposition
oa.Entity.actualLocation.eType = oa.Location
oa.Entity.subEntities.eType = oa.Entity
oa.Entity.ownedEntities.eType = oa.Entity
oa.Entity.ownedCommunicationMeans.eType = oa.CommunicationMean
oa.Entity.ownedRoleAllocations.eType = oa.RoleAllocation
oa.Entity.allocatedRoles.eType = oa.Role
oa.Entity.involvingOperationalCapabilities.eType = oa.OperationalCapability
oa.Entity.realizingSystemComponents.eType = ctx.SystemComponent
oa.ConceptPkg.ownedConceptPkgs.eType = oa.ConceptPkg
oa.ConceptPkg.ownedConcepts.eType = oa.Concept
oa.Concept.compliances.eType = oa.ConceptCompliance
oa.Concept.compositeLinks.eType = oa.ItemInConcept
oa.ConceptCompliance.complyWithConcept.eType = oa.Concept
oa.ConceptCompliance.compliantCapability.eType = oa.OperationalCapability
oa.ItemInConcept.concept.eType = oa.Concept
oa.ItemInConcept.item.eType = oa.AbstractConceptItem
oa.AbstractConceptItem.composingLinks.eType = oa.ItemInConcept
oa.CommunityOfInterest.communityOfInterestCompositions.eType = oa.CommunityOfInterestComposition
oa.CommunityOfInterestComposition.communityOfInterest.eType = oa.CommunityOfInterest
oa.CommunityOfInterestComposition.interestedOrganisationUnit.eType = oa.OrganisationalUnit
oa.OrganisationalUnit.organisationalUnitCompositions.eType = oa.OrganisationalUnitComposition
oa.OrganisationalUnit.communityOfInterestMemberships.eType = oa.CommunityOfInterestComposition
oa.OrganisationalUnitComposition.organisationalUnit.eType = oa.OrganisationalUnit
oa.OrganisationalUnitComposition.participatingEntity.eType = oa.Entity
oa.Location.locatedEntities.eType = oa.Entity
oa.CapabilityConfiguration.configuredCapability.eType = oa.OperationalCapability
oa.CommunicationMean._sourceEntity.eType = oa.Entity
oa.CommunicationMean._targetEntity.eType = oa.Entity
oa.EntityOperationalCapabilityInvolvement._entity.eType = oa.Entity
oa.EntityOperationalCapabilityInvolvement._capability.eType = oa.OperationalCapability
oa.OperationalAnalysis.allocatingSystemAnalyses.eType = ctx.SystemAnalysis
oa.OperationalActivity.activityAllocations.eType = oa.ActivityAllocation
oa.OperationalActivity.allocatorEntities.eType = oa.Entity
oa.OperationalActivity.realizingSystemFunctions.eType = ctx.SystemFunction
oa.OperationalCapability.realizingCapabilities.eType = ctx.Capability
oa.ActivityAllocation._role.eType = oa.Role
oa.ActivityAllocation._activity.eType = oa.OperationalActivity
oa.ActivityAllocation._activity.eOpposite = oa.OperationalActivity.activityAllocations
oa.Role.roleAllocations.eType = oa.RoleAllocation
oa.Role.activityAllocations.eType = oa.ActivityAllocation
oa.Role.activityAllocations.eOpposite = oa.ActivityAllocation._role
oa.RoleAllocation._role.eType = oa.Role
oa.RoleAllocation._role.eOpposite = oa.Role.roleAllocations
oa.RoleAllocation._entity.eType = oa.Entity
oa.Entity.roleAllocations.eType = oa.RoleAllocation
oa.Entity.roleAllocations.eOpposite = oa.RoleAllocation._entity
oa.Entity.allocatedOperationalActivities.eType = oa.OperationalActivity
oa.Entity.allocatedOperationalActivities.eOpposite = oa.OperationalActivity.allocatorEntities

#print('oa.cross_init done')

#print('pa.cross_init starting')


pa.deployment.ComponentInstance.portInstances.eType = pa.deployment.PortInstance
pa.deployment.ComponentInstance.ownedAbstractPhysicalInstances.eType = pa.deployment.AbstractPhysicalInstance
pa.deployment.ComponentInstance.ownedInstanceDeploymentLinks.eType = pa.deployment.InstanceDeploymentLink
pa.deployment.ComponentInstance.type.eType = pa.PhysicalComponent
pa.deployment.ConnectionInstance.type.eType = fa.ComponentExchange
pa.deployment.DeploymentAspect.ownedConfigurations.eType = pa.deployment.DeploymentConfiguration
pa.deployment.DeploymentAspect.ownedDeploymentAspects.eType = pa.deployment.DeploymentAspect
pa.deployment.DeploymentConfiguration.ownedDeploymentLinks.eType = cs.AbstractDeploymentLink
pa.deployment.DeploymentConfiguration.ownedPhysicalInstances.eType = pa.deployment.AbstractPhysicalInstance
pa.deployment.PortInstance._component.eType = pa.deployment.ComponentInstance
pa.deployment.PortInstance.type.eType = fa.ComponentPort
pa.PhysicalArchitecturePkg.ownedPhysicalArchitecturePkgs.eType = pa.PhysicalArchitecturePkg
pa.PhysicalArchitecturePkg.ownedPhysicalArchitectures.eType = pa.PhysicalArchitecture
pa.PhysicalArchitecture.ownedPhysicalComponentPkg.eType = pa.PhysicalComponentPkg
pa.PhysicalArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
pa.PhysicalArchitecture._containedPhysicalFunctionPkg.eType = pa.PhysicalFunctionPkg
pa.PhysicalArchitecture.ownedDeployments.eType = cs.AbstractDeploymentLink
pa.PhysicalArchitecture.ownedLogicalArchitectureRealizations.eType = pa.LogicalArchitectureRealization
pa.PhysicalArchitecture.allocatedLogicalArchitectureRealizations.eType = pa.LogicalArchitectureRealization
pa.PhysicalFunction.ownedPhysicalFunctionPkgs.eType = pa.PhysicalFunctionPkg
pa.PhysicalFunction.containedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunction.childrenPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunctionPkg.ownedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunctionPkg.ownedPhysicalFunctionPkgs.eType = pa.PhysicalFunctionPkg
pa.PhysicalComponent.ownedDeploymentLinks.eType = cs.AbstractDeploymentLink
pa.PhysicalComponent.ownedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.ownedPhysicalComponentPkgs.eType = pa.PhysicalComponentPkg
pa.PhysicalComponent.logicalInterfaceRealizations.eType = pa.LogicalInterfaceRealization
pa.PhysicalComponent.subPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.deployedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.deployingPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponentPkg.ownedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponentPkg.ownedPhysicalComponentPkgs.eType = pa.PhysicalComponentPkg
pa.PhysicalComponentPkg.ownedKeyParts.eType = information.KeyPart
pa.PhysicalComponentPkg.ownedDeployments.eType = cs.AbstractDeploymentLink
pa.PhysicalNode.subPhysicalNodes.eType = pa.PhysicalNode
pa.deployment.ConnectionInstance.connectionEnds.eType = pa.deployment.PortInstance
pa.deployment.PortInstance.connections.eType = pa.deployment.ConnectionInstance
pa.deployment.PortInstance.connections.eOpposite = pa.deployment.ConnectionInstance.connectionEnds
pa.PhysicalArchitecture.allocatedLogicalArchitectures.eType = la.LogicalArchitecture
pa.PhysicalArchitecture.allocatingEpbsArchitectures.eType = epbs.EPBSArchitecture
pa.PhysicalFunction.allocatingPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalFunction.realizedLogicalFunctions.eType = la.LogicalFunction
pa.PhysicalComponent.realizedLogicalComponents.eType = la.LogicalComponent
pa.PhysicalComponent.allocatedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalComponent.allocatedPhysicalFunctions.eOpposite = pa.PhysicalFunction.allocatingPhysicalComponents

#print('pa.cross_init done')

#print('requirement.cross_init starting')


requirement.RequirementsPkg.ownedRequirements.eType = requirement.Requirement
requirement.RequirementsPkg.ownedRequirementPkgs.eType = requirement.RequirementsPkg
requirement.RequirementsTrace._source.eType = modellingcore.TraceableElement
requirement.RequirementsTrace._target.eType = modellingcore.TraceableElement
requirement.Requirement.relatedCapellaElements.eType = capellacore.CapellaElement

#print('requirement.cross_init done')

#print('sharedmodel.cross_init starting')


sharedmodel.SharedPkg.ownedDataPkg.eType = information.DataPkg
sharedmodel.SharedPkg.ownedGenericPkg.eType = sharedmodel.GenericPkg
sharedmodel.GenericPkg.subGenericPkgs.eType = sharedmodel.GenericPkg
sharedmodel.GenericPkg.capellaElements.eType = capellacore.CapellaElement

#print('sharedmodel.cross_init done')

#print('libraries.cross_init starting')


libraries.ModelInformation.ownedReferences.eType = libraries.LibraryReference
libraries.ModelInformation.version.eType = libraries.ModelVersion
libraries.LibraryReference.library.eType = libraries.ModelInformation
libraries.LibraryReference.version.eType = libraries.ModelVersion

#print('libraries.cross_init done')

#print('emde.cross_init starting')


emde.ExtensibleElement.ownedExtensions.eType = emde.ElementExtension

#print('emde.cross_init done')

# Manual patching circular dep for inheritance
information.communication.SignalInstance._staticEClass = False
information.communication.SignalInstance.eClass.eSuperTypes.append(information.AbstractInstance.eClass)
