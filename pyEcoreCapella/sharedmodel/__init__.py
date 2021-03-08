
from .sharedmodel import getEClassifier, eClassifiers
from .sharedmodel import name, nsURI, nsPrefix, eClass
from .sharedmodel import SharedPkg, GenericPkg

from modellingcore import AbstractConstraint, AbstractTrace, ModelElement
from capellacore import CapellaElement, EnumerationPropertyLiteral, Trace, AbstractPropertyValue, EnumerationPropertyType, NamingRule, ReuseLink, PropertyValueGroup, PropertyValuePkg
from capellacommon import GenericTrace
from information import DataPkg
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension

from . import sharedmodel

__all__ = ['SharedPkg', 'GenericPkg']

eSubpackages = []
eSuperPackage = None
sharedmodel.eSubpackages = eSubpackages
sharedmodel.eSuperPackage = eSuperPackage

SharedPkg.ownedDataPkg.eType = DataPkg
SharedPkg.ownedGenericPkg.eType = GenericPkg
GenericPkg.subGenericPkgs.eType = GenericPkg
GenericPkg.capellaElements.eType = CapellaElement

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
