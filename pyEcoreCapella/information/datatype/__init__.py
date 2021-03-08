
from .datatype import getEClassifier, eClassifiers
from .datatype import name, nsURI, nsPrefix, eClass
from .datatype import DataType, BooleanType, Enumeration, StringType, NumericType, PhysicalQuantity, NumericTypeKind

from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Trace, Generalization, AbstractPropertyValue, TypedElement, EnumerationPropertyType, NamingRule, PropertyValuePkg, PropertyValueGroup
from capellacommon import GenericTrace
from modellingcore import AbstractTrace, AbstractTypedElement, AbstractConstraint, ModelElement
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from information.datavalue import AbstractEnumerationValue, NumericValue, AbstractBooleanValue, AbstractStringValue, EnumerationLiteral, DataValue, LiteralBooleanValue
from information import InformationRealization, Unit

from . import datatype
from .. import information


__all__ = ['DataType', 'BooleanType', 'Enumeration', 'StringType',
           'NumericType', 'PhysicalQuantity', 'NumericTypeKind']

eSubpackages = []
eSuperPackage = information
datatype.eSubpackages = eSubpackages
datatype.eSuperPackage = eSuperPackage


otherClassifiers = [NumericTypeKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
