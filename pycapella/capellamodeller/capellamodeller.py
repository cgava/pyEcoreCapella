"""Definition of meta model 'capellamodeller'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import AbstractModellingStructure, CapellaElement, Structure


name = 'capellamodeller'
nsURI = 'http://www.polarsys.org/capella/core/modeller/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.capellamodeller'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class ModelRoot(CapellaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Project(Structure):

    keyValuePairs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFolders = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedModelRoots = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, keyValuePairs=None, ownedFolders=None, ownedModelRoots=None, **kwargs):

        super().__init__(**kwargs)

        if keyValuePairs:
            self.keyValuePairs.extend(keyValuePairs)

        if ownedFolders:
            self.ownedFolders.extend(ownedFolders)

        if ownedModelRoots:
            self.ownedModelRoots.extend(ownedModelRoots)


class Folder(Structure):

    ownedFolders = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedModelRoots = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedFolders=None, ownedModelRoots=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFolders:
            self.ownedFolders.extend(ownedFolders)

        if ownedModelRoots:
            self.ownedModelRoots.extend(ownedModelRoots)


class Library(Project):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SystemEngineeringPkg(Structure, ModelRoot):

    ownedSystemEngineerings = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedSystemEngineerings=None, **kwargs):

        super().__init__(**kwargs)

        if ownedSystemEngineerings:
            self.ownedSystemEngineerings.extend(ownedSystemEngineerings)


class DerivedContainedoperationalanalysis(EDerivedCollection):
    pass


class DerivedContainedsystemanalysis(EDerivedCollection):
    pass


class DerivedContainedlogicalarchitectures(EDerivedCollection):
    pass


class DerivedContainedphysicalarchitectures(EDerivedCollection):
    pass


class DerivedContainedepbsarchitectures(EDerivedCollection):
    pass


class DerivedContainedsharedpkgs(EDerivedCollection):
    pass


class SystemEngineering(AbstractModellingStructure, ModelRoot):

    containedOperationalAnalysis = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedContainedoperationalanalysis)
    containedSystemAnalysis = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedContainedsystemanalysis)
    containedLogicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedContainedlogicalarchitectures)
    containedPhysicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedContainedphysicalarchitectures)
    containedEPBSArchitectures = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedContainedepbsarchitectures)
    containedSharedPkgs = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedContainedsharedpkgs)

    def __init__(self, *, containedOperationalAnalysis=None, containedSystemAnalysis=None, containedLogicalArchitectures=None, containedPhysicalArchitectures=None, containedEPBSArchitectures=None, containedSharedPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if containedOperationalAnalysis:
            self.containedOperationalAnalysis.extend(containedOperationalAnalysis)

        if containedSystemAnalysis:
            self.containedSystemAnalysis.extend(containedSystemAnalysis)

        if containedLogicalArchitectures:
            self.containedLogicalArchitectures.extend(containedLogicalArchitectures)

        if containedPhysicalArchitectures:
            self.containedPhysicalArchitectures.extend(containedPhysicalArchitectures)

        if containedEPBSArchitectures:
            self.containedEPBSArchitectures.extend(containedEPBSArchitectures)

        if containedSharedPkgs:
            self.containedSharedPkgs.extend(containedSharedPkgs)
