
#print('epbs.cross_init starting')


epbs.EPBSArchitecturePkg.ownedEPBSArchitectures.eType = epbs.EPBSArchitecture
epbs.EPBSArchitecture.ownedConfigurationItemPkg.eType = epbs.ConfigurationItemPkg
epbs.EPBSArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
epbs.EPBSArchitecture.ownedPhysicalArchitectureRealizations.eType = epbs.PhysicalArchitectureRealization
epbs.EPBSArchitecture.allocatedPhysicalArchitectureRealizations.eType = epbs.PhysicalArchitectureRealization
epbs.ConfigurationItemPkg.ownedConfigurationItems.eType = epbs.ConfigurationItem
epbs.ConfigurationItemPkg.ownedConfigurationItemPkgs.eType = epbs.ConfigurationItemPkg
epbs.ConfigurationItem.ownedConfigurationItems.eType = epbs.ConfigurationItem
epbs.ConfigurationItem.ownedConfigurationItemPkgs.eType = epbs.ConfigurationItemPkg
epbs.ConfigurationItem.ownedPhysicalArtifactRealizations.eType = epbs.PhysicalArtifactRealization
epbs.PhysicalArtifactRealization._realizedPhysicalArtifact.eType = cs.AbstractPhysicalArtifact
epbs.PhysicalArtifactRealization._realizingConfigurationItem.eType = epbs.ConfigurationItem
epbs.EPBSArchitecture.allocatedPhysicalArchitectures.eType = pa.PhysicalArchitecture
epbs.ConfigurationItem.allocatedPhysicalArtifacts.eType = cs.AbstractPhysicalArtifact

#print('epbs.cross_init done')
