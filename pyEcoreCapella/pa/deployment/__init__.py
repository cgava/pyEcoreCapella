
from .deployment import getEClassifier, eClassifiers
from .deployment import name, nsURI, nsPrefix, eClass
from .deployment import ComponentInstance, ConnectionInstance, DeploymentAspect, DeploymentConfiguration, InstanceDeploymentLink, PartDeploymentLink, AbstractPhysicalInstance, PortInstance, TypeDeploymentLink

from capellacore import EnumerationPropertyLiteral, AbstractPropertyValue, EnumerationPropertyType, NamingRule, PropertyValuePkg, PropertyValueGroup, Trace
from capellacommon import GenericTrace
from modellingcore import AbstractTrace, AbstractConstraint, ModelElement, AbstractInformationFlow
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from fa import ComponentExchange, ComponentPort
from cs import DeployableElement, DeploymentTarget, AbstractDeploymentLink, AbstractDeploymentLink
from pa import PhysicalComponent

from . import deployment
from .. import pa


__all__ = ['ComponentInstance', 'ConnectionInstance', 'DeploymentAspect', 'DeploymentConfiguration',
           'InstanceDeploymentLink', 'PartDeploymentLink', 'AbstractPhysicalInstance', 'PortInstance', 'TypeDeploymentLink']

eSubpackages = []
eSuperPackage = pa
deployment.eSubpackages = eSubpackages
deployment.eSuperPackage = eSuperPackage


otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
