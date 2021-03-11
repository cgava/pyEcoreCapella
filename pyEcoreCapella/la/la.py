print('la.la loading')
"""Definition of meta model 'la'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacommon import AbstractCapabilityPkg, CapabilityRealizationInvolvedElement
from cs import ArchitectureAllocation, BlockArchitecturePkg, Component, ComponentArchitecture, ComponentPkg, InterfaceAllocation
from fa import AbstractFunction, FunctionPkg
from interaction import AbstractCapability


name = 'la'
nsURI = 'http://www.polarsys.org/capella/core/la/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.la'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class LogicalFunctionPkg(FunctionPkg):

    ownedLogicalFunctions = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    ownedLogicalFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedLogicalFunctions=None, ownedLogicalFunctionPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalFunctions:
            self.ownedLogicalFunctions.extend(ownedLogicalFunctions)

        if ownedLogicalFunctionPkgs:
            self.ownedLogicalFunctionPkgs.extend(ownedLogicalFunctionPkgs)


class LogicalComponentPkg(ComponentPkg):

    ownedLogicalComponents = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedLogicalComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedLogicalComponents=None, ownedLogicalComponentPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalComponents:
            self.ownedLogicalComponents.extend(ownedLogicalComponents)

        if ownedLogicalComponentPkgs:
            self.ownedLogicalComponentPkgs.extend(ownedLogicalComponentPkgs)


class CapabilityRealizationPkg(AbstractCapabilityPkg):

    ownedCapabilityRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedCapabilityRealizationPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedCapabilityRealizations=None, ownedCapabilityRealizationPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedCapabilityRealizations:
            self.ownedCapabilityRealizations.extend(ownedCapabilityRealizations)

        if ownedCapabilityRealizationPkgs:
            self.ownedCapabilityRealizationPkgs.extend(ownedCapabilityRealizationPkgs)


class LogicalArchitecturePkg(BlockArchitecturePkg):

    ownedLogicalArchitectures = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedLogicalArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalArchitectures:
            self.ownedLogicalArchitectures.extend(ownedLogicalArchitectures)


class SystemAnalysisRealization(ArchitectureAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ContextInterfaceRealization(InterfaceAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedAllocatedsystemanalysisrealizations(EDerivedCollection):
    pass


class DerivedAllocatedsystemanalyses(EDerivedCollection):
    pass


class DerivedAllocatingphysicalarchitectures(EDerivedCollection):
    pass


class LogicalArchitecture(ComponentArchitecture):

    ownedLogicalComponentPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)
    _containedCapabilityRealizationPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedCapabilityRealizationPkg', transient=True)
    _containedLogicalFunctionPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedLogicalFunctionPkg', transient=True)
    ownedSystemAnalysisRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedSystemAnalysisRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedsystemanalysisrealizations)
    allocatedSystemAnalyses = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedsystemanalyses)
    allocatingPhysicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingphysicalarchitectures)

    @property
    def containedCapabilityRealizationPkg(self):
        raise NotImplementedError('Missing implementation for containedCapabilityRealizationPkg')

    @property
    def containedLogicalFunctionPkg(self):
        raise NotImplementedError('Missing implementation for containedLogicalFunctionPkg')

    def __init__(self, *, ownedLogicalComponentPkg=None, containedCapabilityRealizationPkg=None, containedLogicalFunctionPkg=None, ownedSystemAnalysisRealizations=None, allocatedSystemAnalysisRealizations=None, allocatedSystemAnalyses=None, allocatingPhysicalArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalComponentPkg is not None:
            self.ownedLogicalComponentPkg = ownedLogicalComponentPkg

        if containedCapabilityRealizationPkg is not None:
            self.containedCapabilityRealizationPkg = containedCapabilityRealizationPkg

        if containedLogicalFunctionPkg is not None:
            self.containedLogicalFunctionPkg = containedLogicalFunctionPkg

        if ownedSystemAnalysisRealizations:
            self.ownedSystemAnalysisRealizations.extend(ownedSystemAnalysisRealizations)

        if allocatedSystemAnalysisRealizations:
            self.allocatedSystemAnalysisRealizations.extend(allocatedSystemAnalysisRealizations)

        if allocatedSystemAnalyses:
            self.allocatedSystemAnalyses.extend(allocatedSystemAnalyses)

        if allocatingPhysicalArchitectures:
            self.allocatingPhysicalArchitectures.extend(allocatingPhysicalArchitectures)


class DerivedInvolvedcomponents(EDerivedCollection):
    pass


class DerivedRealizedcapabilities(EDerivedCollection):
    pass


class DerivedRealizedcapabilityrealizations(EDerivedCollection):
    pass


class DerivedRealizingcapabilityrealizations(EDerivedCollection):
    pass


class CapabilityRealization(AbstractCapability):

    ownedCapabilityRealizationInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    involvedComponents = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedcomponents)
    realizedCapabilities = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcapabilities)
    realizedCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcapabilityrealizations)
    realizingCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcapabilityrealizations)

    def __init__(self, *, ownedCapabilityRealizationInvolvements=None, involvedComponents=None, realizedCapabilities=None, realizedCapabilityRealizations=None, realizingCapabilityRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if ownedCapabilityRealizationInvolvements:
            self.ownedCapabilityRealizationInvolvements.extend(
                ownedCapabilityRealizationInvolvements)

        if involvedComponents:
            self.involvedComponents.extend(involvedComponents)

        if realizedCapabilities:
            self.realizedCapabilities.extend(realizedCapabilities)

        if realizedCapabilityRealizations:
            self.realizedCapabilityRealizations.extend(realizedCapabilityRealizations)

        if realizingCapabilityRealizations:
            self.realizingCapabilityRealizations.extend(realizingCapabilityRealizations)


class DerivedSublogicalcomponents(EDerivedCollection):
    pass


class DerivedAllocatedlogicalfunctions(EDerivedCollection):
    pass


class DerivedRealizedsystemcomponents(EDerivedCollection):
    pass


class DerivedRealizingphysicalcomponents(EDerivedCollection):
    pass


class LogicalComponent(Component, CapabilityRealizationInvolvedElement):

    ownedLogicalComponents = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedLogicalArchitectures = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedLogicalComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    subLogicalComponents = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedSublogicalcomponents)
    allocatedLogicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedlogicalfunctions)
    realizedSystemComponents = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedRealizedsystemcomponents)
    realizingPhysicalComponents = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicalcomponents)

    def __init__(self, *, ownedLogicalComponents=None, ownedLogicalArchitectures=None, ownedLogicalComponentPkgs=None, subLogicalComponents=None, allocatedLogicalFunctions=None, realizedSystemComponents=None, realizingPhysicalComponents=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalComponents:
            self.ownedLogicalComponents.extend(ownedLogicalComponents)

        if ownedLogicalArchitectures:
            self.ownedLogicalArchitectures.extend(ownedLogicalArchitectures)

        if ownedLogicalComponentPkgs:
            self.ownedLogicalComponentPkgs.extend(ownedLogicalComponentPkgs)

        if subLogicalComponents:
            self.subLogicalComponents.extend(subLogicalComponents)

        if allocatedLogicalFunctions:
            self.allocatedLogicalFunctions.extend(allocatedLogicalFunctions)

        if realizedSystemComponents:
            self.realizedSystemComponents.extend(realizedSystemComponents)

        if realizingPhysicalComponents:
            self.realizingPhysicalComponents.extend(realizingPhysicalComponents)


class DerivedAllocatinglogicalcomponents(EDerivedCollection):
    pass


class DerivedRealizedsystemfunctions(EDerivedCollection):
    pass


class DerivedRealizingphysicalfunctions(EDerivedCollection):
    pass


class DerivedContainedlogicalfunctions(EDerivedCollection):
    pass


class DerivedChildrenlogicalfunctions(EDerivedCollection):
    pass


class LogicalFunction(AbstractFunction):

    ownedLogicalFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatingLogicalComponents = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedAllocatinglogicalcomponents)
    realizedSystemFunctions = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedRealizedsystemfunctions)
    realizingPhysicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedRealizingphysicalfunctions)
    containedLogicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedContainedlogicalfunctions)
    childrenLogicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedChildrenlogicalfunctions)

    def __init__(self, *, ownedLogicalFunctionPkgs=None, allocatingLogicalComponents=None, realizedSystemFunctions=None, realizingPhysicalFunctions=None, containedLogicalFunctions=None, childrenLogicalFunctions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLogicalFunctionPkgs:
            self.ownedLogicalFunctionPkgs.extend(ownedLogicalFunctionPkgs)

        if allocatingLogicalComponents:
            self.allocatingLogicalComponents.extend(allocatingLogicalComponents)

        if realizedSystemFunctions:
            self.realizedSystemFunctions.extend(realizedSystemFunctions)

        if realizingPhysicalFunctions:
            self.realizingPhysicalFunctions.extend(realizingPhysicalFunctions)

        if containedLogicalFunctions:
            self.containedLogicalFunctions.extend(containedLogicalFunctions)

        if childrenLogicalFunctions:
            self.childrenLogicalFunctions.extend(childrenLogicalFunctions)

print('la.la loaded')
