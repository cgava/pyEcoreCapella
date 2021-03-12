#print('modellingcore.__init__.py loading')
from pyecore.resources import global_registry
from .modellingcore import getEClassifier, eClassifiers
from .modellingcore import name, nsURI, nsPrefix, eClass
from .modellingcore import AbstractConstraint, AbstractExchangeItem, AbstractInformationFlow, AbstractNamedElement, AbstractParameter, AbstractParameterSet, AbstractRelationship, AbstractTrace, AbstractType, AbstractTypedElement, FinalizableElement, InformationsExchanger, IState, ModelElement, ParameterEffectKind, PublishableElement, RateKind, TraceableElement, ValueSpecification
from . import modellingcore

__all__ = ['AbstractConstraint', 'AbstractExchangeItem', 'AbstractInformationFlow', 'AbstractNamedElement', 'AbstractParameter', 'AbstractParameterSet', 'AbstractRelationship', 'AbstractTrace', 'AbstractType',
           'AbstractTypedElement', 'FinalizableElement', 'InformationsExchanger', 'IState', 'ModelElement', 'ParameterEffectKind', 'PublishableElement', 'RateKind', 'TraceableElement', 'ValueSpecification']

eSubpackages = []
eSuperPackage = None
modellingcore.eSubpackages = eSubpackages
modellingcore.eSuperPackage = eSuperPackage

otherClassifiers = [ParameterEffectKind, RateKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [modellingcore] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('modellingcore.__init__.py loaded')
