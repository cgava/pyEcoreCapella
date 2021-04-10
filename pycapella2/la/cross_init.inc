
#print('la.cross_init starting')


la.LogicalArchitecturePkg.ownedLogicalArchitectures.eType = la.LogicalArchitecture
la.LogicalArchitecture.ownedLogicalComponentPkg.eType = la.LogicalComponentPkg
la.LogicalArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
la.LogicalArchitecture._containedLogicalFunctionPkg.eType = la.LogicalFunctionPkg
la.LogicalArchitecture.ownedSystemAnalysisRealizations.eType = la.SystemAnalysisRealization
la.LogicalArchitecture.allocatedSystemAnalysisRealizations.eType = la.SystemAnalysisRealization
la.LogicalFunction.ownedLogicalFunctionPkgs.eType = la.LogicalFunctionPkg
la.LogicalFunction.containedLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunction.childrenLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunctionPkg.ownedLogicalFunctions.eType = la.LogicalFunction
la.LogicalFunctionPkg.ownedLogicalFunctionPkgs.eType = la.LogicalFunctionPkg
la.LogicalComponent.ownedLogicalComponents.eType = la.LogicalComponent
la.LogicalComponent.ownedLogicalArchitectures.eType = la.LogicalArchitecture
la.LogicalComponent.ownedLogicalComponentPkgs.eType = la.LogicalComponentPkg
la.LogicalComponent.subLogicalComponents.eType = la.LogicalComponent
la.LogicalComponent.realizedSystemComponents.eType = ctx.SystemComponent
la.LogicalComponentPkg.ownedLogicalComponents.eType = la.LogicalComponent
la.LogicalComponentPkg.ownedLogicalComponentPkgs.eType = la.LogicalComponentPkg
la.CapabilityRealization.ownedCapabilityRealizationInvolvements.eType = capellacommon.CapabilityRealizationInvolvement
la.CapabilityRealization.involvedComponents.eType = capellacommon.CapabilityRealizationInvolvedElement
la.CapabilityRealizationPkg.ownedCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealizationPkg.ownedCapabilityRealizationPkgs.eType = la.CapabilityRealizationPkg
la.LogicalArchitecture.allocatedSystemAnalyses.eType = ctx.SystemAnalysis
la.LogicalArchitecture.allocatingPhysicalArchitectures.eType = pa.PhysicalArchitecture
la.LogicalFunction.allocatingLogicalComponents.eType = la.LogicalComponent
la.LogicalFunction.realizedSystemFunctions.eType = ctx.SystemFunction
la.LogicalFunction.realizingPhysicalFunctions.eType = pa.PhysicalFunction
la.LogicalComponent.allocatedLogicalFunctions.eType = la.LogicalFunction
la.LogicalComponent.allocatedLogicalFunctions.eOpposite = la.LogicalFunction.allocatingLogicalComponents
la.LogicalComponent.realizingPhysicalComponents.eType = pa.PhysicalComponent
la.CapabilityRealization.realizedCapabilities.eType = ctx.Capability
la.CapabilityRealization.realizedCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealization.realizingCapabilityRealizations.eType = la.CapabilityRealization
la.CapabilityRealization.realizingCapabilityRealizations.eOpposite = la.CapabilityRealization.realizedCapabilityRealizations


#print('la.cross_init done')
