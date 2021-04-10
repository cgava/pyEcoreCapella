"""Definition of meta model 'epbs'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pycapella2.capellacommon import CapabilityRealizationInvolvedElement
from pycapella2.capellacore import Allocation
from pycapella2.cs import ArchitectureAllocation, BlockArchitecturePkg, Component, ComponentArchitecture, ComponentPkg


name = 'epbs'
nsURI = 'http://www.polarsys.org/capella/core/epbs/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.epbs'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ConfigurationItemKind = EEnum('ConfigurationItemKind', literals=[
                              'Unset', 'COTSCI', 'CSCI', 'HWCI', 'InterfaceCI', 'NDICI', 'PrimeItemCI', 'SystemCI'])


class ConfigurationItemPkg(ComponentPkg):

    ownedConfigurationItems = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConfigurationItemPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedConfigurationItems=None, ownedConfigurationItemPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedConfigurationItems:
            self.ownedConfigurationItems.extend(ownedConfigurationItems)

        if ownedConfigurationItemPkgs:
            self.ownedConfigurationItemPkgs.extend(ownedConfigurationItemPkgs)


class PhysicalArtifactRealization(Allocation):

    _realizedPhysicalArtifact = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedPhysicalArtifact', transient=True)
    _realizingConfigurationItem = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingConfigurationItem', transient=True)

    @property
    def realizedPhysicalArtifact(self):
        raise NotImplementedError('Missing implementation for realizedPhysicalArtifact')

    @property
    def realizingConfigurationItem(self):
        raise NotImplementedError('Missing implementation for realizingConfigurationItem')

    def __init__(self, *, realizedPhysicalArtifact=None, realizingConfigurationItem=None, **kwargs):

        super().__init__(**kwargs)

        if realizedPhysicalArtifact is not None:
            self.realizedPhysicalArtifact = realizedPhysicalArtifact

        if realizingConfigurationItem is not None:
            self.realizingConfigurationItem = realizingConfigurationItem


class EPBSArchitecturePkg(BlockArchitecturePkg):

    ownedEPBSArchitectures = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedEPBSArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedEPBSArchitectures:
            self.ownedEPBSArchitectures.extend(ownedEPBSArchitectures)


class PhysicalArchitectureRealization(ArchitectureAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedAllocatedphysicalarchitecturerealizations(EDerivedCollection):
    pass


class DerivedAllocatedphysicalarchitectures(EDerivedCollection):
    pass


class EPBSArchitecture(ComponentArchitecture):

    ownedConfigurationItemPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    _containedCapabilityRealizationPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedCapabilityRealizationPkg', transient=True)
    ownedPhysicalArchitectureRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedPhysicalArchitectureRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedphysicalarchitecturerealizations)
    allocatedPhysicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedphysicalarchitectures)

    @property
    def containedCapabilityRealizationPkg(self):
        raise NotImplementedError('Missing implementation for containedCapabilityRealizationPkg')

    def __init__(self, *, ownedConfigurationItemPkg=None, containedCapabilityRealizationPkg=None, ownedPhysicalArchitectureRealizations=None, allocatedPhysicalArchitectureRealizations=None, allocatedPhysicalArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedConfigurationItemPkg is not None:
            self.ownedConfigurationItemPkg = ownedConfigurationItemPkg

        if containedCapabilityRealizationPkg is not None:
            self.containedCapabilityRealizationPkg = containedCapabilityRealizationPkg

        if ownedPhysicalArchitectureRealizations:
            self.ownedPhysicalArchitectureRealizations.extend(ownedPhysicalArchitectureRealizations)

        if allocatedPhysicalArchitectureRealizations:
            self.allocatedPhysicalArchitectureRealizations.extend(
                allocatedPhysicalArchitectureRealizations)

        if allocatedPhysicalArchitectures:
            self.allocatedPhysicalArchitectures.extend(allocatedPhysicalArchitectures)


class DerivedAllocatedphysicalartifacts(EDerivedCollection):
    pass


class ConfigurationItem(CapabilityRealizationInvolvedElement, Component):

    itemIdentifier = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    kind = EAttribute(eType=ConfigurationItemKind, unique=True, derived=False,
                      changeable=True, default_value=ConfigurationItemKind.Unset)
    ownedConfigurationItems = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedConfigurationItemPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalArtifactRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedPhysicalArtifacts = EReference(ordered=False, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedphysicalartifacts)

    def __init__(self, *, itemIdentifier=None, kind=None, ownedConfigurationItems=None, ownedConfigurationItemPkgs=None, ownedPhysicalArtifactRealizations=None, allocatedPhysicalArtifacts=None, **kwargs):

        super().__init__(**kwargs)

        if itemIdentifier is not None:
            self.itemIdentifier = itemIdentifier

        if kind is not None:
            self.kind = kind

        if ownedConfigurationItems:
            self.ownedConfigurationItems.extend(ownedConfigurationItems)

        if ownedConfigurationItemPkgs:
            self.ownedConfigurationItemPkgs.extend(ownedConfigurationItemPkgs)

        if ownedPhysicalArtifactRealizations:
            self.ownedPhysicalArtifactRealizations.extend(ownedPhysicalArtifactRealizations)

        if allocatedPhysicalArtifacts:
            self.allocatedPhysicalArtifacts.extend(allocatedPhysicalArtifacts)
