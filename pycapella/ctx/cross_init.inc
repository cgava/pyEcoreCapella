
#print('ctx.cross_init starting')


ctx.SystemAnalysis.ownedSystemComponentPkg.eType = ctx.SystemComponentPkg
ctx.SystemAnalysis.ownedMissionPkg.eType = ctx.MissionPkg
ctx.SystemAnalysis._containedCapabilityPkg.eType = ctx.CapabilityPkg
ctx.SystemAnalysis._containedSystemFunctionPkg.eType = ctx.SystemFunctionPkg
ctx.SystemAnalysis.ownedOperationalAnalysisRealizations.eType = ctx.OperationalAnalysisRealization
ctx.SystemAnalysis.allocatedOperationalAnalysisRealizations.eType = ctx.OperationalAnalysisRealization
ctx.SystemFunction.ownedSystemFunctionPkgs.eType = ctx.SystemFunctionPkg
ctx.SystemFunction.allocatingSystemComponents.eType = ctx.SystemComponent
ctx.SystemFunction.containedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunction.childrenSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunctionPkg.ownedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemFunctionPkg.ownedSystemFunctionPkgs.eType = ctx.SystemFunctionPkg
ctx.SystemCommunicationHook.communication.eType = ctx.SystemCommunication
ctx.SystemCommunicationHook.type.eType = cs.Component
ctx.SystemCommunication.ends.eType = ctx.SystemCommunicationHook
ctx.CapabilityInvolvement._systemComponent.eType = ctx.SystemComponent
ctx.CapabilityInvolvement._capability.eType = ctx.Capability
ctx.MissionInvolvement._systemComponent.eType = ctx.SystemComponent
ctx.MissionInvolvement._mission.eType = ctx.Mission
ctx.Mission.ownedMissionInvolvements.eType = ctx.MissionInvolvement
ctx.Mission.involvedSystemComponents.eType = ctx.SystemComponent
ctx.Mission.ownedCapabilityExploitations.eType = ctx.CapabilityExploitation
ctx.MissionPkg.ownedMissionPkgs.eType = ctx.MissionPkg
ctx.MissionPkg.ownedMissions.eType = ctx.Mission
ctx.Capability.ownedCapabilityInvolvements.eType = ctx.CapabilityInvolvement
ctx.Capability.involvedSystemComponents.eType = ctx.SystemComponent
ctx.Capability.purposes.eType = ctx.CapabilityExploitation
ctx.CapabilityExploitation._mission.eType = ctx.Mission
ctx.CapabilityExploitation.capability.eType = ctx.Capability
ctx.CapabilityPkg.ownedCapabilities.eType = ctx.Capability
ctx.CapabilityPkg.ownedCapabilityPkgs.eType = ctx.CapabilityPkg
ctx.SystemComponentPkg.ownedSystemComponents.eType = ctx.SystemComponent
ctx.SystemComponentPkg.ownedSystemComponentPkgs.eType = ctx.SystemComponentPkg
ctx.SystemComponent.ownedSystemComponents.eType = ctx.SystemComponent
ctx.SystemComponent.ownedSystemComponentPkgs.eType = ctx.SystemComponentPkg
ctx.SystemComponent.dataType.eType = capellacore.Classifier
ctx.SystemComponent.involvingCapabilities.eType = ctx.Capability
ctx.SystemComponent.capabilityInvolvements.eType = ctx.CapabilityInvolvement
ctx.SystemComponent.involvingMissions.eType = ctx.Mission
ctx.SystemComponent.missionInvolvements.eType = ctx.MissionInvolvement
ctx.SystemComponent.realizedEntities.eType = oa.Entity
ctx.SystemComponent.realizingLogicalComponents.eType = la.LogicalComponent
ctx.SystemComponent.allocatedSystemFunctions.eType = ctx.SystemFunction
ctx.SystemAnalysis.allocatedOperationalAnalyses.eType = oa.OperationalAnalysis
ctx.SystemAnalysis.allocatingLogicalArchitectures.eType = la.LogicalArchitecture
ctx.SystemFunction.realizedOperationalActivities.eType = oa.OperationalActivity
ctx.SystemFunction.realizingLogicalFunctions.eType = la.LogicalFunction
ctx.Mission.exploitedCapabilities.eType = ctx.Capability
ctx.Capability.purposeMissions.eType = ctx.Mission
ctx.Capability.purposeMissions.eOpposite = ctx.Mission.exploitedCapabilities
ctx.Capability.realizedOperationalCapabilities.eType = oa.OperationalCapability
ctx.Capability.realizingCapabilityRealizations.eType = la.CapabilityRealization

#print('ctx.cross_init done')
