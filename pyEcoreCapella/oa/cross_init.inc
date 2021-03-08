
#print('oa.cross_init starting')


OperationalAnalysis.ownedRolePkg.eType = RolePkg
OperationalAnalysis.ownedEntityPkg.eType = EntityPkg
OperationalAnalysis.ownedConceptPkg.eType = ConceptPkg
OperationalAnalysis._containedOperationalCapabilityPkg.eType = OperationalCapabilityPkg
OperationalAnalysis._containedOperationalActivityPkg.eType = OperationalActivityPkg
OperationalActivityPkg.ownedOperationalActivities.eType = OperationalActivity
OperationalActivityPkg.ownedOperationalActivityPkgs.eType = OperationalActivityPkg
OperationalActivity.ownedOperationalActivityPkgs.eType = OperationalActivityPkg
OperationalActivity.ownedSwimlanes.eType = Swimlane
OperationalActivity.ownedProcess.eType = OperationalProcess
OperationalActivity.allocatingRoles.eType = Role
OperationalActivity.containedOperationalActivities.eType = OperationalActivity
OperationalActivity.childrenOperationalActivities.eType = OperationalActivity
OperationalProcess.involvingOperationalCapabilities.eType = OperationalCapability
Swimlane._representedEntity.eType = Entity
OperationalCapabilityPkg.ownedOperationalCapabilities.eType = OperationalCapability
OperationalCapabilityPkg.ownedOperationalCapabilityPkgs.eType = OperationalCapabilityPkg
OperationalCapabilityPkg.ownedCapabilityConfigurations.eType = CapabilityConfiguration
OperationalCapabilityPkg.ownedConceptCompliances.eType = ConceptCompliance
OperationalCapability.compliances.eType = ConceptCompliance
OperationalCapability.configurations.eType = CapabilityConfiguration
OperationalCapability.ownedEntityOperationalCapabilityInvolvements.eType = EntityOperationalCapabilityInvolvement
OperationalCapability.involvedEntities.eType = Entity
RolePkg.ownedRolePkgs.eType = RolePkg
RolePkg.ownedRoles.eType = Role
Role.ownedRoleAssemblyUsages.eType = RoleAssemblyUsage
Role.ownedActivityAllocations.eType = ActivityAllocation
Role.allocatingEntities.eType = Entity
Role.allocatedOperationalActivities.eType = OperationalActivity
RoleAssemblyUsage.child.eType = Role
EntityPkg.ownedEntities.eType = Entity
EntityPkg.ownedEntityPkgs.eType = EntityPkg
EntityPkg.ownedLocations.eType = Location
EntityPkg.ownedCommunicationMeans.eType = CommunicationMean
Entity.organisationalUnitMemberships.eType = OrganisationalUnitComposition
Entity.actualLocation.eType = Location
Entity.subEntities.eType = Entity
Entity.ownedEntities.eType = Entity
Entity.ownedCommunicationMeans.eType = CommunicationMean
Entity.ownedRoleAllocations.eType = RoleAllocation
Entity.allocatedRoles.eType = Role
Entity.involvingOperationalCapabilities.eType = OperationalCapability
Entity.realizingSystemComponents.eType = SystemComponent
ConceptPkg.ownedConceptPkgs.eType = ConceptPkg
ConceptPkg.ownedConcepts.eType = Concept
Concept.compliances.eType = ConceptCompliance
Concept.compositeLinks.eType = ItemInConcept
ConceptCompliance.complyWithConcept.eType = Concept
ConceptCompliance.compliantCapability.eType = OperationalCapability
ItemInConcept.concept.eType = Concept
ItemInConcept.item.eType = AbstractConceptItem
AbstractConceptItem.composingLinks.eType = ItemInConcept
CommunityOfInterest.communityOfInterestCompositions.eType = CommunityOfInterestComposition
CommunityOfInterestComposition.communityOfInterest.eType = CommunityOfInterest
CommunityOfInterestComposition.interestedOrganisationUnit.eType = OrganisationalUnit
OrganisationalUnit.organisationalUnitCompositions.eType = OrganisationalUnitComposition
OrganisationalUnit.communityOfInterestMemberships.eType = CommunityOfInterestComposition
OrganisationalUnitComposition.organisationalUnit.eType = OrganisationalUnit
OrganisationalUnitComposition.participatingEntity.eType = Entity
Location.locatedEntities.eType = Entity
CapabilityConfiguration.configuredCapability.eType = OperationalCapability
CommunicationMean._sourceEntity.eType = Entity
CommunicationMean._targetEntity.eType = Entity
EntityOperationalCapabilityInvolvement._entity.eType = Entity
EntityOperationalCapabilityInvolvement._capability.eType = OperationalCapability
OperationalAnalysis.allocatingSystemAnalyses.eType = SystemAnalysis
OperationalActivity.activityAllocations.eType = ActivityAllocation
OperationalActivity.allocatorEntities.eType = Entity
OperationalActivity.realizingSystemFunctions.eType = SystemFunction
OperationalCapability.realizingCapabilities.eType = Capability
ActivityAllocation._role.eType = Role
ActivityAllocation._activity.eType = OperationalActivity
ActivityAllocation._activity.eOpposite = OperationalActivity.activityAllocations
Role.roleAllocations.eType = RoleAllocation
Role.activityAllocations.eType = ActivityAllocation
Role.activityAllocations.eOpposite = ActivityAllocation.role
RoleAllocation._role.eType = Role
RoleAllocation._role.eOpposite = Role.roleAllocations
RoleAllocation._entity.eType = Entity
Entity.roleAllocations.eType = RoleAllocation
Entity.roleAllocations.eOpposite = RoleAllocation.entity
Entity.allocatedOperationalActivities.eType = OperationalActivity
Entity.allocatedOperationalActivities.eOpposite = OperationalActivity.allocatorEntities

#print('oa.cross_init done')