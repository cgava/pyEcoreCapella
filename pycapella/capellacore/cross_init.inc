
#print('capellacore.cross_init starting')


capellacore.CapellaElement.ownedPropertyValues.eType = capellacore.AbstractPropertyValue
capellacore.CapellaElement.ownedEnumerationPropertyTypes.eType = capellacore.EnumerationPropertyType
capellacore.CapellaElement.appliedPropertyValues.eType = capellacore.AbstractPropertyValue
capellacore.CapellaElement.ownedPropertyValueGroups.eType = capellacore.PropertyValueGroup
capellacore.CapellaElement.appliedPropertyValueGroups.eType = capellacore.PropertyValueGroup
capellacore.CapellaElement.status.eType = capellacore.EnumerationPropertyLiteral
capellacore.CapellaElement.features.eType = capellacore.EnumerationPropertyLiteral
capellacore.CapellaElement.appliedRequirements.eType = requirement.Requirement
capellacore.Namespace.ownedTraces.eType = capellacore.Trace
capellacore.Namespace.containedGenericTraces.eType = capellacommon.GenericTrace
capellacore.Namespace.containedRequirementsTraces.eType = requirement.RequirementsTrace
capellacore.Namespace.namingRules.eType = capellacore.NamingRule
capellacore.NamedRelationship.namingRules.eType = capellacore.NamingRule
capellacore.Structure.ownedPropertyValuePkgs.eType = capellacore.PropertyValuePkg
capellacore.AbstractModellingStructure.ownedArchitectures.eType = capellacore.ModellingArchitecture
capellacore.AbstractModellingStructure.ownedArchitecturePkgs.eType = capellacore.ModellingArchitecturePkg
capellacore.Type.typedElements.eType = capellacore.TypedElement
capellacore.TypedElement._type.eType = capellacore.Type
capellacore.ReuseLink.reused.eType = capellacore.ReuseableStructure
capellacore.ReuseLink.reuser.eType = capellacore.ReuserStructure
capellacore.ReuseableStructure.reuseLinks.eType = capellacore.ReuseLink
capellacore.ReuserStructure.reuseLinks.eType = capellacore.ReuseLink
capellacore.ReuserStructure.ownedReuseLinks.eType = capellacore.ReuseLink
capellacore.GeneralizableElement.ownedGeneralizations.eType = capellacore.Generalization
capellacore.GeneralizableElement.superGeneralizations.eType = capellacore.Generalization
capellacore.GeneralizableElement.subGeneralizations.eType = capellacore.Generalization
capellacore.Classifier.ownedFeatures.eType = capellacore.Feature
capellacore.Classifier.containedProperties.eType = information.Property
capellacore.GeneralClass.containedOperations.eType = information.Operation
capellacore.GeneralClass.nestedGeneralClasses.eType = capellacore.GeneralClass
capellacore.Generalization.super_.eType = capellacore.GeneralizableElement
capellacore.Generalization.sub.eType = capellacore.GeneralizableElement
capellacore.AbstractExchangeItemPkg.ownedExchangeItems.eType = information.ExchangeItem
capellacore.Involvement._involver.eType = capellacore.InvolverElement
capellacore.Involvement.involved.eType = capellacore.InvolvedElement
capellacore.InvolverElement.involvedInvolvements.eType = capellacore.Involvement
capellacore.InvolvedElement.involvingInvolvements.eType = capellacore.Involvement
capellacore.AbstractPropertyValue.involvedElements.eType = capellacore.CapellaElement
capellacore.AbstractPropertyValue.valuedElements.eType = capellacore.CapellaElement
capellacore.EnumerationPropertyValue.type.eType = capellacore.EnumerationPropertyType
capellacore.EnumerationPropertyValue.value.eType = capellacore.EnumerationPropertyLiteral
capellacore.EnumerationPropertyType.ownedLiterals.eType = capellacore.EnumerationPropertyLiteral
capellacore.PropertyValueGroup.valuedElements.eType = capellacore.CapellaElement
capellacore.GeneralizableElement.super_.eType = capellacore.GeneralizableElement
capellacore.GeneralizableElement.sub.eType = capellacore.GeneralizableElement
capellacore.GeneralizableElement.sub.eOpposite = capellacore.GeneralizableElement.super_

#print('capellacore.cross_init done')
