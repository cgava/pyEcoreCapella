print('ctx.ctx loading')
"""Definition of meta model 'ctx'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacommon import AbstractCapabilityPkg
from capellacore import InvolvedElement, Involvement, InvolverElement, NamedElement, Relationship, Structure
from cs import ArchitectureAllocation, Component, ComponentArchitecture, ComponentPkg
from fa import AbstractFunction, FunctionPkg
from interaction import AbstractCapability


name = 'ctx'
nsURI = 'http://www.polarsys.org/capella/core/ctx/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.ctx'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class SystemCommunicationHook(NamedElement):

    communication = EReference(ordered=True, unique=True, containment=False, derived=False)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, communication=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if communication is not None:
            self.communication = communication

        if type is not None:
            self.type = type


class SystemCommunication(Relationship):

    ends = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ends=None, **kwargs):

        super().__init__(**kwargs)

        if ends:
            self.ends.extend(ends)


class CapabilityExploitation(Relationship):

    _mission = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='mission', transient=True)
    capability = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def mission(self):
        raise NotImplementedError('Missing implementation for mission')

    def __init__(self, *, mission=None, capability=None, **kwargs):

        super().__init__(**kwargs)

        if mission is not None:
            self.mission = mission

        if capability is not None:
            self.capability = capability


class CapabilityInvolvement(Involvement):

    _systemComponent = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='systemComponent', transient=True)
    _capability = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='capability', transient=True)

    @property
    def systemComponent(self):
        raise NotImplementedError('Missing implementation for systemComponent')

    @property
    def capability(self):
        raise NotImplementedError('Missing implementation for capability')

    def __init__(self, *, systemComponent=None, capability=None, **kwargs):

        super().__init__(**kwargs)

        if systemComponent is not None:
            self.systemComponent = systemComponent

        if capability is not None:
            self.capability = capability


class MissionInvolvement(Involvement):

    _systemComponent = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='systemComponent', transient=True)
    _mission = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='mission', transient=True)

    @property
    def systemComponent(self):
        raise NotImplementedError('Missing implementation for systemComponent')

    @property
    def mission(self):
        raise NotImplementedError('Missing implementation for mission')

    def __init__(self, *, systemComponent=None, mission=None, **kwargs):

        super().__init__(**kwargs)

        if systemComponent is not None:
            self.systemComponent = systemComponent

        if mission is not None:
            self.mission = mission


class DerivedInvolvedsystemcomponents(EDerivedCollection):
    pass


class DerivedExploitedcapabilities(EDerivedCollection):
    pass


class Mission(NamedElement, InvolverElement):

    ownedMissionInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    involvedSystemComponents = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedsystemcomponents)
    ownedCapabilityExploitations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    exploitedCapabilities = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedExploitedcapabilities)

    def __init__(self, *, ownedMissionInvolvements=None, involvedSystemComponents=None, ownedCapabilityExploitations=None, exploitedCapabilities=None, **kwargs):

        super().__init__(**kwargs)

        if ownedMissionInvolvements:
            self.ownedMissionInvolvements.extend(ownedMissionInvolvements)

        if involvedSystemComponents:
            self.involvedSystemComponents.extend(involvedSystemComponents)

        if ownedCapabilityExploitations:
            self.ownedCapabilityExploitations.extend(ownedCapabilityExploitations)

        if exploitedCapabilities:
            self.exploitedCapabilities.extend(exploitedCapabilities)


class MissionPkg(Structure):

    ownedMissionPkgs = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedMissions = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedMissionPkgs=None, ownedMissions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedMissionPkgs:
            self.ownedMissionPkgs.extend(ownedMissionPkgs)

        if ownedMissions:
            self.ownedMissions.extend(ownedMissions)


class SystemFunctionPkg(FunctionPkg):

    ownedSystemFunctions = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedSystemFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedSystemFunctions=None, ownedSystemFunctionPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedSystemFunctions:
            self.ownedSystemFunctions.extend(ownedSystemFunctions)

        if ownedSystemFunctionPkgs:
            self.ownedSystemFunctionPkgs.extend(ownedSystemFunctionPkgs)


class CapabilityPkg(AbstractCapabilityPkg):

    ownedCapabilities = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)
    ownedCapabilityPkgs = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedCapabilities=None, ownedCapabilityPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedCapabilities:
            self.ownedCapabilities.extend(ownedCapabilities)

        if ownedCapabilityPkgs:
            self.ownedCapabilityPkgs.extend(ownedCapabilityPkgs)


class SystemComponentPkg(ComponentPkg):

    ownedSystemComponents = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    ownedSystemComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedSystemComponents=None, ownedSystemComponentPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedSystemComponents:
            self.ownedSystemComponents.extend(ownedSystemComponents)

        if ownedSystemComponentPkgs:
            self.ownedSystemComponentPkgs.extend(ownedSystemComponentPkgs)


class OperationalAnalysisRealization(ArchitectureAllocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedAllocatedoperationalanalysisrealizations(EDerivedCollection):
    pass


class DerivedAllocatedoperationalanalyses(EDerivedCollection):
    pass


class DerivedAllocatinglogicalarchitectures(EDerivedCollection):
    pass


class SystemAnalysis(ComponentArchitecture):

    ownedSystemComponentPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMissionPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    _containedCapabilityPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedCapabilityPkg', transient=True)
    _containedSystemFunctionPkg = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='containedSystemFunctionPkg', transient=True)
    ownedOperationalAnalysisRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedOperationalAnalysisRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedoperationalanalysisrealizations)
    allocatedOperationalAnalyses = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedoperationalanalyses)
    allocatingLogicalArchitectures = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedAllocatinglogicalarchitectures)

    @property
    def containedCapabilityPkg(self):
        raise NotImplementedError('Missing implementation for containedCapabilityPkg')

    @property
    def containedSystemFunctionPkg(self):
        raise NotImplementedError('Missing implementation for containedSystemFunctionPkg')

    def __init__(self, *, ownedSystemComponentPkg=None, ownedMissionPkg=None, containedCapabilityPkg=None, containedSystemFunctionPkg=None, ownedOperationalAnalysisRealizations=None, allocatedOperationalAnalysisRealizations=None, allocatedOperationalAnalyses=None, allocatingLogicalArchitectures=None, **kwargs):

        super().__init__(**kwargs)

        if ownedSystemComponentPkg is not None:
            self.ownedSystemComponentPkg = ownedSystemComponentPkg

        if ownedMissionPkg is not None:
            self.ownedMissionPkg = ownedMissionPkg

        if containedCapabilityPkg is not None:
            self.containedCapabilityPkg = containedCapabilityPkg

        if containedSystemFunctionPkg is not None:
            self.containedSystemFunctionPkg = containedSystemFunctionPkg

        if ownedOperationalAnalysisRealizations:
            self.ownedOperationalAnalysisRealizations.extend(ownedOperationalAnalysisRealizations)

        if allocatedOperationalAnalysisRealizations:
            self.allocatedOperationalAnalysisRealizations.extend(
                allocatedOperationalAnalysisRealizations)

        if allocatedOperationalAnalyses:
            self.allocatedOperationalAnalyses.extend(allocatedOperationalAnalyses)

        if allocatingLogicalArchitectures:
            self.allocatingLogicalArchitectures.extend(allocatingLogicalArchitectures)


class DerivedInvolvedsystemcomponents(EDerivedCollection):
    pass


class DerivedPurposes(EDerivedCollection):
    pass


class DerivedPurposemissions(EDerivedCollection):
    pass


class DerivedRealizedoperationalcapabilities(EDerivedCollection):
    pass


class DerivedRealizingcapabilityrealizations(EDerivedCollection):
    pass


class Capability(AbstractCapability):

    ownedCapabilityInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    involvedSystemComponents = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedsystemcomponents)
    purposes = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedPurposes)
    purposeMissions = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedPurposemissions)
    realizedOperationalCapabilities = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedRealizedoperationalcapabilities)
    realizingCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcapabilityrealizations)

    def __init__(self, *, ownedCapabilityInvolvements=None, involvedSystemComponents=None, purposes=None, purposeMissions=None, realizedOperationalCapabilities=None, realizingCapabilityRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if ownedCapabilityInvolvements:
            self.ownedCapabilityInvolvements.extend(ownedCapabilityInvolvements)

        if involvedSystemComponents:
            self.involvedSystemComponents.extend(involvedSystemComponents)

        if purposes:
            self.purposes.extend(purposes)

        if purposeMissions:
            self.purposeMissions.extend(purposeMissions)

        if realizedOperationalCapabilities:
            self.realizedOperationalCapabilities.extend(realizedOperationalCapabilities)

        if realizingCapabilityRealizations:
            self.realizingCapabilityRealizations.extend(realizingCapabilityRealizations)


class DerivedInvolvingcapabilities(EDerivedCollection):
    pass


class DerivedCapabilityinvolvements(EDerivedCollection):
    pass


class DerivedInvolvingmissions(EDerivedCollection):
    pass


class DerivedMissioninvolvements(EDerivedCollection):
    pass


class DerivedRealizedentities(EDerivedCollection):
    pass


class DerivedRealizinglogicalcomponents(EDerivedCollection):
    pass


class DerivedAllocatedsystemfunctions(EDerivedCollection):
    pass


class SystemComponent(Component, InvolvedElement):

    dataComponent = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedSystemComponents = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    ownedSystemComponentPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    dataType = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    involvingCapabilities = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilities)
    capabilityInvolvements = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedCapabilityinvolvements)
    involvingMissions = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingmissions)
    missionInvolvements = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedMissioninvolvements)
    realizedEntities = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedRealizedentities)
    realizingLogicalComponents = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedRealizinglogicalcomponents)
    allocatedSystemFunctions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedsystemfunctions)

    def __init__(self, *, ownedSystemComponents=None, ownedSystemComponentPkgs=None, dataComponent=None, dataType=None, involvingCapabilities=None, capabilityInvolvements=None, involvingMissions=None, missionInvolvements=None, realizedEntities=None, realizingLogicalComponents=None, allocatedSystemFunctions=None, **kwargs):

        super().__init__(**kwargs)

        if dataComponent is not None:
            self.dataComponent = dataComponent

        if ownedSystemComponents:
            self.ownedSystemComponents.extend(ownedSystemComponents)

        if ownedSystemComponentPkgs:
            self.ownedSystemComponentPkgs.extend(ownedSystemComponentPkgs)

        if dataType:
            self.dataType.extend(dataType)

        if involvingCapabilities:
            self.involvingCapabilities.extend(involvingCapabilities)

        if capabilityInvolvements:
            self.capabilityInvolvements.extend(capabilityInvolvements)

        if involvingMissions:
            self.involvingMissions.extend(involvingMissions)

        if missionInvolvements:
            self.missionInvolvements.extend(missionInvolvements)

        if realizedEntities:
            self.realizedEntities.extend(realizedEntities)

        if realizingLogicalComponents:
            self.realizingLogicalComponents.extend(realizingLogicalComponents)

        if allocatedSystemFunctions:
            self.allocatedSystemFunctions.extend(allocatedSystemFunctions)


class DerivedAllocatingsystemcomponents(EDerivedCollection):
    pass


class DerivedRealizedoperationalactivities(EDerivedCollection):
    pass


class DerivedRealizinglogicalfunctions(EDerivedCollection):
    pass


class DerivedContainedsystemfunctions(EDerivedCollection):
    pass


class DerivedChildrensystemfunctions(EDerivedCollection):
    pass


class SystemFunction(AbstractFunction):

    ownedSystemFunctionPkgs = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatingSystemComponents = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingsystemcomponents)
    realizedOperationalActivities = EReference(ordered=True, unique=True, containment=False,
                                               derived=True, upper=-1, transient=True, derived_class=DerivedRealizedoperationalactivities)
    realizingLogicalFunctions = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizinglogicalfunctions)
    containedSystemFunctions = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedContainedsystemfunctions)
    childrenSystemFunctions = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedChildrensystemfunctions)

    def __init__(self, *, ownedSystemFunctionPkgs=None, allocatingSystemComponents=None, realizedOperationalActivities=None, realizingLogicalFunctions=None, containedSystemFunctions=None, childrenSystemFunctions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedSystemFunctionPkgs:
            self.ownedSystemFunctionPkgs.extend(ownedSystemFunctionPkgs)

        if allocatingSystemComponents:
            self.allocatingSystemComponents.extend(allocatingSystemComponents)

        if realizedOperationalActivities:
            self.realizedOperationalActivities.extend(realizedOperationalActivities)

        if realizingLogicalFunctions:
            self.realizingLogicalFunctions.extend(realizingLogicalFunctions)

        if containedSystemFunctions:
            self.containedSystemFunctions.extend(containedSystemFunctions)

        if childrenSystemFunctions:
            self.childrenSystemFunctions.extend(childrenSystemFunctions)

print('ctx.ctx loaded')
