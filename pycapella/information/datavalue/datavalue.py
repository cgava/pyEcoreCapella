"""Definition of meta model 'datavalue'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import CapellaElement, NamedElement, Structure
from modellingcore import ValueSpecification


name = 'datavalue'
nsURI = 'http://www.polarsys.org/capella/core/information/datavalue/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.information.datavalue'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
BinaryOperator = EEnum('BinaryOperator', literals=[
                       'UNSET', 'ADD', 'MUL', 'SUB', 'DIV', 'POW', 'MIN', 'MAX', 'EQU', 'IOR', 'XOR', 'AND'])

UnaryOperator = EEnum('UnaryOperator', literals=['UNSET', 'NOT', 'POS', 'VAL', 'SUC', 'PRE'])


class ValuePart(CapellaElement):

    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)
    ownedValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, referencedProperty=None, ownedValue=None, **kwargs):

        super().__init__(**kwargs)

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty

        if ownedValue is not None:
            self.ownedValue = ownedValue


class OpaqueExpression(CapellaElement, ValueSpecification):

    bodies = EAttribute(eType=EString, unique=False, derived=False, changeable=True, upper=-1)
    languages = EAttribute(eType=EString, unique=True, derived=False, changeable=True, upper=-1)

    def __init__(self, *, bodies=None, languages=None, **kwargs):

        super().__init__(**kwargs)

        if bodies:
            self.bodies.extend(bodies)

        if languages:
            self.languages.extend(languages)


@abstract
class DataValueContainer(Structure):

    ownedDataValues = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedDataValues=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDataValues:
            self.ownedDataValues.extend(ownedDataValues)


@abstract
class DataValue(NamedElement, ValueSpecification):

    abstract = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    _type = EReference(ordered=True, unique=True, containment=False,
                       derived=True, name='type', transient=True)

    @property
    def type(self):
        raise NotImplementedError('Missing implementation for type')

    def __init__(self, *, abstract=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if abstract is not None:
            self.abstract = abstract

        if type is not None:
            self.type = type


@abstract
class AbstractBooleanValue(DataValue):

    _booleanType = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='booleanType', transient=True)

    @property
    def booleanType(self):
        raise NotImplementedError('Missing implementation for booleanType')

    def __init__(self, *, booleanType=None, **kwargs):

        super().__init__(**kwargs)

        if booleanType is not None:
            self.booleanType = booleanType


@abstract
class AbstractEnumerationValue(DataValue):

    _enumerationType = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='enumerationType', transient=True)

    @property
    def enumerationType(self):
        raise NotImplementedError('Missing implementation for enumerationType')

    def __init__(self, *, enumerationType=None, **kwargs):

        super().__init__(**kwargs)

        if enumerationType is not None:
            self.enumerationType = enumerationType


@abstract
class AbstractStringValue(DataValue):

    _stringType = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='stringType', transient=True)

    @property
    def stringType(self):
        raise NotImplementedError('Missing implementation for stringType')

    def __init__(self, *, stringType=None, **kwargs):

        super().__init__(**kwargs)

        if stringType is not None:
            self.stringType = stringType


@abstract
class NumericValue(DataValue):

    unit = EReference(ordered=True, unique=True, containment=False, derived=False)
    _numericType = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='numericType', transient=True)

    @property
    def numericType(self):
        raise NotImplementedError('Missing implementation for numericType')

    def __init__(self, *, unit=None, numericType=None, **kwargs):

        super().__init__(**kwargs)

        if unit is not None:
            self.unit = unit

        if numericType is not None:
            self.numericType = numericType


@abstract
class AbstractComplexValue(DataValue):

    _complexType = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='complexType', transient=True)

    @property
    def complexType(self):
        raise NotImplementedError('Missing implementation for complexType')

    def __init__(self, *, complexType=None, **kwargs):

        super().__init__(**kwargs)

        if complexType is not None:
            self.complexType = complexType


class LiteralBooleanValue(AbstractBooleanValue):

    value = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BooleanReference(AbstractBooleanValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


class EnumerationLiteral(AbstractEnumerationValue):

    domainValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, domainValue=None, **kwargs):

        super().__init__(**kwargs)

        if domainValue is not None:
            self.domainValue = domainValue


class EnumerationReference(AbstractEnumerationValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


class LiteralStringValue(AbstractStringValue):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class StringReference(AbstractStringValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


class LiteralNumericValue(NumericValue):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class NumericReference(NumericValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


class ComplexValue(AbstractComplexValue):

    ownedParts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedParts=None, **kwargs):

        super().__init__(**kwargs)

        if ownedParts:
            self.ownedParts.extend(ownedParts)


class ComplexValueReference(AbstractComplexValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


@abstract
class AbstractExpressionValue(AbstractBooleanValue, AbstractComplexValue, AbstractEnumerationValue, NumericValue, AbstractStringValue):

    _expression = EAttribute(eType=EString, unique=True, derived=True,
                             changeable=False, name='expression', transient=True)
    unparsedExpression = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    _expressionType = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, name='expressionType', transient=True)

    @property
    def expression(self):
        raise NotImplementedError('Missing implementation for expression')

    @property
    def expressionType(self):
        raise NotImplementedError('Missing implementation for expressionType')

    def __init__(self, *, expression=None, unparsedExpression=None, expressionType=None, **kwargs):

        super().__init__(**kwargs)

        if expression is not None:
            self.expression = expression

        if unparsedExpression is not None:
            self.unparsedExpression = unparsedExpression

        if expressionType is not None:
            self.expressionType = expressionType


class BinaryExpression(AbstractExpressionValue):

    operator = EAttribute(eType=BinaryOperator, unique=True, derived=False, changeable=True)
    ownedLeftOperand = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedRightOperand = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, operator=None, ownedLeftOperand=None, ownedRightOperand=None, **kwargs):

        super().__init__(**kwargs)

        if operator is not None:
            self.operator = operator

        if ownedLeftOperand is not None:
            self.ownedLeftOperand = ownedLeftOperand

        if ownedRightOperand is not None:
            self.ownedRightOperand = ownedRightOperand


class UnaryExpression(AbstractExpressionValue):

    operator = EAttribute(eType=UnaryOperator, unique=True, derived=False, changeable=True)
    ownedOperand = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, operator=None, ownedOperand=None, **kwargs):

        super().__init__(**kwargs)

        if operator is not None:
            self.operator = operator

        if ownedOperand is not None:
            self.ownedOperand = ownedOperand
