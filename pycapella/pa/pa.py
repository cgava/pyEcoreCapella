print('pa.pa loading')
"""Definition of meta model 'pa'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacommon import CapabilityRealizationInvolvedElement
from cs import AbstractPhysicalArtifact, ArchitectureAllocation, BlockArchitecturePkg, Component, ComponentArchitecture, ComponentPkg, DeployableElement, DeploymentTarget, InterfaceAllocation
from fa import AbstractFunction, FunctionPkg
from information import AssociationPkg


name = 'pa'
nsURI = 'http://www.polarsys.org/capella/core/pa/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.pa'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
PhysicalComponentKind = EEnum('PhysicalComponentKind', literals=['UNSET', 'HARDWARE', 'HARDWARE_COMPUTER', 'SOFTWARE', 'SOFTWARE_DEPLOYMENT_UNIT',
                                                                 'SOFTWARE_EXECUTION_UNIT', 'SOFTWARE_APPLICATION', 'FIRMWARE', 'PERSON', 'FACILITIES', 'DATA', 'MATERIALS', 'SERVICES', 'PROCESSES'])

PhysicalComponentNature = EEnum('PhysicalComponentNature', literals=['UNSET', 'BEHAVIOR', 'NODE'])


class PhysicalFunctionPkg(FunctionPkg):

    ownedPhysicalFunctions = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedPhysicalFunctions=None, ownedPhysicalFunctionPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPhysicalFunctions:
            self.ownedPhysicalFunctions.extend(ownedPhysicalFunctions)

        if ownedPhysicalFunctionPkgs:
            self.ownedPhysicalFunctionPkgs.extend(ownedPhysicalFunctionPkgs)


class PhysicalArchitecturePkg(BlockArchitecturePkg):

    ownedPhysicalArchitecturePkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalArchitectures = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedPhysicalArchitecturePkgs=None, ownedPhysicalArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPhysicalArchitecturePkgs:
            self.ownedPhysicalArchitecturePkgs.extend(ownedPhysicalArchitecturePkgs)

        if ownedPhysicalArchitectures:
            self.ownedPhysicalArchitectures.extend(ownedPhysicalArchitectures)


class LogicalArchitectureRealization(ArchitectureAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class LogicalInterfaceRealization(InterfaceAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PhysicalComponentPkg(ComponentPkg, AssociationPkg):

    ownedPhysicalComponents = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedKeyParts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedDeployments = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedPhysicalComponents=None, ownedPhysicalComponentPkgs=None, ownedKeyParts=None, ownedDeployments=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPhysicalComponents:
            self.ownedPhysicalComponents.extend(ownedPhysicalComponents)

        if ownedPhysicalComponentPkgs:
            self.ownedPhysicalComponentPkgs.extend(ownedPhysicalComponentPkgs)

        if ownedKeyParts:
            self.ownedKeyParts.extend(ownedKeyParts)

        if ownedDeployments:
            self.ownedDeployments.extend(ownedDeployments)


class DerivedAllocatedlogicalarchitecturerealizations(EDerivedCollection):
    pass


class DerivedAllocatedlogicalarchitectures(EDerivedCollection):
    pass


class DerivedAllocatingepbsarchitectures(EDerivedCollection):
    pass


class PhysicalArchitecture(ComponentArchitecture):

    ownedPhysicalComponentPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    _containedCapabilityRealizationPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedCapabilityRealizationPkg', transient=True)
    _containedPhysicalFunctionPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedPhysicalFunctionPkg', transient=True)
    ownedDeployments = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedLogicalArchitectureRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedLogicalArchitectureRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedlogicalarchitecturerealizations)
    allocatedLogicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedlogicalarchitectures)
    allocatingEpbsArchitectures = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingepbsarchitectures)

    @property
    def containedCapabilityRealizationPkg(self):
        raise NotImplementedError('Missing implementation for containedCapabilityRealizationPkg')

    @property
    def containedPhysicalFunctionPkg(self):
        raise NotImplementedError('Missing implementation for containedPhysicalFunctionPkg')

    def __init__(self, *, ownedPhysicalComponentPkg=None, containedCapabilityRealizationPkg=None, containedPhysicalFunctionPkg=None, ownedDeployments=None, ownedLogicalArchitectureRealizations=None, allocatedLogicalArchitectureRealizations=None, allocatedLogicalArchitectures=None, allocatingEpbsArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPhysicalComponentPkg is not None:
            self.ownedPhysicalComponentPkg = ownedPhysicalComponentPkg

        if containedCapabilityRealizationPkg is not None:
            self.containedCapabilityRealizationPkg = containedCapabilityRealizationPkg

        if containedPhysicalFunctionPkg is not None:
            self.containedPhysicalFunctionPkg = containedPhysicalFunctionPkg

        if ownedDeployments:
            self.ownedDeployments.extend(ownedDeployments)

        if ownedLogicalArchitectureRealizations:
            self.ownedLogicalArchitectureRealizations.extend(ownedLogicalArchitectureRealizations)

        if allocatedLogicalArchitectureRealizations:
            self.allocatedLogicalArchitectureRealizations.extend(
                allocatedLogicalArchitectureRealizations)

        if allocatedLogicalArchitectures:
            self.allocatedLogicalArchitectures.extend(allocatedLogicalArchitectures)

        if allocatingEpbsArchitectures:
            self.allocatingEpbsArchitectures.extend(allocatingEpbsArchitectures)


class DerivedLogicalinterfacerealizations(EDerivedCollection):
    pass


class DerivedSubphysicalcomponents(EDerivedCollection):
    pass


class DerivedRealizedlogicalcomponents(EDerivedCollection):
    pass


class DerivedAllocatedphysicalfunctions(EDerivedCollection):
    pass


class DerivedDeployedphysicalcomponents(EDerivedCollection):
    pass


class DerivedDeployingphysicalcomponents(EDerivedCollection):
    pass


class PhysicalComponent(AbstractPhysicalArtifact, Component, CapabilityRealizationInvolvedElement, DeployableElement, DeploymentTarget):

    kind = EAttribute(eType=PhysicalComponentKind, unique=True, derived=False, changeable=True)
    nature = EAttribute(eType=PhysicalComponentNature, unique=True, derived=False, changeable=True)
    ownedDeploymentLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedPhysicalComponents = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedPhysicalComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    logicalInterfaceRealizations = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedLogicalinterfacerealizations)
    subPhysicalComponents = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedSubphysicalcomponents)
    realizedLogicalComponents = EReference(ordered=False, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizedlogicalcomponents)
    allocatedPhysicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedphysicalfunctions)
    deployedPhysicalComponents = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedDeployedphysicalcomponents)
    deployingPhysicalComponents = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedDeployingphysicalcomponents)

    def __init__(self, *, kind=None, nature=None, ownedDeploymentLinks=None, ownedPhysicalComponents=None, ownedPhysicalComponentPkgs=None, logicalInterfaceRealizations=None, subPhysicalComponents=None, realizedLogicalComponents=None, allocatedPhysicalFunctions=None, deployedPhysicalComponents=None, deployingPhysicalComponents=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if nature is not None:
            self.nature = nature

        if ownedDeploymentLinks:
            self.ownedDeploymentLinks.extend(ownedDeploymentLinks)

        if ownedPhysicalComponents:
            self.ownedPhysicalComponents.extend(ownedPhysicalComponents)

        if ownedPhysicalComponentPkgs:
            self.ownedPhysicalComponentPkgs.extend(ownedPhysicalComponentPkgs)

        if logicalInterfaceRealizations:
            self.logicalInterfaceRealizations.extend(logicalInterfaceRealizations)

        if subPhysicalComponents:
            self.subPhysicalComponents.extend(subPhysicalComponents)

        if realizedLogicalComponents:
            self.realizedLogicalComponents.extend(realizedLogicalComponents)

        if allocatedPhysicalFunctions:
            self.allocatedPhysicalFunctions.extend(allocatedPhysicalFunctions)

        if deployedPhysicalComponents:
            self.deployedPhysicalComponents.extend(deployedPhysicalComponents)

        if deployingPhysicalComponents:
            self.deployingPhysicalComponents.extend(deployingPhysicalComponents)


class DerivedSubphysicalnodes(EDerivedCollection):
    pass


class PhysicalNode(PhysicalComponent):

    subPhysicalNodes = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedSubphysicalnodes)

    def __init__(self, *, subPhysicalNodes=None, **kwargs):

        super().__init__(**kwargs)

        if subPhysicalNodes:
            self.subPhysicalNodes.extend(subPhysicalNodes)


class DerivedAllocatingphysicalcomponents(EDerivedCollection):
    pass


class DerivedRealizedlogicalfunctions(EDerivedCollection):
    pass


class DerivedContainedphysicalfunctions(EDerivedCollection):
    pass


class DerivedChildrenphysicalfunctions(EDerivedCollection):
    pass


class PhysicalFunction(AbstractFunction):

    ownedPhysicalFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatingPhysicalComponents = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingphysicalcomponents)
    realizedLogicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedRealizedlogicalfunctions)
    containedPhysicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedContainedphysicalfunctions)
    childrenPhysicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedChildrenphysicalfunctions)

    def __init__(self, *, ownedPhysicalFunctionPkgs=None, allocatingPhysicalComponents=None, realizedLogicalFunctions=None, containedPhysicalFunctions=None, childrenPhysicalFunctions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedPhysicalFunctionPkgs:
            self.ownedPhysicalFunctionPkgs.extend(ownedPhysicalFunctionPkgs)

        if allocatingPhysicalComponents:
            self.allocatingPhysicalComponents.extend(allocatingPhysicalComponents)

        if realizedLogicalFunctions:
            self.realizedLogicalFunctions.extend(realizedLogicalFunctions)

        if containedPhysicalFunctions:
            self.containedPhysicalFunctions.extend(containedPhysicalFunctions)

        if childrenPhysicalFunctions:
            self.childrenPhysicalFunctions.extend(childrenPhysicalFunctions)

print('pa.pa loaded')
