
#print('capellamodeller.cross_init starting')


Project.keyValuePairs.eType = KeyValue
Project.ownedFolders.eType = Folder
Project.ownedModelRoots.eType = ModelRoot
Folder.ownedFolders.eType = Folder
Folder.ownedModelRoots.eType = ModelRoot
SystemEngineering.containedOperationalAnalysis.eType = OperationalAnalysis
SystemEngineering.containedSystemAnalysis.eType = SystemAnalysis
SystemEngineering.containedLogicalArchitectures.eType = LogicalArchitecture
SystemEngineering.containedPhysicalArchitectures.eType = PhysicalArchitecture
SystemEngineering.containedEPBSArchitectures.eType = EPBSArchitecture
SystemEngineering.containedSharedPkgs.eType = SharedPkg
SystemEngineeringPkg.ownedSystemEngineerings.eType = SystemEngineering

#print('capellamodeller.cross_init done')
