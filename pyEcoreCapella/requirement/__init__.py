
from .requirement import getEClassifier, eClassifiers
from .requirement import name, nsURI, nsPrefix, eClass
from .requirement import RequirementsPkg, RequirementsTrace, Requirement, SystemFunctionalInterfaceRequirement, SystemFunctionalRequirement, SystemNonFunctionalInterfaceRequirement, SystemNonFunctionalRequirement, SystemUserRequirement

from modellingcore import AbstractConstraint, TraceableElement, AbstractTrace, ModelElement, AbstractInformationFlow, TraceableElement
from capellacore import EnumerationPropertyLiteral, AbstractPropertyValue, EnumerationPropertyType, NamingRule, PropertyValuePkg, CapellaElement, PropertyValueGroup, Trace
from capellacommon import GenericTrace
from emde import ElementExtension

from . import requirement

__all__ = ['RequirementsPkg', 'RequirementsTrace', 'Requirement', 'SystemFunctionalInterfaceRequirement',
           'SystemFunctionalRequirement', 'SystemNonFunctionalInterfaceRequirement', 'SystemNonFunctionalRequirement', 'SystemUserRequirement']

eSubpackages = []
eSuperPackage = None
requirement.eSubpackages = eSubpackages
requirement.eSuperPackage = eSuperPackage

RequirementsPkg.ownedRequirements.eType = Requirement
RequirementsPkg.ownedRequirementPkgs.eType = RequirementsPkg
RequirementsTrace._source.eType = TraceableElement
RequirementsTrace._target.eType = TraceableElement
Requirement.relatedCapellaElements.eType = CapellaElement

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
