
from .epbs import getEClassifier, eClassifiers
from .epbs import name, nsURI, nsPrefix, eClass
from .epbs import EPBSArchitecturePkg, EPBSArchitecture, ConfigurationItemPkg, ConfigurationItem, ConfigurationItemKind, PhysicalArchitectureRealization, PhysicalArtifactRealization

from fa import ExchangeLink, ComponentExchangeCategory, ComponentExchange, ExchangeLink, ComponentFunctionalAllocation, ComponentFunctionalAllocation, ComponentExchangeRealization, ComponentExchangeCategory, ComponentExchange, FunctionPkg, AbstractFunction, ComponentExchangeRealization, ComponentPort
from cs import InterfaceImplementation, PhysicalPort, AbstractPhysicalArtifact, Interface, PhysicalLinkCategory, Component, PhysicalPath, ComponentRealization, PhysicalLink, Part, InterfaceAllocation, ArchitectureAllocation, InterfacePkg, InterfaceUse, BlockArchitecture
from pa import PhysicalArchitecture
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Trace, Generalization, AbstractPropertyValue, TypedElement, EnumerationPropertyType, NamingRule, Involvement, Feature, PropertyValueGroup, PropertyValuePkg
from modellingcore import AbstractConstraint, AbstractTrace, AbstractTypedElement, AbstractInformationFlow, ModelElement, TraceableElement
from requirement import RequirementsPkg, RequirementsTrace, Requirement
from capellacommon import GenericTrace, AbstractCapabilityPkg, StateMachine, CapabilityRealizationInvolvement
from emde import ElementExtension
from information.communication import CommunicationLink
from la import CapabilityRealization, CapabilityRealizationPkg
from information import DataPkg, Property

from . import epbs

__all__ = ['EPBSArchitecturePkg', 'EPBSArchitecture', 'ConfigurationItemPkg', 'ConfigurationItem',
           'ConfigurationItemKind', 'PhysicalArchitectureRealization', 'PhysicalArtifactRealization']

eSubpackages = []
eSuperPackage = None
epbs.eSubpackages = eSubpackages
epbs.eSuperPackage = eSuperPackage

EPBSArchitecturePkg.ownedEPBSArchitectures.eType = EPBSArchitecture
EPBSArchitecture.ownedConfigurationItemPkg.eType = ConfigurationItemPkg
EPBSArchitecture._containedCapabilityRealizationPkg.eType = CapabilityRealizationPkg
EPBSArchitecture.ownedPhysicalArchitectureRealizations.eType = PhysicalArchitectureRealization
EPBSArchitecture.allocatedPhysicalArchitectureRealizations.eType = PhysicalArchitectureRealization
ConfigurationItemPkg.ownedConfigurationItems.eType = ConfigurationItem
ConfigurationItemPkg.ownedConfigurationItemPkgs.eType = ConfigurationItemPkg
ConfigurationItem.ownedConfigurationItems.eType = ConfigurationItem
ConfigurationItem.ownedConfigurationItemPkgs.eType = ConfigurationItemPkg
ConfigurationItem.ownedPhysicalArtifactRealizations.eType = PhysicalArtifactRealization
PhysicalArtifactRealization._realizedPhysicalArtifact.eType = AbstractPhysicalArtifact
PhysicalArtifactRealization._realizingConfigurationItem.eType = ConfigurationItem
EPBSArchitecture.allocatedPhysicalArchitectures.eType = PhysicalArchitecture
ConfigurationItem.allocatedPhysicalArtifacts.eType = AbstractPhysicalArtifact

otherClassifiers = [ConfigurationItemKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
