
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
