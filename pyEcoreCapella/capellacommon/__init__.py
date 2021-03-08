
from .capellacommon import getEClassifier, eClassifiers
from .capellacommon import name, nsURI, nsPrefix, eClass
from .capellacommon import AbstractCapabilityPkg, GenericTrace, TransfoLink, JustificationLink, CapabilityRealizationInvolvement, CapabilityRealizationInvolvedElement, StateMachine, Region, State, Mode, FinalState, AbstractState, StateTransition, Pseudostate, InitialPseudoState, JoinPseudoState, ForkPseudoState, ChoicePseudoState, TerminatePseudoState, AbstractStateRealization, StateTransitionRealization, TransitionKind, ShallowHistoryPseudoState, DeepHistoryPseudoState, EntryPointPseudoState, ExitPointPseudoState, StateEventRealization, StateEvent, ChangeEvent, TimeEvent, TimeEventKind, ChangeEventKind

from modellingcore import TraceableElement, AbstractConstraint, AbstractParameter, IState, AbstractParameterSet, AbstractTrace, AbstractTypedElement, AbstractInformationFlow, ModelElement, AbstractConstraint, TraceableElement
from capellacore import EnumerationPropertyLiteral, Trace, Constraint, InvolverElement, AbstractPropertyValue, InvolvedElement, EnumerationPropertyType, KeyValue, NamingRule, Involvement, PropertyValuePkg, PropertyValueGroup
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from la import CapabilityRealization
from fa import FunctionalChain, AbstractFunction
from interaction import AbstractCapability
from behavior import AbstractEvent

from . import capellacommon

__all__ = ['AbstractCapabilityPkg', 'GenericTrace', 'TransfoLink', 'JustificationLink', 'CapabilityRealizationInvolvement', 'CapabilityRealizationInvolvedElement', 'StateMachine', 'Region', 'State', 'Mode', 'FinalState', 'AbstractState', 'StateTransition', 'Pseudostate', 'InitialPseudoState', 'JoinPseudoState', 'ForkPseudoState',
           'ChoicePseudoState', 'TerminatePseudoState', 'AbstractStateRealization', 'StateTransitionRealization', 'TransitionKind', 'ShallowHistoryPseudoState', 'DeepHistoryPseudoState', 'EntryPointPseudoState', 'ExitPointPseudoState', 'StateEventRealization', 'StateEvent', 'ChangeEvent', 'TimeEvent', 'TimeEventKind', 'ChangeEventKind']

eSubpackages = []
eSuperPackage = None
capellacommon.eSubpackages = eSubpackages
capellacommon.eSuperPackage = eSuperPackage

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

otherClassifiers = [TransitionKind, TimeEventKind, ChangeEventKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
