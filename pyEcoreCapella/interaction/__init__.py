
from .interaction import getEClassifier, eClassifiers
from .interaction import name, nsURI, nsPrefix, eClass
from .interaction import SequenceMessage, Scenario, MessageEnd, Execution, ExecutionEnd, CreationEvent, DestructionEvent, ExecutionEvent, InstanceRole, AbstractEnd, MessageKind, Event, EventReceiptOperation, EventSentOperation, MergeLink, RefinementLink, AbstractCapabilityRealization, AbstractCapability, AbstractCapabilityExtend, AbstractCapabilityExtensionPoint, AbstractCapabilityGeneralization, AbstractCapabilityInclude, ScenarioKind, InteractionFragment, InteractionState, InteractionUse, CombinedFragment, Gate, InteractionOperand, InteractionOperatorKind, TimeLapse, AbstractFragment, FragmentEnd, FunctionalChainAbstractCapabilityInvolvement, AbstractFunctionAbstractCapabilityInvolvement, ScenarioRealization, StateFragment, ArmTimerEvent, CancelTimerEvent, ConstraintDuration, SequenceMessageValuation

from modellingcore import AbstractConstraint, AbstractParameter, AbstractParameterSet, AbstractTrace, AbstractTypedElement, ValueSpecification, AbstractInformationFlow, ModelElement, TraceableElement
from capellacore import EnumerationPropertyLiteral, Trace, InvolverElement, AbstractPropertyValue, InvolvedElement, EnumerationPropertyType, NamingRule, Involvement, PropertyValueGroup, PropertyValuePkg, Constraint
from information import ExchangeItemElement, AbstractInstance, AbstractEventOperation, ExchangeItem
from capellacommon import GenericTrace, State, AbstractState
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from fa import AbstractFunction, FunctionalChain, FunctionalChain
from cs import Part

from . import interaction

__all__ = ['SequenceMessage', 'Scenario', 'MessageEnd', 'Execution', 'ExecutionEnd', 'CreationEvent', 'DestructionEvent', 'ExecutionEvent', 'InstanceRole', 'AbstractEnd', 'MessageKind', 'Event', 'EventReceiptOperation', 'EventSentOperation', 'MergeLink', 'RefinementLink', 'AbstractCapabilityRealization', 'AbstractCapability', 'AbstractCapabilityExtend', 'AbstractCapabilityExtensionPoint', 'AbstractCapabilityGeneralization',
           'AbstractCapabilityInclude', 'ScenarioKind', 'InteractionFragment', 'InteractionState', 'InteractionUse', 'CombinedFragment', 'Gate', 'InteractionOperand', 'InteractionOperatorKind', 'TimeLapse', 'AbstractFragment', 'FragmentEnd', 'FunctionalChainAbstractCapabilityInvolvement', 'AbstractFunctionAbstractCapabilityInvolvement', 'ScenarioRealization', 'StateFragment', 'ArmTimerEvent', 'CancelTimerEvent', 'ConstraintDuration', 'SequenceMessageValuation']

eSubpackages = []
eSuperPackage = None
interaction.eSubpackages = eSubpackages
interaction.eSuperPackage = eSuperPackage

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
AbstractCapability.incomingCapabilityAllocation.eOpposite = AbstractCapabilityRealization.realizedCapability
AbstractCapability.outgoingCapabilityAllocation.eType = AbstractCapabilityRealization
AbstractCapability.outgoingCapabilityAllocation.eOpposite = AbstractCapabilityRealization.realizingCapability
AbstractCapabilityExtend.extensionLocation.eType = AbstractCapabilityExtensionPoint
AbstractCapabilityExtensionPoint.extendLinks.eType = AbstractCapabilityExtend
AbstractCapabilityExtensionPoint.extendLinks.eOpposite = AbstractCapabilityExtend.extensionLocation

otherClassifiers = [MessageKind, ScenarioKind, InteractionOperatorKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
