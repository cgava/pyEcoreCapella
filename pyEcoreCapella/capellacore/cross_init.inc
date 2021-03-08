
#print('capellacore.cross_init starting')


CapellaElement.ownedPropertyValues.eType = AbstractPropertyValue
CapellaElement.ownedEnumerationPropertyTypes.eType = EnumerationPropertyType
CapellaElement.appliedPropertyValues.eType = AbstractPropertyValue
CapellaElement.ownedPropertyValueGroups.eType = PropertyValueGroup
CapellaElement.appliedPropertyValueGroups.eType = PropertyValueGroup
CapellaElement.status.eType = EnumerationPropertyLiteral
CapellaElement.features.eType = EnumerationPropertyLiteral
CapellaElement.appliedRequirements.eType = Requirement
Namespace.ownedTraces.eType = Trace
Namespace.containedGenericTraces.eType = GenericTrace
Namespace.containedRequirementsTraces.eType = RequirementsTrace
Namespace.namingRules.eType = NamingRule
NamedRelationship.namingRules.eType = NamingRule
Structure.ownedPropertyValuePkgs.eType = PropertyValuePkg
AbstractModellingStructure.ownedArchitectures.eType = ModellingArchitecture
AbstractModellingStructure.ownedArchitecturePkgs.eType = ModellingArchitecturePkg
Type.typedElements.eType = TypedElement
TypedElement._type.eType = Type
ReuseLink.reused.eType = ReuseableStructure
ReuseLink.reuser.eType = ReuserStructure
ReuseableStructure.reuseLinks.eType = ReuseLink
ReuserStructure.reuseLinks.eType = ReuseLink
ReuserStructure.ownedReuseLinks.eType = ReuseLink
GeneralizableElement.ownedGeneralizations.eType = Generalization
GeneralizableElement.superGeneralizations.eType = Generalization
GeneralizableElement.subGeneralizations.eType = Generalization
Classifier.ownedFeatures.eType = Feature
Classifier.containedProperties.eType = Property
GeneralClass.containedOperations.eType = Operation
GeneralClass.nestedGeneralClasses.eType = GeneralClass
Generalization.super.eType = GeneralizableElement
Generalization.sub.eType = GeneralizableElement
AbstractExchangeItemPkg.ownedExchangeItems.eType = ExchangeItem
Involvement._involver.eType = InvolverElement
Involvement.involved.eType = InvolvedElement
InvolverElement.involvedInvolvements.eType = Involvement
InvolvedElement.involvingInvolvements.eType = Involvement
AbstractPropertyValue.involvedElements.eType = CapellaElement
AbstractPropertyValue.valuedElements.eType = CapellaElement
EnumerationPropertyValue.type.eType = EnumerationPropertyType
EnumerationPropertyValue.value.eType = EnumerationPropertyLiteral
EnumerationPropertyType.ownedLiterals.eType = EnumerationPropertyLiteral
PropertyValueGroup.valuedElements.eType = CapellaElement
GeneralizableElement.super.eType = GeneralizableElement
GeneralizableElement.sub.eType = GeneralizableElement
GeneralizableElement.sub.eOpposite = GeneralizableElement.super

#print('capellacore.cross_init done')
