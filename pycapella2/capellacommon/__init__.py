#print('capellacommon.__init__.py loading')
from pyecore.resources import global_registry
from .capellacommon import getEClassifier, eClassifiers
from .capellacommon import name, nsURI, nsPrefix, eClass
from .capellacommon import AbstractCapabilityPkg, AbstractState, AbstractStateRealization, CapabilityRealizationInvolvedElement, CapabilityRealizationInvolvement, ChangeEvent, ChangeEventKind, ChoicePseudoState, DeepHistoryPseudoState, EntryPointPseudoState, ExitPointPseudoState, FinalState, ForkPseudoState, GenericTrace, InitialPseudoState, JoinPseudoState, JustificationLink, Mode, Pseudostate, Region, ShallowHistoryPseudoState, State, StateEvent, StateEventRealization, StateMachine, StateTransition, StateTransitionRealization, TerminatePseudoState, TimeEvent, TimeEventKind, TransfoLink, TransitionKind
from . import capellacommon

__all__ = ['AbstractCapabilityPkg', 'AbstractState', 'AbstractStateRealization', 'CapabilityRealizationInvolvedElement', 'CapabilityRealizationInvolvement', 'ChangeEvent', 'ChangeEventKind', 'ChoicePseudoState', 'DeepHistoryPseudoState', 'EntryPointPseudoState', 'ExitPointPseudoState', 'FinalState', 'ForkPseudoState', 'GenericTrace',
           'InitialPseudoState', 'JoinPseudoState', 'JustificationLink', 'Mode', 'Pseudostate', 'Region', 'ShallowHistoryPseudoState', 'State', 'StateEvent', 'StateEventRealization', 'StateMachine', 'StateTransition', 'StateTransitionRealization', 'TerminatePseudoState', 'TimeEvent', 'TimeEventKind', 'TransfoLink', 'TransitionKind']

eSubpackages = []
eSuperPackage = None
capellacommon.eSubpackages = eSubpackages
capellacommon.eSuperPackage = eSuperPackage

otherClassifiers = [TransitionKind, TimeEventKind, ChangeEventKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [capellacommon] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('capellacommon.__init__.py loaded')
