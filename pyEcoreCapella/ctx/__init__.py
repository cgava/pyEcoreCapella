
from .ctx import getEClassifier, eClassifiers
from .ctx import name, nsURI, nsPrefix, eClass
from .ctx import SystemAnalysis, SystemFunction, SystemFunctionPkg, SystemCommunicationHook, SystemCommunication, CapabilityInvolvement, MissionInvolvement, Mission, MissionPkg, Capability, CapabilityExploitation, CapabilityPkg, OperationalAnalysisRealization, SystemComponentPkg, SystemComponent

from la import CapabilityRealization, LogicalFunction, LogicalArchitecture, LogicalComponent, CapabilityRealization
from oa import OperationalAnalysis, OperationalCapability, OperationalActivity, Entity
from capellacommon import StateMachine, State, GenericTrace, StateMachine, State, AbstractCapabilityPkg
from cs import Component, InterfaceImplementation, PhysicalLinkCategory, PhysicalPort, Interface, PhysicalPath, Component, ComponentRealization, PhysicalLink, Part, InterfaceAllocation, ArchitectureAllocation, InterfacePkg, InterfaceUse, BlockArchitecture
from requirement import RequirementsPkg, RequirementsTrace, Requirement
from interaction import AbstractCapabilityRealization, AbstractCapabilityInclude, AbstractCapabilityExtend, AbstractCapability, AbstractCapabilityGeneralization, AbstractCapabilityExtensionPoint, FunctionalChainAbstractCapabilityInvolvement, Scenario, InstanceRole, AbstractFunctionAbstractCapabilityInvolvement
from fa import ComponentExchangeCategory, FunctionRealization, ComponentFunctionalAllocation, FunctionalExchangeSpecification, ExchangeSpecificationRealization, ComponentExchangeRealization, ExchangeCategory, AbstractFunction, ExchangeLink, FunctionalChain, ComponentExchange, ComponentExchangeCategory, ComponentExchange, FunctionalExchange, AbstractFunctionalBlock, FunctionSpecification, FunctionalChain, ExchangeLink, ComponentFunctionalAllocation, ComponentExchangeRealization, AbstractFunction, FunctionPkg, ComponentPort
from information import DataPkg, Property, Association
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Generalization, Classifier, AbstractPropertyValue, InvolverElement, TypedElement, InvolvedElement, NamingRule, EnumerationPropertyType, Type, Involvement, Feature, PropertyValuePkg, PropertyValueGroup, Trace, Constraint
from modellingcore import AbstractConstraint, AbstractConstraint, AbstractType, AbstractTrace, AbstractTypedElement, ModelElement, AbstractInformationFlow, AbstractType, TraceableElement
from activity import InterruptibleActivityRegion, ActivityEdge, ExceptionHandler, ActivityPartition, OutputPin, InputPin
from information.communication import CommunicationLink
from information.datavalue import NumericValue, DataValue
from emde import ElementExtension
from behavior import AbstractBehavior

from . import ctx

__all__ = ['SystemAnalysis', 'SystemFunction', 'SystemFunctionPkg', 'SystemCommunicationHook', 'SystemCommunication', 'CapabilityInvolvement', 'MissionInvolvement',
           'Mission', 'MissionPkg', 'Capability', 'CapabilityExploitation', 'CapabilityPkg', 'OperationalAnalysisRealization', 'SystemComponentPkg', 'SystemComponent']

eSubpackages = []
eSuperPackage = None
ctx.eSubpackages = eSubpackages
ctx.eSuperPackage = eSuperPackage

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

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
