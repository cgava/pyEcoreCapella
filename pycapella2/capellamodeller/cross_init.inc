
#print('capellamodeller.cross_init starting')


capellamodeller.Project.keyValuePairs.eType = capellacore.KeyValue
capellamodeller.Project.ownedFolders.eType = capellamodeller.Folder
capellamodeller.Project.ownedModelRoots.eType = capellamodeller.ModelRoot
capellamodeller.Folder.ownedFolders.eType = capellamodeller.Folder
capellamodeller.Folder.ownedModelRoots.eType = capellamodeller.ModelRoot
capellamodeller.SystemEngineering.containedOperationalAnalysis.eType = oa.OperationalAnalysis
capellamodeller.SystemEngineering.containedSystemAnalysis.eType = ctx.SystemAnalysis
capellamodeller.SystemEngineering.containedLogicalArchitectures.eType = la.LogicalArchitecture
capellamodeller.SystemEngineering.containedPhysicalArchitectures.eType = pa.PhysicalArchitecture
capellamodeller.SystemEngineering.containedEPBSArchitectures.eType = epbs.EPBSArchitecture
capellamodeller.SystemEngineering.containedSharedPkgs.eType = sharedmodel.SharedPkg
capellamodeller.SystemEngineeringPkg.ownedSystemEngineerings.eType = capellamodeller.SystemEngineering


#print('capellamodeller.cross_init done')
