"""Definition of meta model 'capellacommon'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pycapella2.behavior import AbstractBehavior, AbstractEvent
from pycapella2.capellacore import Allocation, CapellaElement, InvolvedElement, Involvement, NamedElement, Relationship, Structure, Trace
from pycapella2.modellingcore import IState


name = 'capellacommon'
nsURI = 'http://www.polarsys.org/capella/core/common/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.capellacommon'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
TransitionKind = EEnum('TransitionKind', literals=['internal', 'local', 'external'])

TimeEventKind = EEnum('TimeEventKind', literals=['AT', 'AFTER'])

ChangeEventKind = EEnum('ChangeEventKind', literals=['WHEN'])


class DerivedCapabilityrealizationinvolvements(EDerivedCollection):
    pass


class DerivedInvolvingcapabilityrealizations(EDerivedCollection):
    pass


@abstract
class CapabilityRealizationInvolvedElement(InvolvedElement):

    capabilityRealizationInvolvements = EReference(ordered=True, unique=True, containment=False,
                                                   derived=True, upper=-1, transient=True, derived_class=DerivedCapabilityrealizationinvolvements)
    involvingCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilityrealizations)

    def __init__(self, *, capabilityRealizationInvolvements=None, involvingCapabilityRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if capabilityRealizationInvolvements:
            self.capabilityRealizationInvolvements.extend(capabilityRealizationInvolvements)

        if involvingCapabilityRealizations:
            self.involvingCapabilityRealizations.extend(involvingCapabilityRealizations)


class StateMachine(CapellaElement, AbstractBehavior):

    ownedRegions = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConnectionPoints = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedRegions=None, ownedConnectionPoints=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRegions:
            self.ownedRegions.extend(ownedRegions)

        if ownedConnectionPoints:
            self.ownedConnectionPoints.extend(ownedConnectionPoints)


class Region(NamedElement):

    ownedStates = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedTransitions = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    involvedStates = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)

    def __init__(self, *, ownedStates=None, ownedTransitions=None, involvedStates=None, **kwargs):

        super().__init__(**kwargs)

        if ownedStates:
            self.ownedStates.extend(ownedStates)

        if ownedTransitions:
            self.ownedTransitions.extend(ownedTransitions)

        if involvedStates:
            self.involvedStates.extend(involvedStates)


class CapabilityRealizationInvolvement(Involvement):

    _involvedCapabilityRealizationInvolvedElement = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='involvedCapabilityRealizationInvolvedElement', transient=True)

    @property
    def involvedCapabilityRealizationInvolvedElement(self):
        raise NotImplementedError(
            'Missing implementation for involvedCapabilityRealizationInvolvedElement')

    def __init__(self, *, involvedCapabilityRealizationInvolvedElement=None, **kwargs):

        super().__init__(**kwargs)

        if involvedCapabilityRealizationInvolvedElement is not None:
            self.involvedCapabilityRealizationInvolvedElement = involvedCapabilityRealizationInvolvedElement


@abstract
class AbstractCapabilityPkg(Structure):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedRealizedabstractstates(EDerivedCollection):
    pass


class DerivedRealizingabstractstates(EDerivedCollection):
    pass


class DerivedOutgoing(EDerivedCollection):
    pass


class DerivedIncoming(EDerivedCollection):
    pass


class DerivedInvolverregions(EDerivedCollection):
    pass


@abstract
class AbstractState(NamedElement, IState):

    ownedAbstractStateRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedAbstractStates = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizedabstractstates)
    realizingAbstractStates = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedRealizingabstractstates)
    outgoing = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedOutgoing)
    incoming = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedIncoming)
    involverRegions = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedInvolverregions)

    def __init__(self, *, ownedAbstractStateRealizations=None, realizedAbstractStates=None, realizingAbstractStates=None, outgoing=None, incoming=None, involverRegions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedAbstractStateRealizations:
            self.ownedAbstractStateRealizations.extend(ownedAbstractStateRealizations)

        if realizedAbstractStates:
            self.realizedAbstractStates.extend(realizedAbstractStates)

        if realizingAbstractStates:
            self.realizingAbstractStates.extend(realizingAbstractStates)

        if outgoing:
            self.outgoing.extend(outgoing)

        if incoming:
            self.incoming.extend(incoming)

        if involverRegions:
            self.involverRegions.extend(involverRegions)


class DerivedRealizedstatetransitions(EDerivedCollection):
    pass


class DerivedRealizingstatetransitions(EDerivedCollection):
    pass


class StateTransition(NamedElement, Relationship):

    kind = EAttribute(eType=TransitionKind, unique=True, derived=False, changeable=True)
    triggerDescription = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    guard = EReference(ordered=True, unique=True, containment=False, derived=False)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    effect = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    triggers = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownedStateTransitionRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedStateTransitions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedRealizedstatetransitions)
    realizingStateTransitions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizingstatetransitions)

    def __init__(self, *, kind=None, triggerDescription=None, guard=None, source=None, target=None, effect=None, triggers=None, ownedStateTransitionRealizations=None, realizedStateTransitions=None, realizingStateTransitions=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if triggerDescription is not None:
            self.triggerDescription = triggerDescription

        if guard is not None:
            self.guard = guard

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target

        if effect:
            self.effect.extend(effect)

        if triggers:
            self.triggers.extend(triggers)

        if ownedStateTransitionRealizations:
            self.ownedStateTransitionRealizations.extend(ownedStateTransitionRealizations)

        if realizedStateTransitions:
            self.realizedStateTransitions.extend(realizedStateTransitions)

        if realizingStateTransitions:
            self.realizingStateTransitions.extend(realizingStateTransitions)


class GenericTrace(Trace):

    keyValuePairs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    _source = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='source', transient=True)
    _target = EReference(ordered=True, unique=True, containment=False,
                         derived=True, name='target', transient=True)

    @property
    def source(self):
        raise NotImplementedError('Missing implementation for source')

    @property
    def target(self):
        raise NotImplementedError('Missing implementation for target')

    def __init__(self, *, keyValuePairs=None, source=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if keyValuePairs:
            self.keyValuePairs.extend(keyValuePairs)

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target


class DerivedAvailableabstractfunctions(EDerivedCollection):
    pass


class DerivedAvailablefunctionalchains(EDerivedCollection):
    pass


class DerivedAvailableabstractcapabilities(EDerivedCollection):
    pass


class State(AbstractState):

    ownedRegions = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConnectionPoints = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    availableAbstractFunctions = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedAvailableabstractfunctions)
    availableFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedAvailablefunctionalchains)
    availableAbstractCapabilities = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedAvailableabstractcapabilities)
    entry = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    doActivity = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    exit = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    stateInvariant = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedRegions=None, ownedConnectionPoints=None, availableAbstractFunctions=None, availableFunctionalChains=None, availableAbstractCapabilities=None, entry=None, doActivity=None, exit=None, stateInvariant=None, **kwargs):

        super().__init__(**kwargs)

        if ownedRegions:
            self.ownedRegions.extend(ownedRegions)

        if ownedConnectionPoints:
            self.ownedConnectionPoints.extend(ownedConnectionPoints)

        if availableAbstractFunctions:
            self.availableAbstractFunctions.extend(availableAbstractFunctions)

        if availableFunctionalChains:
            self.availableFunctionalChains.extend(availableFunctionalChains)

        if availableAbstractCapabilities:
            self.availableAbstractCapabilities.extend(availableAbstractCapabilities)

        if entry:
            self.entry.extend(entry)

        if doActivity:
            self.doActivity.extend(doActivity)

        if exit:
            self.exit.extend(exit)

        if stateInvariant is not None:
            self.stateInvariant = stateInvariant


@abstract
class Pseudostate(AbstractState):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class AbstractStateRealization(Allocation):

    _realizedAbstractState = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedAbstractState', transient=True)
    _realizingAbstractState = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingAbstractState', transient=True)

    @property
    def realizedAbstractState(self):
        raise NotImplementedError('Missing implementation for realizedAbstractState')

    @property
    def realizingAbstractState(self):
        raise NotImplementedError('Missing implementation for realizingAbstractState')

    def __init__(self, *, realizedAbstractState=None, realizingAbstractState=None, **kwargs):

        super().__init__(**kwargs)

        if realizedAbstractState is not None:
            self.realizedAbstractState = realizedAbstractState

        if realizingAbstractState is not None:
            self.realizingAbstractState = realizingAbstractState


class StateTransitionRealization(Allocation):

    _realizedStateTransition = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedStateTransition', transient=True)
    _realizingStateTransition = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingStateTransition', transient=True)

    @property
    def realizedStateTransition(self):
        raise NotImplementedError('Missing implementation for realizedStateTransition')

    @property
    def realizingStateTransition(self):
        raise NotImplementedError('Missing implementation for realizingStateTransition')

    def __init__(self, *, realizedStateTransition=None, realizingStateTransition=None, **kwargs):

        super().__init__(**kwargs)

        if realizedStateTransition is not None:
            self.realizedStateTransition = realizedStateTransition

        if realizingStateTransition is not None:
            self.realizingStateTransition = realizingStateTransition


class StateEventRealization(Allocation):

    _realizedEvent = EReference(ordered=True, unique=True, containment=False,
                                derived=True, name='realizedEvent', transient=True)
    _realizingEvent = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, name='realizingEvent', transient=True)

    @property
    def realizedEvent(self):
        raise NotImplementedError('Missing implementation for realizedEvent')

    @property
    def realizingEvent(self):
        raise NotImplementedError('Missing implementation for realizingEvent')

    def __init__(self, *, realizedEvent=None, realizingEvent=None, **kwargs):

        super().__init__(**kwargs)

        if realizedEvent is not None:
            self.realizedEvent = realizedEvent

        if realizingEvent is not None:
            self.realizingEvent = realizingEvent


@abstract
class StateEvent(NamedElement, AbstractEvent):

    expression = EReference(ordered=True, unique=True, containment=False, derived=False)
    ownedStateEventRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, expression=None, ownedStateEventRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if expression is not None:
            self.expression = expression

        if ownedStateEventRealizations:
            self.ownedStateEventRealizations.extend(ownedStateEventRealizations)


class TransfoLink(GenericTrace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class JustificationLink(GenericTrace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Mode(State):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FinalState(State):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class InitialPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class JoinPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ForkPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ChoicePseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TerminatePseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ShallowHistoryPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DeepHistoryPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class EntryPointPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ExitPointPseudoState(Pseudostate):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ChangeEvent(StateEvent):

    kind = EAttribute(eType=ChangeEventKind, unique=True, derived=False, changeable=True)

    def __init__(self, *, kind=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind


class TimeEvent(StateEvent):

    kind = EAttribute(eType=TimeEventKind, unique=True, derived=False, changeable=True)

    def __init__(self, *, kind=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind
