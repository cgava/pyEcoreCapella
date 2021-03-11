
#print('requirement.cross_init starting')


requirement.RequirementsPkg.ownedRequirements.eType = requirement.Requirement
requirement.RequirementsPkg.ownedRequirementPkgs.eType = requirement.RequirementsPkg
requirement.RequirementsTrace._source.eType = modellingcore.TraceableElement
requirement.RequirementsTrace._target.eType = modellingcore.TraceableElement
requirement.Requirement.relatedCapellaElements.eType = capellacore.CapellaElement

#print('requirement.cross_init done')
