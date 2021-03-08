
from .behavior import getEClassifier, eClassifiers
from .behavior import name, nsURI, nsPrefix, eClass
from .behavior import AbstractBehavior, AbstractSignal, AbstractEvent, AbstractTimeEvent, AbstractMessageEvent, AbstractSignalEvent, TimeExpression

from modellingcore import AbstractConstraint, AbstractParameter, AbstractType, AbstractNamedElement, AbstractTypedElement, ModelElement, ValueSpecification, AbstractParameterSet
from emde import ElementExtension

from . import behavior

__all__ = ['AbstractBehavior', 'AbstractSignal', 'AbstractEvent', 'AbstractTimeEvent',
           'AbstractMessageEvent', 'AbstractSignalEvent', 'TimeExpression']

eSubpackages = []
eSuperPackage = None
behavior.eSubpackages = eSubpackages
behavior.eSuperPackage = eSuperPackage

AbstractBehavior.ownedParameterSet.eType = AbstractParameterSet
AbstractBehavior.ownedParameter.eType = AbstractParameter
AbstractTimeEvent.when.eType = TimeExpression
AbstractSignalEvent.signal.eType = AbstractSignal
TimeExpression.observations.eType = AbstractNamedElement
TimeExpression.expression.eType = ValueSpecification

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
