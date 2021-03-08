
from .pa import getEClassifier, eClassifiers
from .pa import name, nsURI, nsPrefix, eClass
from .pa import PhysicalArchitecturePkg, PhysicalArchitecture, PhysicalFunction, PhysicalFunctionPkg, PhysicalComponent, PhysicalComponentPkg, PhysicalNode, PhysicalComponentKind, LogicalArchitectureRealization, LogicalInterfaceRealization, PhysicalComponentNature

from cs import InterfaceImplementation, PhysicalLinkCategory, PhysicalPort, Interface, PhysicalPath, Component, AbstractDeploymentLink, ComponentRealization, AbstractDeploymentLink, PhysicalLink, InterfaceAllocator, Part, InterfaceAllocation, ArchitectureAllocation, InterfacePkg, InterfaceUse, BlockArchitecture
from capellacommon import StateMachine, GenericTrace, StateMachine, CapabilityRealizationInvolvement, State, AbstractCapabilityPkg
from requirement import RequirementsPkg, RequirementsTrace, Requirement
from fa import ComponentPort, ComponentExchangeCategory, FunctionRealization, FunctionalExchangeSpecification, ExchangeSpecificationRealization, ComponentExchangeRealization, ExchangeCategory, AbstractFunction, ExchangeLink, FunctionalChain, ComponentExchange, ComponentExchangeCategory, ComponentExchange, FunctionalExchange, AbstractFunctionalBlock, FunctionSpecification, ExchangeLink, ComponentFunctionalAllocation, ComponentExchangeRealization, FunctionPkg, ComponentFunctionalAllocation
from ctx import Capability
from la import CapabilityRealization, CapabilityRealizationPkg, LogicalArchitecture, LogicalFunction, LogicalComponent, CapabilityRealization
from information import DataPkg, KeyPart, Property, Association
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Generalization, AbstractPropertyValue, TypedElement, NamingRule, EnumerationPropertyType, Type, Involvement, Feature, PropertyValuePkg, PropertyValueGroup, Trace
from modellingcore import AbstractConstraint, AbstractConstraint, AbstractType, AbstractTrace, AbstractTypedElement, ModelElement, AbstractInformationFlow, AbstractType, TraceableElement
from activity import InterruptibleActivityRegion, ActivityEdge, ExceptionHandler, ActivityPartition, OutputPin, InputPin
from information.communication import CommunicationLink
from interaction import InstanceRole
from epbs import ConfigurationItem, EPBSArchitecture
from information.datavalue import NumericValue, DataValue
from emde import ElementExtension
from behavior import AbstractBehavior

from .deployment import InstanceDeploymentLink, AbstractPhysicalInstance, PortInstance, ConnectionInstance, DeploymentAspect, DeploymentConfiguration, ComponentInstance
from . import pa
from . import deployment


__all__ = ['PhysicalArchitecturePkg', 'PhysicalArchitecture', 'PhysicalFunction', 'PhysicalFunctionPkg', 'PhysicalComponent', 'PhysicalComponentPkg',
           'PhysicalNode', 'PhysicalComponentKind', 'LogicalArchitectureRealization', 'LogicalInterfaceRealization', 'PhysicalComponentNature']

eSubpackages = [deployment]
eSuperPackage = None
pa.eSubpackages = eSubpackages
pa.eSuperPackage = eSuperPackage

ComponentInstance.portInstances.eType = PortInstance
ComponentInstance.ownedAbstractPhysicalInstances.eType = AbstractPhysicalInstance
ComponentInstance.ownedInstanceDeploymentLinks.eType = InstanceDeploymentLink
ComponentInstance.type.eType = PhysicalComponent
ConnectionInstance.type.eType = ComponentExchange
DeploymentAspect.ownedConfigurations.eType = DeploymentConfiguration
DeploymentAspect.ownedDeploymentAspects.eType = DeploymentAspect
DeploymentConfiguration.ownedDeploymentLinks.eType = AbstractDeploymentLink
DeploymentConfiguration.ownedPhysicalInstances.eType = AbstractPhysicalInstance
PortInstance._component.eType = ComponentInstance
PortInstance.type.eType = ComponentPort
PhysicalArchitecturePkg.ownedPhysicalArchitecturePkgs.eType = PhysicalArchitecturePkg
PhysicalArchitecturePkg.ownedPhysicalArchitectures.eType = PhysicalArchitecture
PhysicalArchitecture.ownedPhysicalComponentPkg.eType = PhysicalComponentPkg
PhysicalArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
PhysicalArchitecture._containedPhysicalFunctionPkg.eType = PhysicalFunctionPkg
PhysicalArchitecture.ownedDeployments.eType = AbstractDeploymentLink
PhysicalArchitecture.ownedLogicalArchitectureRealizations.eType = LogicalArchitectureRealization
PhysicalArchitecture.allocatedLogicalArchitectureRealizations.eType = LogicalArchitectureRealization
PhysicalFunction.ownedPhysicalFunctionPkgs.eType = PhysicalFunctionPkg
PhysicalFunction.containedPhysicalFunctions.eType = PhysicalFunction
PhysicalFunction.childrenPhysicalFunctions.eType = PhysicalFunction
PhysicalFunctionPkg.ownedPhysicalFunctions.eType = PhysicalFunction
PhysicalFunctionPkg.ownedPhysicalFunctionPkgs.eType = PhysicalFunctionPkg
PhysicalComponent.ownedDeploymentLinks.eType = AbstractDeploymentLink
PhysicalComponent.ownedPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.ownedPhysicalComponentPkgs.eType = PhysicalComponentPkg
PhysicalComponent.logicalInterfaceRealizations.eType = LogicalInterfaceRealization
PhysicalComponent.subPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.deployedPhysicalComponents.eType = PhysicalComponent
PhysicalComponent.deployingPhysicalComponents.eType = PhysicalComponent
PhysicalComponentPkg.ownedPhysicalComponents.eType = PhysicalComponent
PhysicalComponentPkg.ownedPhysicalComponentPkgs.eType = PhysicalComponentPkg
PhysicalComponentPkg.ownedKeyParts.eType = KeyPart
PhysicalComponentPkg.ownedDeployments.eType = AbstractDeploymentLink
PhysicalNode.subPhysicalNodes.eType = PhysicalNode
ConnectionInstance.connectionEnds.eType = PortInstance
PortInstance.connections.eType = ConnectionInstance
PortInstance.connections.eOpposite = ConnectionInstance.connectionEnds
PhysicalArchitecture.allocatedLogicalArchitectures.eType = LogicalArchitecture
PhysicalArchitecture.allocatingEpbsArchitectures.eType = EPBSArchitecture
PhysicalFunction.allocatingPhysicalComponents.eType = PhysicalComponent
PhysicalFunction.realizedLogicalFunctions.eType = LogicalFunction
PhysicalComponent.realizedLogicalComponents.eType = LogicalComponent
PhysicalComponent.allocatedPhysicalFunctions.eType = PhysicalFunction
PhysicalComponent.allocatedPhysicalFunctions.eOpposite = PhysicalFunction.allocatingPhysicalComponents

otherClassifiers = [PhysicalComponentKind, PhysicalComponentNature]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
