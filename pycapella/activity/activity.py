"""Definition of meta model 'activity'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from behavior import AbstractBehavior
from modellingcore import AbstractInformationFlow, AbstractNamedElement, AbstractRelationship, AbstractTypedElement, ModelElement, RateKind, TraceableElement


name = 'activity'
nsURI = 'http://www.polarsys.org/capella/common/activity/1.4.0'
nsPrefix = 'org.polarsys.capella.common.data.activity'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ObjectNodeOrderingKind = EEnum('ObjectNodeOrderingKind', literals=[
                               'FIFO', 'LIFO', 'ordered', 'unordered'])

ObjectNodeKind = EEnum('ObjectNodeKind', literals=['Unspecified', 'NoBuffer', 'Overwrite'])


@abstract
class ExceptionHandler(ModelElement):

    protectedNode = EReference(ordered=True, unique=True, containment=False, derived=False)
    handlerBody = EReference(ordered=True, unique=True, containment=False, derived=False)
    exceptionInput = EReference(ordered=True, unique=True, containment=False, derived=False)
    exceptionTypes = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)

    def __init__(self, *, protectedNode=None, handlerBody=None, exceptionInput=None, exceptionTypes=None, **kwargs):

        super().__init__(**kwargs)

        if protectedNode is not None:
            self.protectedNode = protectedNode

        if handlerBody is not None:
            self.handlerBody = handlerBody

        if exceptionInput is not None:
            self.exceptionInput = exceptionInput

        if exceptionTypes:
            self.exceptionTypes.extend(exceptionTypes)


@abstract
class ActivityGroup(ModelElement):

    superGroup = EReference(ordered=True, unique=True, containment=False, derived=False)
    subGroups = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedNodes = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedEdges = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, superGroup=None, subGroups=None, ownedNodes=None, ownedEdges=None, **kwargs):

        super().__init__(**kwargs)

        if superGroup is not None:
            self.superGroup = superGroup

        if subGroups:
            self.subGroups.extend(subGroups)

        if ownedNodes:
            self.ownedNodes.extend(ownedNodes)

        if ownedEdges:
            self.ownedEdges.extend(ownedEdges)


@abstract
class InterruptibleActivityRegion(ActivityGroup):

    interruptingEdges = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)

    def __init__(self, *, interruptingEdges=None, **kwargs):

        super().__init__(**kwargs)

        if interruptingEdges:
            self.interruptingEdges.extend(interruptingEdges)


@abstract
class ActivityEdge(AbstractRelationship):

    kindOfRate = EAttribute(eType=RateKind, unique=True, derived=False, changeable=True)
    _inActivityPartition = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inActivityPartition', transient=True)
    _inInterruptibleRegion = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inInterruptibleRegion', transient=True)
    _inStructuredNode = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inStructuredNode', transient=True)
    rate = EReference(ordered=True, unique=True, containment=True, derived=False)
    probability = EReference(ordered=True, unique=True, containment=True, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    guard = EReference(ordered=True, unique=True, containment=True, derived=False)
    weight = EReference(ordered=True, unique=True, containment=True, derived=False)
    interrupts = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def inActivityPartition(self):
        raise NotImplementedError('Missing implementation for inActivityPartition')

    @property
    def inInterruptibleRegion(self):
        raise NotImplementedError('Missing implementation for inInterruptibleRegion')

    @property
    def inStructuredNode(self):
        raise NotImplementedError('Missing implementation for inStructuredNode')

    def __init__(self, *, kindOfRate=None, inActivityPartition=None, inInterruptibleRegion=None, inStructuredNode=None, rate=None, probability=None, target=None, source=None, guard=None, weight=None, interrupts=None, **kwargs):

        super().__init__(**kwargs)

        if kindOfRate is not None:
            self.kindOfRate = kindOfRate

        if inActivityPartition is not None:
            self.inActivityPartition = inActivityPartition

        if inInterruptibleRegion is not None:
            self.inInterruptibleRegion = inInterruptibleRegion

        if inStructuredNode is not None:
            self.inStructuredNode = inStructuredNode

        if rate is not None:
            self.rate = rate

        if probability is not None:
            self.probability = probability

        if target is not None:
            self.target = target

        if source is not None:
            self.source = source

        if guard is not None:
            self.guard = guard

        if weight is not None:
            self.weight = weight

        if interrupts is not None:
            self.interrupts = interrupts


class DerivedOutgoing(EDerivedCollection):
    pass


class DerivedIncoming(EDerivedCollection):
    pass


@abstract
class ActivityNode(AbstractNamedElement):

    _inActivityPartition = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inActivityPartition', transient=True)
    _inInterruptibleRegion = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inInterruptibleRegion', transient=True)
    _inStructuredNode = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='inStructuredNode', transient=True)
    outgoing = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedOutgoing)
    incoming = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedIncoming)

    @property
    def inActivityPartition(self):
        raise NotImplementedError('Missing implementation for inActivityPartition')

    @property
    def inInterruptibleRegion(self):
        raise NotImplementedError('Missing implementation for inInterruptibleRegion')

    @property
    def inStructuredNode(self):
        raise NotImplementedError('Missing implementation for inStructuredNode')

    def __init__(self, *, inActivityPartition=None, inInterruptibleRegion=None, inStructuredNode=None, outgoing=None, incoming=None, **kwargs):

        super().__init__(**kwargs)

        if inActivityPartition is not None:
            self.inActivityPartition = inActivityPartition

        if inInterruptibleRegion is not None:
            self.inInterruptibleRegion = inInterruptibleRegion

        if inStructuredNode is not None:
            self.inStructuredNode = inStructuredNode

        if outgoing:
            self.outgoing.extend(outgoing)

        if incoming:
            self.incoming.extend(incoming)


@abstract
class ControlFlow(ActivityEdge):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ObjectFlow(ActivityEdge):

    isMulticast = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isMultireceive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    transformation = EReference(ordered=True, unique=True, containment=False, derived=False)
    selection = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, isMulticast=None, isMultireceive=None, transformation=None, selection=None, **kwargs):

        super().__init__(**kwargs)

        if isMulticast is not None:
            self.isMulticast = isMulticast

        if isMultireceive is not None:
            self.isMultireceive = isMultireceive

        if transformation is not None:
            self.transformation = transformation

        if selection is not None:
            self.selection = selection


@abstract
class ExecutableNode(ActivityNode):

    ownedHandlers = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedHandlers=None, **kwargs):

        super().__init__(**kwargs)

        if ownedHandlers:
            self.ownedHandlers.extend(ownedHandlers)


class DerivedOwnedstructurednodes(EDerivedCollection):
    pass


@abstract
class AbstractActivity(AbstractBehavior, TraceableElement):

    isReadOnly = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isSingleExecution = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedNodes = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedEdges = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedGroups = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedStructuredNodes = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedOwnedstructurednodes)

    def __init__(self, *, isReadOnly=None, isSingleExecution=None, ownedNodes=None, ownedEdges=None, ownedGroups=None, ownedStructuredNodes=None, **kwargs):

        super().__init__(**kwargs)

        if isReadOnly is not None:
            self.isReadOnly = isReadOnly

        if isSingleExecution is not None:
            self.isSingleExecution = isSingleExecution

        if ownedNodes:
            self.ownedNodes.extend(ownedNodes)

        if ownedEdges:
            self.ownedEdges.extend(ownedEdges)

        if ownedGroups:
            self.ownedGroups.extend(ownedGroups)

        if ownedStructuredNodes:
            self.ownedStructuredNodes.extend(ownedStructuredNodes)


class DerivedSubpartitions(EDerivedCollection):
    pass


@abstract
class ActivityPartition(ActivityGroup, AbstractNamedElement):

    isDimension = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isExternal = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    representedElement = EReference(ordered=True, unique=True, containment=False, derived=False)
    _superPartition = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, name='superPartition', transient=True)
    subPartitions = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedSubpartitions)

    @property
    def superPartition(self):
        raise NotImplementedError('Missing implementation for superPartition')

    def __init__(self, *, isDimension=None, isExternal=None, representedElement=None, superPartition=None, subPartitions=None, **kwargs):

        super().__init__(**kwargs)

        if isDimension is not None:
            self.isDimension = isDimension

        if isExternal is not None:
            self.isExternal = isExternal

        if representedElement is not None:
            self.representedElement = representedElement

        if superPartition is not None:
            self.superPartition = superPartition

        if subPartitions:
            self.subPartitions.extend(subPartitions)


class DerivedRealizingactivityflows(EDerivedCollection):
    pass


@abstract
class ActivityExchange(AbstractInformationFlow):

    realizingActivityFlows = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingactivityflows)

    def __init__(self, *, realizingActivityFlows=None, **kwargs):

        super().__init__(**kwargs)

        if realizingActivityFlows:
            self.realizingActivityFlows.extend(realizingActivityFlows)


@abstract
class AbstractAction(ExecutableNode, AbstractNamedElement):

    localPrecondition = EReference(ordered=True, unique=True, containment=True, derived=False)
    localPostcondition = EReference(ordered=True, unique=True, containment=True, derived=False)
    context = EReference(ordered=True, unique=True, containment=False, derived=False)
    inputs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    outputs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, localPrecondition=None, localPostcondition=None, context=None, inputs=None, outputs=None, **kwargs):

        super().__init__(**kwargs)

        if localPrecondition is not None:
            self.localPrecondition = localPrecondition

        if localPostcondition is not None:
            self.localPostcondition = localPostcondition

        if context is not None:
            self.context = context

        if inputs:
            self.inputs.extend(inputs)

        if outputs:
            self.outputs.extend(outputs)


@abstract
class AcceptEventAction(AbstractAction):

    isUnmarshall = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    result = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, isUnmarshall=None, result=None, **kwargs):

        super().__init__(**kwargs)

        if isUnmarshall is not None:
            self.isUnmarshall = isUnmarshall

        if result:
            self.result.extend(result)


@abstract
class InvocationAction(AbstractAction):

    arguments = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, arguments=None, **kwargs):

        super().__init__(**kwargs)

        if arguments:
            self.arguments.extend(arguments)


@abstract
class ObjectNode(ActivityNode, AbstractTypedElement):

    isControlType = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    kindOfNode = EAttribute(eType=ObjectNodeKind, unique=True, derived=False, changeable=True)
    ordering = EAttribute(eType=ObjectNodeOrderingKind, unique=True, derived=False, changeable=True)
    upperBound = EReference(ordered=True, unique=True, containment=True, derived=False)
    inState = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    selection = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, isControlType=None, kindOfNode=None, ordering=None, upperBound=None, inState=None, selection=None, **kwargs):

        super().__init__(**kwargs)

        if isControlType is not None:
            self.isControlType = isControlType

        if kindOfNode is not None:
            self.kindOfNode = kindOfNode

        if ordering is not None:
            self.ordering = ordering

        if upperBound is not None:
            self.upperBound = upperBound

        if inState:
            self.inState.extend(inState)

        if selection is not None:
            self.selection = selection


@abstract
class SendSignalAction(InvocationAction):

    target = EReference(ordered=True, unique=True, containment=True, derived=False)
    signal = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, target=None, signal=None, **kwargs):

        super().__init__(**kwargs)

        if target is not None:
            self.target = target

        if signal is not None:
            self.signal = signal


@abstract
class CallAction(InvocationAction):

    results = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, results=None, **kwargs):

        super().__init__(**kwargs)

        if results:
            self.results.extend(results)


@abstract
class Pin(ObjectNode):

    isControl = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, isControl=None, **kwargs):

        super().__init__(**kwargs)

        if isControl is not None:
            self.isControl = isControl


@abstract
class StructuredActivityNode(ActivityGroup, AbstractAction):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class CallBehaviorAction(CallAction):

    behavior = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, behavior=None, **kwargs):

        super().__init__(**kwargs)

        if behavior is not None:
            self.behavior = behavior


@abstract
class InputPin(Pin):

    inputEvaluationAction = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, inputEvaluationAction=None, **kwargs):

        super().__init__(**kwargs)

        if inputEvaluationAction is not None:
            self.inputEvaluationAction = inputEvaluationAction


@abstract
class OutputPin(Pin):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ValuePin(InputPin):

    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value
