
from .activity import getEClassifier, eClassifiers
from .activity import name, nsURI, nsPrefix, eClass
from .activity import AbstractActivity, ExceptionHandler, ActivityGroup, InterruptibleActivityRegion, ObjectNodeOrderingKind, ObjectNodeKind, ActivityEdge, ControlFlow, ObjectFlow, ActivityPartition, ActivityExchange, ActivityNode, ExecutableNode, StructuredActivityNode, AbstractAction, AcceptEventAction, InvocationAction, SendSignalAction, CallAction, CallBehaviorAction, ObjectNode, Pin, InputPin, ValuePin, OutputPin

from modellingcore import AbstractConstraint, AbstractParameter, AbstractConstraint, IState, AbstractParameterSet, AbstractType, AbstractTrace, AbstractType, ValueSpecification, ModelElement, AbstractRelationship, AbstractInformationFlow, AbstractExchangeItem, InformationsExchanger
from behavior import AbstractBehavior, AbstractSignal
from emde import ElementExtension

from . import activity

__all__ = ['AbstractActivity', 'ExceptionHandler', 'ActivityGroup', 'InterruptibleActivityRegion', 'ObjectNodeOrderingKind', 'ObjectNodeKind', 'ActivityEdge', 'ControlFlow', 'ObjectFlow', 'ActivityPartition', 'ActivityExchange',
           'ActivityNode', 'ExecutableNode', 'StructuredActivityNode', 'AbstractAction', 'AcceptEventAction', 'InvocationAction', 'SendSignalAction', 'CallAction', 'CallBehaviorAction', 'ObjectNode', 'Pin', 'InputPin', 'ValuePin', 'OutputPin']

eSubpackages = []
eSuperPackage = None
activity.eSubpackages = eSubpackages
activity.eSuperPackage = eSuperPackage

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

otherClassifiers = [ObjectNodeOrderingKind, ObjectNodeKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
