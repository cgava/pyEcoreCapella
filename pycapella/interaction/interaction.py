print('interaction.interaction loading')
"""Definition of meta model 'interaction'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from behavior import AbstractBehavior, AbstractEvent
from capellacore import Allocation, CapellaElement, Involvement, InvolverElement, NamedElement, NamedRelationship, Namespace, Relationship, Structure, Trace
from fa import AbstractFunctionalChainContainer


name = 'interaction'
nsURI = 'http://www.polarsys.org/capella/core/interaction/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.interaction'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
MessageKind = EEnum('MessageKind', literals=[
                    'UNSET', 'ASYNCHRONOUS_CALL', 'SYNCHRONOUS_CALL', 'REPLY', 'DELETE', 'CREATE', 'TIMER'])

ScenarioKind = EEnum('ScenarioKind', literals=[
                     'UNSET', 'INTERFACE', 'DATA_FLOW', 'INTERACTION', 'FUNCTIONAL'])

InteractionOperatorKind = EEnum('InteractionOperatorKind', literals=[
                                'UNSET', 'ALT', 'OPT', 'PAR', 'LOOP', 'CRITICAL', 'NEG', 'ASSERT', 'STRICT', 'SEQ', 'IGNORE', 'CONSIDER'])


class SequenceMessageValuation(CapellaElement):

    exchangeItemElement = EReference(ordered=True, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, exchangeItemElement=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if exchangeItemElement is not None:
            self.exchangeItemElement = exchangeItemElement

        if value is not None:
            self.value = value


class SequenceMessage(NamedElement):

    kind = EAttribute(eType=MessageKind, unique=True, derived=False, changeable=True)
    exchangeContext = EReference(ordered=True, unique=True, containment=False, derived=False)
    sendingEnd = EReference(ordered=True, unique=True, containment=False, derived=False)
    receivingEnd = EReference(ordered=True, unique=True, containment=False, derived=False)
    _invokedOperation = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='invokedOperation', transient=True)
    exchangedItems = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    _sendingPart = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='sendingPart', transient=True)
    _receivingPart = EReference(ordered=True, unique=True, containment=False,
                                derived=True, name='receivingPart', transient=True)
    _sendingFunction = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='sendingFunction', transient=True)
    _receivingFunction = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='receivingFunction', transient=True)
    ownedSequenceMessageValuations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    @property
    def invokedOperation(self):
        raise NotImplementedError('Missing implementation for invokedOperation')

    @property
    def sendingPart(self):
        raise NotImplementedError('Missing implementation for sendingPart')

    @property
    def receivingPart(self):
        raise NotImplementedError('Missing implementation for receivingPart')

    @property
    def sendingFunction(self):
        raise NotImplementedError('Missing implementation for sendingFunction')

    @property
    def receivingFunction(self):
        raise NotImplementedError('Missing implementation for receivingFunction')

    def __init__(self, *, kind=None, exchangeContext=None, sendingEnd=None, receivingEnd=None, invokedOperation=None, exchangedItems=None, sendingPart=None, receivingPart=None, sendingFunction=None, receivingFunction=None, ownedSequenceMessageValuations=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if exchangeContext is not None:
            self.exchangeContext = exchangeContext

        if sendingEnd is not None:
            self.sendingEnd = sendingEnd

        if receivingEnd is not None:
            self.receivingEnd = receivingEnd

        if invokedOperation is not None:
            self.invokedOperation = invokedOperation

        if exchangedItems:
            self.exchangedItems.extend(exchangedItems)

        if sendingPart is not None:
            self.sendingPart = sendingPart

        if receivingPart is not None:
            self.receivingPart = receivingPart

        if sendingFunction is not None:
            self.sendingFunction = sendingFunction

        if receivingFunction is not None:
            self.receivingFunction = receivingFunction

        if ownedSequenceMessageValuations:
            self.ownedSequenceMessageValuations.extend(ownedSequenceMessageValuations)


class DerivedAbstractends(EDerivedCollection):
    pass


class InstanceRole(NamedElement):

    abstractEnds = EReference(ordered=True, unique=True, containment=False,
                              derived=True, upper=-1, transient=True, derived_class=DerivedAbstractends)
    representedInstance = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, abstractEnds=None, representedInstance=None, **kwargs):

        super().__init__(**kwargs)

        if abstractEnds:
            self.abstractEnds.extend(abstractEnds)

        if representedInstance is not None:
            self.representedInstance = representedInstance


class AbstractCapabilityExtend(Relationship):

    extended = EReference(ordered=True, unique=True, containment=False, derived=False)
    _extension = EReference(ordered=True, unique=True, containment=False,
                            derived=True, name='extension', transient=True)
    extensionLocation = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def extension(self):
        raise NotImplementedError('Missing implementation for extension')

    def __init__(self, *, extended=None, extension=None, extensionLocation=None, **kwargs):

        super().__init__(**kwargs)

        if extended is not None:
            self.extended = extended

        if extension is not None:
            self.extension = extension

        if extensionLocation is not None:
            self.extensionLocation = extensionLocation


class AbstractCapabilityGeneralization(Relationship):

    super = EReference(ordered=True, unique=True, containment=False, derived=False)
    _sub = EReference(ordered=True, unique=True, containment=False,
                      derived=True, name='sub', transient=True)

    @property
    def sub(self):
        raise NotImplementedError('Missing implementation for sub')

    def __init__(self, *, super=None, sub=None, **kwargs):

        super().__init__(**kwargs)

        if super is not None:
            self.super = super

        if sub is not None:
            self.sub = sub


class AbstractCapabilityInclude(Relationship):

    included = EReference(ordered=True, unique=True, containment=False, derived=False)
    _inclusion = EReference(ordered=True, unique=True, containment=False,
                            derived=True, name='inclusion', transient=True)

    @property
    def inclusion(self):
        raise NotImplementedError('Missing implementation for inclusion')

    def __init__(self, *, included=None, inclusion=None, **kwargs):

        super().__init__(**kwargs)

        if included is not None:
            self.included = included

        if inclusion is not None:
            self.inclusion = inclusion


@abstract
class InteractionFragment(NamedElement):

    coveredInstanceRoles = EReference(ordered=True, unique=True,
                                      containment=False, derived=False, upper=-1)

    def __init__(self, *, coveredInstanceRoles=None, **kwargs):

        super().__init__(**kwargs)

        if coveredInstanceRoles:
            self.coveredInstanceRoles.extend(coveredInstanceRoles)


@abstract
class TimeLapse(NamedElement):

    start = EReference(ordered=True, unique=True, containment=False, derived=False)
    finish = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, start=None, finish=None, **kwargs):

        super().__init__(**kwargs)

        if start is not None:
            self.start = start

        if finish is not None:
            self.finish = finish


class ConstraintDuration(NamedElement):

    duration = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    start = EReference(ordered=True, unique=True, containment=False, derived=False)
    finish = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, duration=None, start=None, finish=None, **kwargs):

        super().__init__(**kwargs)

        if duration is not None:
            self.duration = duration

        if start is not None:
            self.start = start

        if finish is not None:
            self.finish = finish


class Execution(TimeLapse):

    _covered = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='covered', transient=True)

    @property
    def covered(self):
        raise NotImplementedError('Missing implementation for covered')

    def __init__(self, *, covered=None, **kwargs):

        super().__init__(**kwargs)

        if covered is not None:
            self.covered = covered


@abstract
class AbstractEnd(InteractionFragment):

    event = EReference(ordered=True, unique=True, containment=False, derived=False)
    _covered = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='covered', transient=True)

    @property
    def covered(self):
        raise NotImplementedError('Missing implementation for covered')

    def __init__(self, *, event=None, covered=None, **kwargs):

        super().__init__(**kwargs)

        if event is not None:
            self.event = event

        if covered is not None:
            self.covered = covered


class InteractionState(InteractionFragment):

    relatedAbstractState = EReference(ordered=True, unique=True, containment=False, derived=False)
    relatedAbstractFunction = EReference(
        ordered=True, unique=True, containment=False, derived=False)
    _covered = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='covered', transient=True)

    @property
    def covered(self):
        raise NotImplementedError('Missing implementation for covered')

    def __init__(self, *, relatedAbstractState=None, relatedAbstractFunction=None, covered=None, **kwargs):

        super().__init__(**kwargs)

        if relatedAbstractState is not None:
            self.relatedAbstractState = relatedAbstractState

        if relatedAbstractFunction is not None:
            self.relatedAbstractFunction = relatedAbstractFunction

        if covered is not None:
            self.covered = covered


class InteractionOperand(InteractionFragment):

    referencedInteractionFragments = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    guard = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedInteractionFragments=None, guard=None, **kwargs):

        super().__init__(**kwargs)

        if referencedInteractionFragments:
            self.referencedInteractionFragments.extend(referencedInteractionFragments)

        if guard is not None:
            self.guard = guard


@abstract
class AbstractFragment(TimeLapse):

    ownedGates = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedGates=None, **kwargs):

        super().__init__(**kwargs)

        if ownedGates:
            self.ownedGates.extend(ownedGates)


class FragmentEnd(InteractionFragment):

    _abstractFragment = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='abstractFragment', transient=True)

    @property
    def abstractFragment(self):
        raise NotImplementedError('Missing implementation for abstractFragment')

    def __init__(self, *, abstractFragment=None, **kwargs):

        super().__init__(**kwargs)

        if abstractFragment is not None:
            self.abstractFragment = abstractFragment


class FunctionalChainAbstractCapabilityInvolvement(Involvement):

    _capability = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='capability', transient=True)
    _functionalChain = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='functionalChain', transient=True)

    @property
    def capability(self):
        raise NotImplementedError('Missing implementation for capability')

    @property
    def functionalChain(self):
        raise NotImplementedError('Missing implementation for functionalChain')

    def __init__(self, *, capability=None, functionalChain=None, **kwargs):

        super().__init__(**kwargs)

        if capability is not None:
            self.capability = capability

        if functionalChain is not None:
            self.functionalChain = functionalChain


class AbstractFunctionAbstractCapabilityInvolvement(Involvement):

    _capability = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='capability', transient=True)
    _function = EReference(ordered=True, unique=True, containment=False,
                           derived=True, name='function', transient=True)

    @property
    def capability(self):
        raise NotImplementedError('Missing implementation for capability')

    @property
    def function(self):
        raise NotImplementedError('Missing implementation for function')

    def __init__(self, *, capability=None, function=None, **kwargs):

        super().__init__(**kwargs)

        if capability is not None:
            self.capability = capability

        if function is not None:
            self.function = function


class StateFragment(TimeLapse):

    relatedAbstractState = EReference(ordered=True, unique=True, containment=False, derived=False)
    relatedAbstractFunction = EReference(
        ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, relatedAbstractState=None, relatedAbstractFunction=None, **kwargs):

        super().__init__(**kwargs)

        if relatedAbstractState is not None:
            self.relatedAbstractState = relatedAbstractState

        if relatedAbstractFunction is not None:
            self.relatedAbstractFunction = relatedAbstractFunction


class MessageEnd(AbstractEnd):

    _message = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='message', transient=True)

    @property
    def message(self):
        raise NotImplementedError('Missing implementation for message')

    def __init__(self, *, message=None, **kwargs):

        super().__init__(**kwargs)

        if message is not None:
            self.message = message


class ExecutionEnd(AbstractEnd):

    _execution = EReference(ordered=True, unique=True, containment=False,
                            derived=True, name='execution', transient=True)

    @property
    def execution(self):
        raise NotImplementedError('Missing implementation for execution')

    def __init__(self, *, execution=None, **kwargs):

        super().__init__(**kwargs)

        if execution is not None:
            self.execution = execution


class DerivedActualgates(EDerivedCollection):
    pass


class InteractionUse(AbstractFragment):

    referencedScenario = EReference(ordered=True, unique=True, containment=False, derived=False)
    actualGates = EReference(ordered=True, unique=True, containment=False,
                             derived=True, upper=-1, transient=True, derived_class=DerivedActualgates)

    def __init__(self, *, referencedScenario=None, actualGates=None, **kwargs):

        super().__init__(**kwargs)

        if referencedScenario is not None:
            self.referencedScenario = referencedScenario

        if actualGates:
            self.actualGates.extend(actualGates)


class DerivedExpressiongates(EDerivedCollection):
    pass


class CombinedFragment(AbstractFragment):

    operator = EAttribute(eType=InteractionOperatorKind, unique=True, derived=False,
                          changeable=True, default_value=InteractionOperatorKind.UNSET)
    referencedOperands = EReference(ordered=True, unique=True,
                                    containment=False, derived=False, upper=-1)
    expressionGates = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedExpressiongates)

    def __init__(self, *, operator=None, referencedOperands=None, expressionGates=None, **kwargs):

        super().__init__(**kwargs)

        if operator is not None:
            self.operator = operator

        if referencedOperands:
            self.referencedOperands.extend(referencedOperands)

        if expressionGates:
            self.expressionGates.extend(expressionGates)


class DerivedContainedfunctions(EDerivedCollection):
    pass


class DerivedContainedparts(EDerivedCollection):
    pass


class DerivedReferencedscenarios(EDerivedCollection):
    pass


class DerivedRealizedscenarios(EDerivedCollection):
    pass


class DerivedRealizingscenarios(EDerivedCollection):
    pass


class Scenario(Namespace, AbstractBehavior):

    kind = EAttribute(eType=ScenarioKind, unique=True, derived=False,
                      changeable=True, default_value=ScenarioKind.UNSET)
    merged = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    preCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    postCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    ownedInstanceRoles = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedMessages = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedInteractionFragments = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedTimeLapses = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedEvents = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFormalGates = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedScenarioRealization = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConstraintDurations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    containedFunctions = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedContainedfunctions)
    containedParts = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedContainedparts)
    referencedScenarios = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedReferencedscenarios)
    realizedScenarios = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedRealizedscenarios)
    realizingScenarios = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedRealizingscenarios)

    def __init__(self, *, kind=None, merged=None, preCondition=None, postCondition=None, ownedInstanceRoles=None, ownedMessages=None, ownedInteractionFragments=None, ownedTimeLapses=None, ownedEvents=None, ownedFormalGates=None, ownedScenarioRealization=None, ownedConstraintDurations=None, containedFunctions=None, containedParts=None, referencedScenarios=None, realizedScenarios=None, realizingScenarios=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if merged is not None:
            self.merged = merged

        if preCondition is not None:
            self.preCondition = preCondition

        if postCondition is not None:
            self.postCondition = postCondition

        if ownedInstanceRoles:
            self.ownedInstanceRoles.extend(ownedInstanceRoles)

        if ownedMessages:
            self.ownedMessages.extend(ownedMessages)

        if ownedInteractionFragments:
            self.ownedInteractionFragments.extend(ownedInteractionFragments)

        if ownedTimeLapses:
            self.ownedTimeLapses.extend(ownedTimeLapses)

        if ownedEvents:
            self.ownedEvents.extend(ownedEvents)

        if ownedFormalGates:
            self.ownedFormalGates.extend(ownedFormalGates)

        if ownedScenarioRealization:
            self.ownedScenarioRealization.extend(ownedScenarioRealization)

        if ownedConstraintDurations:
            self.ownedConstraintDurations.extend(ownedConstraintDurations)

        if containedFunctions:
            self.containedFunctions.extend(containedFunctions)

        if containedParts:
            self.containedParts.extend(containedParts)

        if referencedScenarios:
            self.referencedScenarios.extend(referencedScenarios)

        if realizedScenarios:
            self.realizedScenarios.extend(realizedScenarios)

        if realizingScenarios:
            self.realizingScenarios.extend(realizingScenarios)


@abstract
class Event(NamedElement, AbstractEvent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class MergeLink(Trace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RefinementLink(Trace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AbstractCapabilityRealization(Allocation):

    _realizedCapability = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedCapability', transient=True)
    _realizingCapability = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingCapability', transient=True)

    @property
    def realizedCapability(self):
        raise NotImplementedError('Missing implementation for realizedCapability')

    @property
    def realizingCapability(self):
        raise NotImplementedError('Missing implementation for realizingCapability')

    def __init__(self, *, realizedCapability=None, realizingCapability=None, **kwargs):

        super().__init__(**kwargs)

        if realizedCapability is not None:
            self.realizedCapability = realizedCapability

        if realizingCapability is not None:
            self.realizingCapability = realizingCapability


class AbstractCapabilityExtensionPoint(NamedRelationship):

    _abstractCapability = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='abstractCapability', transient=True)
    extendLinks = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    @property
    def abstractCapability(self):
        raise NotImplementedError('Missing implementation for abstractCapability')

    def __init__(self, *, abstractCapability=None, extendLinks=None, **kwargs):

        super().__init__(**kwargs)

        if abstractCapability is not None:
            self.abstractCapability = abstractCapability

        if extendLinks:
            self.extendLinks.extend(extendLinks)


class Gate(MessageEnd):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ScenarioRealization(Allocation):

    _realizedScenario = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedScenario', transient=True)
    _realizingScenario = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingScenario', transient=True)

    @property
    def realizedScenario(self):
        raise NotImplementedError('Missing implementation for realizedScenario')

    @property
    def realizingScenario(self):
        raise NotImplementedError('Missing implementation for realizingScenario')

    def __init__(self, *, realizedScenario=None, realizingScenario=None, **kwargs):

        super().__init__(**kwargs)

        if realizedScenario is not None:
            self.realizedScenario = realizedScenario

        if realizingScenario is not None:
            self.realizingScenario = realizingScenario


class CreationEvent(Event):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DestructionEvent(Event):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ExecutionEvent(Event):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EventReceiptOperation(Event):

    operation = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, operation=None, **kwargs):

        super().__init__(**kwargs)

        if operation is not None:
            self.operation = operation


class EventSentOperation(Event):

    operation = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, operation=None, **kwargs):

        super().__init__(**kwargs)

        if operation is not None:
            self.operation = operation


class ArmTimerEvent(Event):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CancelTimerEvent(Event):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedIncomingcapabilityallocation(EDerivedCollection):
    pass


class DerivedOutgoingcapabilityallocation(EDerivedCollection):
    pass


class DerivedExtending(EDerivedCollection):
    pass


class DerivedSubgeneralizations(EDerivedCollection):
    pass


class DerivedIncluding(EDerivedCollection):
    pass


class DerivedSuper(EDerivedCollection):
    pass


class DerivedSub(EDerivedCollection):
    pass


class DerivedIncludedabstractcapabilities(EDerivedCollection):
    pass


class DerivedIncludingabstractcapabilities(EDerivedCollection):
    pass


class DerivedExtendedabstractcapabilities(EDerivedCollection):
    pass


class DerivedExtendingabstractcapabilities(EDerivedCollection):
    pass


class DerivedInvolvedabstractfunctions(EDerivedCollection):
    pass


class DerivedInvolvedfunctionalchains(EDerivedCollection):
    pass


@abstract
class AbstractCapability(Structure, InvolverElement, AbstractFunctionalChainContainer):

    preCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    postCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    ownedScenarios = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    incomingCapabilityAllocation = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedIncomingcapabilityallocation)
    outgoingCapabilityAllocation = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingcapabilityallocation)
    extends = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    extending = EReference(ordered=True, unique=True, containment=False,
                           derived=True, upper=-1, transient=True, derived_class=DerivedExtending)
    abstractCapabilityExtensionPoints = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    superGeneralizations = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    subGeneralizations = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedSubgeneralizations)
    includes = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    including = EReference(ordered=True, unique=True, containment=False,
                           derived=True, upper=-1, transient=True, derived_class=DerivedIncluding)
    super = EReference(ordered=True, unique=True, containment=False, derived=True,
                       upper=-1, transient=True, derived_class=DerivedSuper)
    sub = EReference(ordered=True, unique=True, containment=False, derived=True,
                     upper=-1, transient=True, derived_class=DerivedSub)
    includedAbstractCapabilities = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedIncludedabstractcapabilities)
    includingAbstractCapabilities = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedIncludingabstractcapabilities)
    extendedAbstractCapabilities = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedExtendedabstractcapabilities)
    extendingAbstractCapabilities = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedExtendingabstractcapabilities)
    ownedFunctionalChainAbstractCapabilityInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedAbstractFunctionAbstractCapabilityInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    availableInStates = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)
    ownedAbstractCapabilityRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    involvedAbstractFunctions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedabstractfunctions)
    involvedFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedfunctionalchains)

    def __init__(self, *, preCondition=None, postCondition=None, ownedScenarios=None, incomingCapabilityAllocation=None, outgoingCapabilityAllocation=None, extends=None, extending=None, abstractCapabilityExtensionPoints=None, superGeneralizations=None, subGeneralizations=None, includes=None, including=None, super=None, sub=None, includedAbstractCapabilities=None, includingAbstractCapabilities=None, extendedAbstractCapabilities=None, extendingAbstractCapabilities=None, ownedFunctionalChainAbstractCapabilityInvolvements=None, ownedAbstractFunctionAbstractCapabilityInvolvements=None, availableInStates=None, ownedAbstractCapabilityRealizations=None, involvedAbstractFunctions=None, involvedFunctionalChains=None, **kwargs):

        super().__init__(**kwargs)

        if preCondition is not None:
            self.preCondition = preCondition

        if postCondition is not None:
            self.postCondition = postCondition

        if ownedScenarios:
            self.ownedScenarios.extend(ownedScenarios)

        if incomingCapabilityAllocation:
            self.incomingCapabilityAllocation.extend(incomingCapabilityAllocation)

        if outgoingCapabilityAllocation:
            self.outgoingCapabilityAllocation.extend(outgoingCapabilityAllocation)

        if extends:
            self.extends.extend(extends)

        if extending:
            self.extending.extend(extending)

        if abstractCapabilityExtensionPoints:
            self.abstractCapabilityExtensionPoints.extend(abstractCapabilityExtensionPoints)

        if superGeneralizations:
            self.superGeneralizations.extend(superGeneralizations)

        if subGeneralizations:
            self.subGeneralizations.extend(subGeneralizations)

        if includes:
            self.includes.extend(includes)

        if including:
            self.including.extend(including)

        if super:
            self.super.extend(super)

        if sub:
            self.sub.extend(sub)

        if includedAbstractCapabilities:
            self.includedAbstractCapabilities.extend(includedAbstractCapabilities)

        if includingAbstractCapabilities:
            self.includingAbstractCapabilities.extend(includingAbstractCapabilities)

        if extendedAbstractCapabilities:
            self.extendedAbstractCapabilities.extend(extendedAbstractCapabilities)

        if extendingAbstractCapabilities:
            self.extendingAbstractCapabilities.extend(extendingAbstractCapabilities)

        if ownedFunctionalChainAbstractCapabilityInvolvements:
            self.ownedFunctionalChainAbstractCapabilityInvolvements.extend(
                ownedFunctionalChainAbstractCapabilityInvolvements)

        if ownedAbstractFunctionAbstractCapabilityInvolvements:
            self.ownedAbstractFunctionAbstractCapabilityInvolvements.extend(
                ownedAbstractFunctionAbstractCapabilityInvolvements)

        if availableInStates:
            self.availableInStates.extend(availableInStates)

        if ownedAbstractCapabilityRealizations:
            self.ownedAbstractCapabilityRealizations.extend(ownedAbstractCapabilityRealizations)

        if involvedAbstractFunctions:
            self.involvedAbstractFunctions.extend(involvedAbstractFunctions)

        if involvedFunctionalChains:
            self.involvedFunctionalChains.extend(involvedFunctionalChains)

print('interaction.interaction loaded')
