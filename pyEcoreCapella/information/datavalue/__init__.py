print('datavalue.__init__.py loading')
from pyecore.resources import global_registry
from .datavalue import getEClassifier, eClassifiers
from .datavalue import name, nsURI, nsPrefix, eClass
from .datavalue import AbstractBooleanValue, AbstractComplexValue, AbstractEnumerationValue, AbstractExpressionValue, AbstractStringValue, BinaryExpression, BinaryOperator, BooleanReference, ComplexValue, ComplexValueReference, DataValue, DataValueContainer, EnumerationLiteral, EnumerationReference, LiteralBooleanValue, LiteralNumericValue, LiteralStringValue, NumericReference, NumericValue, OpaqueExpression, StringReference, UnaryExpression, UnaryOperator, ValuePart
from . import datavalue
from .. import information


__all__ = ['AbstractBooleanValue', 'AbstractComplexValue', 'AbstractEnumerationValue', 'AbstractExpressionValue', 'AbstractStringValue', 'BinaryExpression', 'BinaryOperator', 'BooleanReference', 'ComplexValue', 'ComplexValueReference', 'DataValue',
           'DataValueContainer', 'EnumerationLiteral', 'EnumerationReference', 'LiteralBooleanValue', 'LiteralNumericValue', 'LiteralStringValue', 'NumericReference', 'NumericValue', 'OpaqueExpression', 'StringReference', 'UnaryExpression', 'UnaryOperator', 'ValuePart']

eSubpackages = []
eSuperPackage = information
datavalue.eSubpackages = eSubpackages
datavalue.eSuperPackage = eSuperPackage

otherClassifiers = [BinaryOperator, UnaryOperator]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [datavalue] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('datavalue.__init__.py loaded')
