"""Definition of meta model 'behavior'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from modellingcore import AbstractNamedElement, AbstractType, ValueSpecification


name = 'behavior'
nsURI = 'http://www.polarsys.org/capella/common/behavior/1.4.0'
nsPrefix = 'org.polarsys.capella.common.data.behavior'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class AbstractBehavior(AbstractNamedElement):

    isControlOperator = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedParameterSet = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)
    ownedParameter = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)

    def __init__(self, *, isControlOperator=None, ownedParameterSet=None, ownedParameter=None, **kwargs):

        super().__init__(**kwargs)

        if isControlOperator is not None:
            self.isControlOperator = isControlOperator

        if ownedParameterSet:
            self.ownedParameterSet.extend(ownedParameterSet)

        if ownedParameter:
            self.ownedParameter.extend(ownedParameter)


@abstract
class AbstractSignal(AbstractType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractEvent(AbstractType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractTimeEvent(AbstractEvent):

    isRelative = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    when = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, isRelative=None, when=None, **kwargs):

        super().__init__(**kwargs)

        if isRelative is not None:
            self.isRelative = isRelative

        if when is not None:
            self.when = when


@abstract
class AbstractMessageEvent(AbstractEvent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class TimeExpression(ValueSpecification):

    observations = EReference(ordered=True, unique=True, containment=False, derived=False)
    expression = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, observations=None, expression=None, **kwargs):

        super().__init__(**kwargs)

        if observations is not None:
            self.observations = observations

        if expression is not None:
            self.expression = expression


@abstract
class AbstractSignalEvent(AbstractMessageEvent):

    signal = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, signal=None, **kwargs):

        super().__init__(**kwargs)

        if signal is not None:
            self.signal = signal
