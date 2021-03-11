#print('oa.__init__.py loading')
from pyecore.resources import global_registry
from .oa import getEClassifier, eClassifiers
from .oa import name, nsURI, nsPrefix, eClass
from .oa import AbstractConceptItem, ActivityAllocation, CapabilityConfiguration, CommunicationMean, CommunityOfInterest, CommunityOfInterestComposition, Concept, ConceptCompliance, ConceptPkg, Entity, EntityOperationalCapabilityInvolvement, EntityPkg, ItemInConcept, Location, OperationalActivity, OperationalActivityPkg, OperationalAnalysis, OperationalCapability, OperationalCapabilityPkg, OperationalProcess, OperationalScenario, OrganisationalUnit, OrganisationalUnitComposition, Role, RoleAllocation, RoleAssemblyUsage, RolePkg, Swimlane
from . import oa

__all__ = ['AbstractConceptItem', 'ActivityAllocation', 'CapabilityConfiguration', 'CommunicationMean', 'CommunityOfInterest', 'CommunityOfInterestComposition', 'Concept', 'ConceptCompliance', 'ConceptPkg', 'Entity', 'EntityOperationalCapabilityInvolvement', 'EntityPkg', 'ItemInConcept', 'Location',
           'OperationalActivity', 'OperationalActivityPkg', 'OperationalAnalysis', 'OperationalCapability', 'OperationalCapabilityPkg', 'OperationalProcess', 'OperationalScenario', 'OrganisationalUnit', 'OrganisationalUnitComposition', 'Role', 'RoleAllocation', 'RoleAssemblyUsage', 'RolePkg', 'Swimlane']

eSubpackages = []
eSuperPackage = None
oa.eSubpackages = eSubpackages
oa.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [oa] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('oa.__init__.py loaded')
