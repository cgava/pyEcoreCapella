
#print('re.cross_init starting')


re.ReElementContainer.ownedElements.eType = re.CatalogElement
re.CatalogElementPkg.ownedElementPkgs.eType = re.CatalogElementPkg
re.RecCatalog.ownedCompliancyDefinitionPkg.eType = re.CompliancyDefinitionPkg
re.CatalogElementLink.source.eType = re.CatalogElement
re.CatalogElementLink.target.eType = ecore.EObject
re.CatalogElementLink.origin.eType = re.CatalogElementLink
re.CatalogElement.origin.eType = re.CatalogElement
re.CatalogElement.currentCompliancy.eType = re.CompliancyDefinition
re.CatalogElement.defaultReplicaCompliancy.eType = re.CompliancyDefinition
re.CatalogElement.ownedLinks.eType = re.CatalogElementLink
re.CatalogElement.referencedElements.eType = ecore.EObject
re.CatalogElement.replicatedElements.eType = re.CatalogElement
re.CompliancyDefinitionPkg.ownedDefinitions.eType = re.CompliancyDefinition


#print('re.cross_init done')
