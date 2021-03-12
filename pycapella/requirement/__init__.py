#print('requirement.__init__.py loading')
from pyecore.resources import global_registry
from .requirement import getEClassifier, eClassifiers
from .requirement import name, nsURI, nsPrefix, eClass
from .requirement import Requirement, RequirementsPkg, RequirementsTrace, SystemFunctionalInterfaceRequirement, SystemFunctionalRequirement, SystemNonFunctionalInterfaceRequirement, SystemNonFunctionalRequirement, SystemUserRequirement
from . import requirement

__all__ = ['Requirement', 'RequirementsPkg', 'RequirementsTrace', 'SystemFunctionalInterfaceRequirement',
           'SystemFunctionalRequirement', 'SystemNonFunctionalInterfaceRequirement', 'SystemNonFunctionalRequirement', 'SystemUserRequirement']

eSubpackages = []
eSuperPackage = None
requirement.eSubpackages = eSubpackages
requirement.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [requirement] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('requirement.__init__.py loaded')
