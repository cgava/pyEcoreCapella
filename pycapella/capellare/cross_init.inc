
#print('re.cross_init starting')


ElementContainer.ownedElements.eType = CatalogElement
CatalogElementPkg.ownedElementPkgs.eType = CatalogElementPkg
RecCatalog.ownedCompliancyDefinitionPkg.eType = CompliancyDefinitionPkg
CatalogElementLink.source.eType = CatalogElement
CatalogElementLink.target.eType = EObject
CatalogElementLink.origin.eType = CatalogElementLink
CatalogElement.origin.eType = CatalogElement
CatalogElement.currentCompliancy.eType = CompliancyDefinition
CatalogElement.defaultReplicaCompliancy.eType = CompliancyDefinition
CatalogElement.ownedLinks.eType = CatalogElementLink
CatalogElement.referencedElements.eType = EObject
CatalogElement.replicatedElements.eType = CatalogElement
CompliancyDefinitionPkg.ownedDefinitions.eType = CompliancyDefinition

#print('re.cross_init done')
