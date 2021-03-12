print('capellacore.__init__.py loading')
from pyecore.resources import global_registry
from .capellacore import getEClassifier, eClassifiers
from .capellacore import name, nsURI, nsPrefix, eClass
from .capellacore import AbstractAnnotation, AbstractDependenciesPkg, AbstractExchangeItemPkg, AbstractModellingStructure, AbstractPropertyValue, Allocation, BooleanPropertyValue, CapellaElement, Classifier, Constraint, EnumerationPropertyLiteral, EnumerationPropertyType, EnumerationPropertyValue, Feature, FloatPropertyValue, GeneralClass, GeneralizableElement, Generalization, IntegerPropertyValue, InvolvedElement, Involvement, InvolverElement, KeyValue, ModellingArchitecture, ModellingArchitecturePkg, ModellingBlock, NamedElement, NamedRelationship, Namespace, NamingRule, PropertyValueGroup, PropertyValuePkg, Relationship, ReuseableStructure, ReuseLink, ReuserStructure, StringPropertyValue, Structure, Trace, Type, TypedElement, VisibilityKind
from . import capellacore

__all__ = ['AbstractAnnotation', 'AbstractDependenciesPkg', 'AbstractExchangeItemPkg', 'AbstractModellingStructure', 'AbstractPropertyValue', 'Allocation', 'BooleanPropertyValue', 'CapellaElement', 'Classifier', 'Constraint', 'EnumerationPropertyLiteral', 'EnumerationPropertyType', 'EnumerationPropertyValue', 'Feature', 'FloatPropertyValue', 'GeneralClass', 'GeneralizableElement', 'Generalization',
           'IntegerPropertyValue', 'InvolvedElement', 'Involvement', 'InvolverElement', 'KeyValue', 'ModellingArchitecture', 'ModellingArchitecturePkg', 'ModellingBlock', 'NamedElement', 'NamedRelationship', 'Namespace', 'NamingRule', 'PropertyValueGroup', 'PropertyValuePkg', 'Relationship', 'ReuseableStructure', 'ReuseLink', 'ReuserStructure', 'StringPropertyValue', 'Structure', 'Trace', 'Type', 'TypedElement', 'VisibilityKind']

eSubpackages = []
eSuperPackage = None
capellacore.eSubpackages = eSubpackages
capellacore.eSuperPackage = eSuperPackage

otherClassifiers = [VisibilityKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [capellacore] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('capellacore.__init__.py loaded')
