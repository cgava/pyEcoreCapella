
from .la import getEClassifier, eClassifiers
from .la import name, nsURI, nsPrefix, eClass
from .la import LogicalArchitecturePkg, LogicalArchitecture, LogicalFunction, LogicalFunctionPkg, LogicalComponent, LogicalComponentPkg, CapabilityRealization, CapabilityRealizationPkg, SystemAnalysisRealization, ContextInterfaceRealization

from capellacommon import StateMachine, State, GenericTrace, StateMachine, CapabilityRealizationInvolvement, State, AbstractCapabilityPkg, CapabilityRealizationInvolvedElement, CapabilityRealizationInvolvement
from cs import InterfaceImplementation, PhysicalLinkCategory, PhysicalPort, Interface, PhysicalPath, Component, ComponentRealization, PhysicalLink, InterfaceAllocator, Part, InterfaceAllocation, ArchitectureAllocation, InterfacePkg, InterfaceUse, BlockArchitecture
from requirement import RequirementsPkg, RequirementsTrace, Requirement
from interaction import AbstractCapabilityRealization, AbstractCapabilityInclude, AbstractCapabilityExtend, AbstractCapability, AbstractCapabilityGeneralization, AbstractCapabilityExtensionPoint, FunctionalChainAbstractCapabilityInvolvement, Scenario, InstanceRole, AbstractFunctionAbstractCapabilityInvolvement
from fa import ComponentExchangeCategory, FunctionRealization, ComponentFunctionalAllocation, FunctionalExchangeSpecification, ExchangeSpecificationRealization, ComponentExchangeRealization, ExchangeCategory, AbstractFunction, ExchangeLink, FunctionalChain, ComponentExchange, ComponentExchangeCategory, ComponentExchange, FunctionalExchange, AbstractFunctionalBlock, FunctionSpecification, FunctionalChain, ExchangeLink, ComponentFunctionalAllocation, ComponentExchangeRealization, AbstractFunction, FunctionPkg, ComponentPort
from ctx import SystemAnalysis, Capability, Capability, SystemFunction, SystemComponent
from information import DataPkg, Property, Association
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Generalization, AbstractPropertyValue, TypedElement, NamingRule, EnumerationPropertyType, Type, Involvement, Feature, PropertyValuePkg, PropertyValueGroup, Trace, Constraint
from modellingcore import AbstractConstraint, AbstractConstraint, AbstractType, AbstractTrace, AbstractTypedElement, ModelElement, AbstractInformationFlow, AbstractType, TraceableElement
from activity import InterruptibleActivityRegion, ActivityEdge, ExceptionHandler, ActivityPartition, OutputPin, InputPin
from information.communication import CommunicationLink
from information.datavalue import NumericValue, DataValue
from pa import PhysicalArchitecture, PhysicalFunction, PhysicalComponent
from emde import ElementExtension
from behavior import AbstractBehavior

from . import la

__all__ = ['LogicalArchitecturePkg', 'LogicalArchitecture', 'LogicalFunction', 'LogicalFunctionPkg', 'LogicalComponent',
           'LogicalComponentPkg', 'CapabilityRealization', 'CapabilityRealizationPkg', 'SystemAnalysisRealization', 'ContextInterfaceRealization']

eSubpackages = []
eSuperPackage = None
la.eSubpackages = eSubpackages
la.eSuperPackage = eSuperPackage

LogicalArchitecturePkg.ownedLogicalArchitectures.eType = LogicalArchitecture
LogicalArchitecture.ownedLogicalComponentPkg.eType = LogicalComponentPkg
LogicalArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
LogicalArchitecture._containedLogicalFunctionPkg.eType = LogicalFunctionPkg
LogicalArchitecture.ownedSystemAnalysisRealizations.eType = SystemAnalysisRealization
LogicalArchitecture.allocatedSystemAnalysisRealizations.eType = SystemAnalysisRealization
LogicalFunction.ownedLogicalFunctionPkgs.eType = LogicalFunctionPkg
LogicalFunction.containedLogicalFunctions.eType = LogicalFunction
LogicalFunction.childrenLogicalFunctions.eType = LogicalFunction
LogicalFunctionPkg.ownedLogicalFunctions.eType = LogicalFunction
LogicalFunctionPkg.ownedLogicalFunctionPkgs.eType = LogicalFunctionPkg
LogicalComponent.ownedLogicalComponents.eType = LogicalComponent
LogicalComponent.ownedLogicalArchitectures.eType = LogicalArchitecture
LogicalComponent.ownedLogicalComponentPkgs.eType = LogicalComponentPkg
LogicalComponent.subLogicalComponents.eType = LogicalComponent
LogicalComponent.realizedSystemComponents.eType = SystemComponent
LogicalComponentPkg.ownedLogicalComponents.eType = LogicalComponent
LogicalComponentPkg.ownedLogicalComponentPkgs.eType = LogicalComponentPkg
CapabilityRealization.ownedCapabilityRealizationInvolvements.eType = CapabilityRealizationInvolvement
CapabilityRealization.involvedComponents.eType = CapabilityRealizationInvolvedElement
CapabilityRealizationPkg.ownedCapabilityRealizations.eType = CapabilityRealization
CapabilityRealizationPkg.ownedCapabilityRealizationPkgs.eType = CapabilityRealizationPkg
LogicalArchitecture.allocatedSystemAnalyses.eType = SystemAnalysis
LogicalArchitecture.allocatingPhysicalArchitectures.eType = PhysicalArchitecture
LogicalFunction.allocatingLogicalComponents.eType = LogicalComponent
LogicalFunction.realizedSystemFunctions.eType = SystemFunction
LogicalFunction.realizingPhysicalFunctions.eType = PhysicalFunction
LogicalComponent.allocatedLogicalFunctions.eType = LogicalFunction
LogicalComponent.allocatedLogicalFunctions.eOpposite = LogicalFunction.allocatingLogicalComponents
LogicalComponent.realizingPhysicalComponents.eType = PhysicalComponent
CapabilityRealization.realizedCapabilities.eType = Capability
CapabilityRealization.realizedCapabilityRealizations.eType = CapabilityRealization
CapabilityRealization.realizingCapabilityRealizations.eType = CapabilityRealization
CapabilityRealization.realizingCapabilityRealizations.eOpposite = CapabilityRealization.realizedCapabilityRealizations

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
