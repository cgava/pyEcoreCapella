#print('interaction.__init__.py loading')
from pyecore.resources import global_registry
from .interaction import getEClassifier, eClassifiers
from .interaction import name, nsURI, nsPrefix, eClass
from .interaction import AbstractCapability, AbstractCapabilityExtend, AbstractCapabilityExtensionPoint, AbstractCapabilityGeneralization, AbstractCapabilityInclude, AbstractCapabilityRealization, AbstractEnd, AbstractFragment, AbstractFunctionAbstractCapabilityInvolvement, ArmTimerEvent, CancelTimerEvent, CombinedFragment, ConstraintDuration, CreationEvent, DestructionEvent, Event, EventReceiptOperation, EventSentOperation, Execution, ExecutionEnd, ExecutionEvent, FragmentEnd, FunctionalChainAbstractCapabilityInvolvement, Gate, InstanceRole, InteractionFragment, InteractionOperand, InteractionOperatorKind, InteractionState, InteractionUse, MergeLink, MessageEnd, MessageKind, RefinementLink, Scenario, ScenarioKind, ScenarioRealization, SequenceMessage, SequenceMessageValuation, StateFragment, TimeLapse
from . import interaction

__all__ = ['AbstractCapability', 'AbstractCapabilityExtend', 'AbstractCapabilityExtensionPoint', 'AbstractCapabilityGeneralization', 'AbstractCapabilityInclude', 'AbstractCapabilityRealization', 'AbstractEnd', 'AbstractFragment', 'AbstractFunctionAbstractCapabilityInvolvement', 'ArmTimerEvent', 'CancelTimerEvent', 'CombinedFragment', 'ConstraintDuration', 'CreationEvent', 'DestructionEvent', 'Event', 'EventReceiptOperation', 'EventSentOperation',
           'Execution', 'ExecutionEnd', 'ExecutionEvent', 'FragmentEnd', 'FunctionalChainAbstractCapabilityInvolvement', 'Gate', 'InstanceRole', 'InteractionFragment', 'InteractionOperand', 'InteractionOperatorKind', 'InteractionState', 'InteractionUse', 'MergeLink', 'MessageEnd', 'MessageKind', 'RefinementLink', 'Scenario', 'ScenarioKind', 'ScenarioRealization', 'SequenceMessage', 'SequenceMessageValuation', 'StateFragment', 'TimeLapse']

eSubpackages = []
eSuperPackage = None
interaction.eSubpackages = eSubpackages
interaction.eSuperPackage = eSuperPackage

otherClassifiers = [MessageKind, ScenarioKind, InteractionOperatorKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [interaction] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('interaction.__init__.py loaded')
