
from .capellamodeller import getEClassifier, eClassifiers
from .capellamodeller import name, nsURI, nsPrefix, eClass
from .capellamodeller import Project, Folder, ModelRoot, SystemEngineering, SystemEngineeringPkg, Library

from capellacore import EnumerationPropertyLiteral, Trace, ModellingArchitecturePkg, AbstractPropertyValue, KeyValue, EnumerationPropertyType, NamingRule, PropertyValuePkg, ReuseLink, ModellingArchitecture, PropertyValueGroup
from capellacommon import GenericTrace
from modellingcore import AbstractTrace, AbstractConstraint, ModelElement
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from oa import OperationalAnalysis
from ctx import SystemAnalysis
from la import LogicalArchitecture
from pa import PhysicalArchitecture
from epbs import EPBSArchitecture
from sharedmodel import SharedPkg

from . import capellamodeller

__all__ = ['Project', 'Folder', 'ModelRoot', 'SystemEngineering', 'SystemEngineeringPkg', 'Library']

eSubpackages = []
eSuperPackage = None
capellamodeller.eSubpackages = eSubpackages
capellamodeller.eSuperPackage = eSuperPackage

Project.keyValuePairs.eType = KeyValue
Project.ownedFolders.eType = Folder
Project.ownedModelRoots.eType = ModelRoot
Folder.ownedFolders.eType = Folder
Folder.ownedModelRoots.eType = ModelRoot
SystemEngineering.containedOperationalAnalysis.eType = OperationalAnalysis
SystemEngineering.containedSystemAnalysis.eType = SystemAnalysis
SystemEngineering.containedLogicalArchitectures.eType = LogicalArchitecture
SystemEngineering.containedPhysicalArchitectures.eType = PhysicalArchitecture
SystemEngineering.containedEPBSArchitectures.eType = EPBSArchitecture
SystemEngineering.containedSharedPkgs.eType = SharedPkg
SystemEngineeringPkg.ownedSystemEngineerings.eType = SystemEngineering

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
