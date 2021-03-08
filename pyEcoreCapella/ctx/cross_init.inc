
#print('ctx.cross_init starting')


SystemAnalysis.ownedSystemComponentPkg.eType = SystemComponentPkg
SystemAnalysis.ownedMissionPkg.eType = MissionPkg
SystemAnalysis._containedCapabilityPkg.eType = CapabilityPkg
SystemAnalysis._containedSystemFunctionPkg.eType = SystemFunctionPkg
SystemAnalysis.ownedOperationalAnalysisRealizations.eType = OperationalAnalysisRealization
SystemAnalysis.allocatedOperationalAnalysisRealizations.eType = OperationalAnalysisRealization
SystemFunction.ownedSystemFunctionPkgs.eType = SystemFunctionPkg
SystemFunction.allocatingSystemComponents.eType = SystemComponent
SystemFunction.containedSystemFunctions.eType = SystemFunction
SystemFunction.childrenSystemFunctions.eType = SystemFunction
SystemFunctionPkg.ownedSystemFunctions.eType = SystemFunction
SystemFunctionPkg.ownedSystemFunctionPkgs.eType = SystemFunctionPkg
SystemCommunicationHook.communication.eType = SystemCommunication
SystemCommunicationHook.type.eType = Component
SystemCommunication.ends.eType = SystemCommunicationHook
CapabilityInvolvement._systemComponent.eType = SystemComponent
CapabilityInvolvement._capability.eType = Capability
MissionInvolvement._systemComponent.eType = SystemComponent
MissionInvolvement._mission.eType = Mission
Mission.ownedMissionInvolvements.eType = MissionInvolvement
Mission.involvedSystemComponents.eType = SystemComponent
Mission.ownedCapabilityExploitations.eType = CapabilityExploitation
MissionPkg.ownedMissionPkgs.eType = MissionPkg
MissionPkg.ownedMissions.eType = Mission
Capability.ownedCapabilityInvolvements.eType = CapabilityInvolvement
Capability.involvedSystemComponents.eType = SystemComponent
Capability.purposes.eType = CapabilityExploitation
CapabilityExploitation._mission.eType = Mission
CapabilityExploitation.capability.eType = Capability
CapabilityPkg.ownedCapabilities.eType = Capability
CapabilityPkg.ownedCapabilityPkgs.eType = CapabilityPkg
SystemComponentPkg.ownedSystemComponents.eType = SystemComponent
SystemComponentPkg.ownedSystemComponentPkgs.eType = SystemComponentPkg
SystemComponent.ownedSystemComponents.eType = SystemComponent
SystemComponent.ownedSystemComponentPkgs.eType = SystemComponentPkg
SystemComponent.dataType.eType = Classifier
SystemComponent.involvingCapabilities.eType = Capability
SystemComponent.capabilityInvolvements.eType = CapabilityInvolvement
SystemComponent.involvingMissions.eType = Mission
SystemComponent.missionInvolvements.eType = MissionInvolvement
SystemComponent.realizedEntities.eType = Entity
SystemComponent.realizingLogicalComponents.eType = LogicalComponent
SystemComponent.allocatedSystemFunctions.eType = SystemFunction
SystemAnalysis.allocatedOperationalAnalyses.eType = OperationalAnalysis
SystemAnalysis.allocatingLogicalArchitectures.eType = LogicalArchitecture
SystemFunction.realizedOperationalActivities.eType = OperationalActivity
SystemFunction.realizingLogicalFunctions.eType = LogicalFunction
Mission.exploitedCapabilities.eType = Capability
Capability.purposeMissions.eType = Mission
Capability.purposeMissions.eOpposite = Mission.exploitedCapabilities
Capability.realizedOperationalCapabilities.eType = OperationalCapability
Capability.realizingCapabilityRealizations.eType = CapabilityRealization

#print('ctx.cross_init done')
