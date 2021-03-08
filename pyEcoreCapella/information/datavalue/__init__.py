
from .datavalue import getEClassifier, eClassifiers
from .datavalue import name, nsURI, nsPrefix, eClass
from .datavalue import DataValue, DataValueContainer, AbstractBooleanValue, LiteralBooleanValue, BooleanReference, AbstractEnumerationValue, EnumerationLiteral, EnumerationReference, AbstractStringValue, LiteralStringValue, StringReference, NumericValue, LiteralNumericValue, NumericReference, AbstractComplexValue, ComplexValue, ComplexValueReference, ValuePart, AbstractExpressionValue, BinaryExpression, UnaryExpression, BinaryOperator, UnaryOperator, OpaqueExpression

from capellacore import EnumerationPropertyLiteral, Trace, AbstractPropertyValue, Type, Classifier, EnumerationPropertyType, NamingRule, PropertyValuePkg, PropertyValueGroup
from information.datatype import DataType, StringType, BooleanType, Enumeration, NumericType
from capellacommon import GenericTrace
from modellingcore import AbstractTrace, AbstractType, AbstractConstraint, ModelElement
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from information import Property, Unit

from . import datavalue
from .. import information


__all__ = ['DataValue', 'DataValueContainer', 'AbstractBooleanValue', 'LiteralBooleanValue', 'BooleanReference', 'AbstractEnumerationValue', 'EnumerationLiteral', 'EnumerationReference', 'AbstractStringValue', 'LiteralStringValue', 'StringReference',
           'NumericValue', 'LiteralNumericValue', 'NumericReference', 'AbstractComplexValue', 'ComplexValue', 'ComplexValueReference', 'ValuePart', 'AbstractExpressionValue', 'BinaryExpression', 'UnaryExpression', 'BinaryOperator', 'UnaryOperator', 'OpaqueExpression']

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
