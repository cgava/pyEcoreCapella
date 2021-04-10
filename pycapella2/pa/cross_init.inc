
#print('pa.cross_init starting')


pa.deployment.ComponentInstance.portInstances.eType = pa.deployment.PortInstance
pa.deployment.ComponentInstance.ownedAbstractPhysicalInstances.eType = pa.deployment.AbstractPhysicalInstance
pa.deployment.ComponentInstance.ownedInstanceDeploymentLinks.eType = pa.deployment.InstanceDeploymentLink
pa.deployment.ComponentInstance.type.eType = pa.PhysicalComponent
pa.deployment.ConnectionInstance.type.eType = fa.ComponentExchange
pa.deployment.DeploymentAspect.ownedConfigurations.eType = pa.deployment.DeploymentConfiguration
pa.deployment.DeploymentAspect.ownedDeploymentAspects.eType = pa.deployment.DeploymentAspect
pa.deployment.DeploymentConfiguration.ownedDeploymentLinks.eType = cs.AbstractDeploymentLink
pa.deployment.DeploymentConfiguration.ownedPhysicalInstances.eType = pa.deployment.AbstractPhysicalInstance
pa.deployment.PortInstance._component.eType = pa.deployment.ComponentInstance
pa.deployment.PortInstance.type.eType = fa.ComponentPort
pa.PhysicalArchitecturePkg.ownedPhysicalArchitecturePkgs.eType = pa.PhysicalArchitecturePkg
pa.PhysicalArchitecturePkg.ownedPhysicalArchitectures.eType = pa.PhysicalArchitecture
pa.PhysicalArchitecture.ownedPhysicalComponentPkg.eType = pa.PhysicalComponentPkg
pa.PhysicalArchitecture._containedCapabilityRealizationPkg.eType = la.CapabilityRealizationPkg
pa.PhysicalArchitecture._containedPhysicalFunctionPkg.eType = pa.PhysicalFunctionPkg
pa.PhysicalArchitecture.ownedDeployments.eType = cs.AbstractDeploymentLink
pa.PhysicalArchitecture.ownedLogicalArchitectureRealizations.eType = pa.LogicalArchitectureRealization
pa.PhysicalArchitecture.allocatedLogicalArchitectureRealizations.eType = pa.LogicalArchitectureRealization
pa.PhysicalFunction.ownedPhysicalFunctionPkgs.eType = pa.PhysicalFunctionPkg
pa.PhysicalFunction.containedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunction.childrenPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunctionPkg.ownedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalFunctionPkg.ownedPhysicalFunctionPkgs.eType = pa.PhysicalFunctionPkg
pa.PhysicalComponent.ownedDeploymentLinks.eType = cs.AbstractDeploymentLink
pa.PhysicalComponent.ownedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.ownedPhysicalComponentPkgs.eType = pa.PhysicalComponentPkg
pa.PhysicalComponent.logicalInterfaceRealizations.eType = pa.LogicalInterfaceRealization
pa.PhysicalComponent.subPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.deployedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponent.deployingPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponentPkg.ownedPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalComponentPkg.ownedPhysicalComponentPkgs.eType = pa.PhysicalComponentPkg
pa.PhysicalComponentPkg.ownedKeyParts.eType = information.KeyPart
pa.PhysicalComponentPkg.ownedDeployments.eType = cs.AbstractDeploymentLink
pa.PhysicalNode.subPhysicalNodes.eType = pa.PhysicalNode
pa.deployment.ConnectionInstance.connectionEnds.eType = pa.deployment.PortInstance
pa.deployment.PortInstance.connections.eType = pa.deployment.ConnectionInstance
pa.deployment.PortInstance.connections.eOpposite = pa.deployment.ConnectionInstance.connectionEnds
pa.PhysicalArchitecture.allocatedLogicalArchitectures.eType = la.LogicalArchitecture
pa.PhysicalArchitecture.allocatingEpbsArchitectures.eType = epbs.EPBSArchitecture
pa.PhysicalFunction.allocatingPhysicalComponents.eType = pa.PhysicalComponent
pa.PhysicalFunction.realizedLogicalFunctions.eType = la.LogicalFunction
pa.PhysicalComponent.realizedLogicalComponents.eType = la.LogicalComponent
pa.PhysicalComponent.allocatedPhysicalFunctions.eType = pa.PhysicalFunction
pa.PhysicalComponent.allocatedPhysicalFunctions.eOpposite = pa.PhysicalFunction.allocatingPhysicalComponents


#print('pa.cross_init done')
