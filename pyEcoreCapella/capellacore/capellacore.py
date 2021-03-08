print('capellacore.capellacore loading')
"""Definition of meta model 'capellacore'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from emde import Element, ExtensibleElement
from modellingcore import AbstractConstraint, AbstractNamedElement, AbstractNamedElement, AbstractRelationship, AbstractTrace, AbstractType, AbstractTypedElement, FinalizableElement, ModelElement, PublishableElement, TraceableElement, TraceableElement


name = 'capellacore'
nsURI = 'http://www.polarsys.org/capella/core/core/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.capellacore'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
VisibilityKind = EEnum('VisibilityKind', literals=[
                       'UNSET', 'PUBLIC', 'PROTECTED', 'PRIVATE', 'PACKAGE'])


class DerivedAppliedrequirements(EDerivedCollection):
    pass


@abstract
class CapellaElement(TraceableElement, PublishableElement):

    summary = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    review = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    ownedPropertyValues = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    ownedEnumerationPropertyTypes = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    appliedPropertyValues = EReference(ordered=True, unique=True,
                                       containment=False, derived=False, upper=-1)
    ownedPropertyValueGroups = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    appliedPropertyValueGroups = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    status = EReference(ordered=True, unique=True, containment=False, derived=False)
    features = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    appliedRequirements = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedAppliedrequirements)

    def __init__(self, *, summary=None, description=None, review=None, ownedPropertyValues=None, ownedEnumerationPropertyTypes=None, appliedPropertyValues=None, ownedPropertyValueGroups=None, appliedPropertyValueGroups=None, status=None, features=None, appliedRequirements=None, **kwargs):

        super().__init__(**kwargs)

        if summary is not None:
            self.summary = summary

        if description is not None:
            self.description = description

        if review is not None:
            self.review = review

        if ownedPropertyValues:
            self.ownedPropertyValues.extend(ownedPropertyValues)

        if ownedEnumerationPropertyTypes:
            self.ownedEnumerationPropertyTypes.extend(ownedEnumerationPropertyTypes)

        if appliedPropertyValues:
            self.appliedPropertyValues.extend(appliedPropertyValues)

        if ownedPropertyValueGroups:
            self.ownedPropertyValueGroups.extend(ownedPropertyValueGroups)

        if appliedPropertyValueGroups:
            self.appliedPropertyValueGroups.extend(appliedPropertyValueGroups)

        if status is not None:
            self.status = status

        if features:
            self.features.extend(features)

        if appliedRequirements:
            self.appliedRequirements.extend(appliedRequirements)


@abstract
class AbstractAnnotation(CapellaElement):

    content = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, content=None, **kwargs):

        super().__init__(**kwargs)

        if content is not None:
            self.content = content


class KeyValue(CapellaElement):

    key = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, key=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


class DerivedInvolvedinvolvements(EDerivedCollection):
    pass


@abstract
class InvolverElement(CapellaElement):

    involvedInvolvements = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedinvolvements)

    def __init__(self, *, involvedInvolvements=None, **kwargs):

        super().__init__(**kwargs)

        if involvedInvolvements:
            self.involvedInvolvements.extend(involvedInvolvements)


class DerivedInvolvinginvolvements(EDerivedCollection):
    pass


@abstract
class InvolvedElement(CapellaElement):

    involvingInvolvements = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedInvolvinginvolvements)

    def __init__(self, *, involvingInvolvements=None, **kwargs):

        super().__init__(**kwargs)

        if involvingInvolvements:
            self.involvingInvolvements.extend(involvingInvolvements)


@abstract
class NamedElement(AbstractNamedElement, CapellaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Relationship(AbstractRelationship, CapellaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class NamingRule(AbstractAnnotation):

    targetType = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, targetType=None, **kwargs):

        super().__init__(**kwargs)

        if targetType is not None:
            self.targetType = targetType


class DerivedContainedgenerictraces(EDerivedCollection):
    pass


class DerivedContainedrequirementstraces(EDerivedCollection):
    pass


@abstract
class Namespace(NamedElement):

    ownedTraces = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    containedGenericTraces = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedContainedgenerictraces)
    containedRequirementsTraces = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedContainedrequirementstraces)
    namingRules = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedTraces=None, containedGenericTraces=None, containedRequirementsTraces=None, namingRules=None, **kwargs):

        super().__init__(**kwargs)

        if ownedTraces:
            self.ownedTraces.extend(ownedTraces)

        if containedGenericTraces:
            self.containedGenericTraces.extend(containedGenericTraces)

        if containedRequirementsTraces:
            self.containedRequirementsTraces.extend(containedRequirementsTraces)

        if namingRules:
            self.namingRules.extend(namingRules)


class ReuseLink(Relationship):

    reused = EReference(ordered=True, unique=True, containment=False, derived=False)
    reuser = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, reused=None, reuser=None, **kwargs):

        super().__init__(**kwargs)

        if reused is not None:
            self.reused = reused

        if reuser is not None:
            self.reuser = reuser


class Generalization(Relationship):

    super = EReference(ordered=True, unique=True, containment=False, derived=False)
    sub = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, super=None, sub=None, **kwargs):

        super().__init__(**kwargs)

        if super is not None:
            self.super = super

        if sub is not None:
            self.sub = sub


@abstract
class Feature(NamedElement):

    isAbstract = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isStatic = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)

    def __init__(self, *, isAbstract=None, isStatic=None, visibility=None, **kwargs):

        super().__init__(**kwargs)

        if isAbstract is not None:
            self.isAbstract = isAbstract

        if isStatic is not None:
            self.isStatic = isStatic

        if visibility is not None:
            self.visibility = visibility


@abstract
class Involvement(Relationship):

    _involver = EReference(ordered=True, unique=True, containment=False,
                           derived=True, name='involver', transient=True)
    involved = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def involver(self):
        raise NotImplementedError('Missing implementation for involver')

    def __init__(self, *, involver=None, involved=None, **kwargs):

        super().__init__(**kwargs)

        if involver is not None:
            self.involver = involver

        if involved is not None:
            self.involved = involved


class DerivedValuedelements(EDerivedCollection):
    pass


@abstract
class AbstractPropertyValue(NamedElement):

    involvedElements = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    valuedElements = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedValuedelements)

    def __init__(self, *, involvedElements=None, valuedElements=None, **kwargs):

        super().__init__(**kwargs)

        if involvedElements:
            self.involvedElements.extend(involvedElements)

        if valuedElements:
            self.valuedElements.extend(valuedElements)


class EnumerationPropertyType(NamedElement):

    ownedLiterals = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedLiterals=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLiterals:
            self.ownedLiterals.extend(ownedLiterals)


class EnumerationPropertyLiteral(NamedElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Structure(Namespace):

    ownedPropertyValuePkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedPropertyValuePkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPropertyValuePkgs:
            self.ownedPropertyValuePkgs.extend(ownedPropertyValuePkgs)


class Constraint(NamedElement, AbstractConstraint):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class StringPropertyValue(AbstractPropertyValue):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class IntegerPropertyValue(AbstractPropertyValue):

    value = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BooleanPropertyValue(AbstractPropertyValue):

    value = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class FloatPropertyValue(AbstractPropertyValue):

    value = EAttribute(eType=EFloat, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class EnumerationPropertyValue(AbstractPropertyValue):

    type = EReference(ordered=True, unique=True, containment=False, derived=False)
    value = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, type=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if value is not None:
            self.value = value


class DerivedValuedelements(EDerivedCollection):
    pass


class PropertyValueGroup(Namespace):

    valuedElements = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedValuedelements)

    def __init__(self, *, valuedElements=None, **kwargs):

        super().__init__(**kwargs)

        if valuedElements:
            self.valuedElements.extend(valuedElements)


@abstract
class NamedRelationship(Relationship, NamedElement):

    namingRules = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, namingRules=None, **kwargs):

        super().__init__(**kwargs)

        if namingRules:
            self.namingRules.extend(namingRules)


@abstract
class ModellingArchitecture(Structure):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ModellingArchitecturePkg(Structure):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class TypedElement(AbstractTypedElement, NamedElement):

    _type = EReference(ordered=True, unique=True, containment=False,
                       derived=True, name='type', transient=True)

    @property
    def type(self):
        raise NotImplementedError('Missing implementation for type')

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


@abstract
class Trace(Relationship, AbstractTrace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ReuseableStructure(Structure):

    reuseLinks = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, reuseLinks=None, **kwargs):

        super().__init__(**kwargs)

        if reuseLinks:
            self.reuseLinks.extend(reuseLinks)


@abstract
class ReuserStructure(Structure):

    reuseLinks = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownedReuseLinks = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, reuseLinks=None, ownedReuseLinks=None, **kwargs):

        super().__init__(**kwargs)

        if reuseLinks:
            self.reuseLinks.extend(reuseLinks)

        if ownedReuseLinks:
            self.ownedReuseLinks.extend(ownedReuseLinks)


@abstract
class AbstractExchangeItemPkg(Structure):

    ownedExchangeItems = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedExchangeItems=None, **kwargs):

        super().__init__(**kwargs)

        if ownedExchangeItems:
            self.ownedExchangeItems.extend(ownedExchangeItems)


@abstract
class Allocation(Relationship, AbstractTrace):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PropertyValuePkg(Structure):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractDependenciesPkg(Structure):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractModellingStructure(ReuserStructure):

    ownedArchitectures = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedArchitecturePkgs = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedArchitectures=None, ownedArchitecturePkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedArchitectures:
            self.ownedArchitectures.extend(ownedArchitectures)

        if ownedArchitecturePkgs:
            self.ownedArchitecturePkgs.extend(ownedArchitecturePkgs)


class DerivedTypedelements(EDerivedCollection):
    pass


@abstract
class Type(AbstractType, Namespace):

    typedElements = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedTypedelements)

    def __init__(self, *, typedElements=None, **kwargs):

        super().__init__(**kwargs)

        if typedElements:
            self.typedElements.extend(typedElements)


@abstract
class ModellingBlock(Type):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedSupergeneralizations(EDerivedCollection):
    pass


class DerivedSubgeneralizations(EDerivedCollection):
    pass


class DerivedSuper(EDerivedCollection):
    pass


class DerivedSub(EDerivedCollection):
    pass


@abstract
class GeneralizableElement(Type):

    abstract = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedGeneralizations = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    superGeneralizations = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedSupergeneralizations)
    subGeneralizations = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedSubgeneralizations)
    super = EReference(ordered=True, unique=True, containment=False, derived=True,
                       upper=-1, transient=True, derived_class=DerivedSuper)
    sub = EReference(ordered=True, unique=True, containment=False, derived=True,
                     upper=-1, transient=True, derived_class=DerivedSub)

    def __init__(self, *, abstract=None, ownedGeneralizations=None, superGeneralizations=None, subGeneralizations=None, super=None, sub=None, **kwargs):

        super().__init__(**kwargs)

        if abstract is not None:
            self.abstract = abstract

        if ownedGeneralizations:
            self.ownedGeneralizations.extend(ownedGeneralizations)

        if superGeneralizations:
            self.superGeneralizations.extend(superGeneralizations)

        if subGeneralizations:
            self.subGeneralizations.extend(subGeneralizations)

        if super:
            self.super.extend(super)

        if sub:
            self.sub.extend(sub)


class DerivedContainedproperties(EDerivedCollection):
    pass


@abstract
class Classifier(GeneralizableElement):

    ownedFeatures = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    containedProperties = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedContainedproperties)

    def __init__(self, *, ownedFeatures=None, containedProperties=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFeatures:
            self.ownedFeatures.extend(ownedFeatures)

        if containedProperties:
            self.containedProperties.extend(containedProperties)


class DerivedContainedoperations(EDerivedCollection):
    pass


@abstract
class GeneralClass(Classifier, FinalizableElement):

    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)
    containedOperations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedContainedoperations)
    nestedGeneralClasses = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)

    def __init__(self, *, visibility=None, containedOperations=None, nestedGeneralClasses=None, **kwargs):

        super().__init__(**kwargs)

        if visibility is not None:
            self.visibility = visibility

        if containedOperations:
            self.containedOperations.extend(containedOperations)

        if nestedGeneralClasses:
            self.nestedGeneralClasses.extend(nestedGeneralClasses)

print('capellacore.capellacore loaded')
