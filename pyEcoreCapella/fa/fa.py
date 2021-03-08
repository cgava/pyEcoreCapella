"""Definition of meta model 'fa'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from modellingcore import InformationsExchanger, AbstractType, AbstractRelationship, AbstractRelationship, AbstractTypedElement, AbstractType, FinalizableElement, TraceableElement, AbstractNamedElement, AbstractNamedElement, AbstractTrace, AbstractInformationFlow, ModelElement, AbstractTypedElement, PublishableElement, TraceableElement, TraceableElement, AbstractNamedElement, AbstractRelationship, AbstractNamedElement
from capellacore import Relationship, NamedElement, NamedRelationship, Relationship, InvolvedElement, TypedElement, InvolverElement, Type, Namespace, Structure, CapellaElement, Involvement, CapellaElement, ModellingArchitecture, ModellingBlock, Structure, NamedElement, Namespace, Feature, CapellaElement, TypedElement, Allocation, NamedElement
from activity import ExecutableNode, AbstractAction, CallBehaviorAction, ActivityNode, OutputPin, CallAction, ActivityEdge, AbstractActivity, Pin, InvocationAction, InputPin, ObjectNode, ActivityExchange, ObjectFlow
from information import MultiplicityElement, AbstractEventOperation, Port, AbstractInstance, Property, Property
from emde import ExtensibleElement, Element
from behavior import AbstractEvent, AbstractBehavior


name = 'fa'
nsURI = 'http://www.polarsys.org/capella/core/fa/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.fa'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
FunctionalChainKind = EEnum('FunctionalChainKind', literals=['SIMPLE', 'COMPOSITE', 'FRAGMENT'])

FunctionKind = EEnum('FunctionKind', literals=[
                     'FUNCTION', 'DUPLICATE', 'GATHER', 'SELECT', 'SPLIT', 'ROUTE'])

ComponentExchangeKind = EEnum('ComponentExchangeKind', literals=[
                              'UNSET', 'DELEGATION', 'ASSEMBLY', 'FLOW'])

ComponentPortKind = EEnum('ComponentPortKind', literals=['STANDARD', 'FLOW'])

OrientationPortKind = EEnum('OrientationPortKind', literals=['UNSET', 'IN', 'OUT', 'INOUT'])

ControlNodeKind = EEnum('ControlNodeKind', literals=['OR', 'AND', 'ITERATE'])


@abstract
class ReferenceHierarchyContext(EObject, metaclass=MetaEClass):

    sourceReferenceHierarchy = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    targetReferenceHierarchy = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, sourceReferenceHierarchy=None, targetReferenceHierarchy=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if sourceReferenceHierarchy:
            self.sourceReferenceHierarchy.extend(sourceReferenceHierarchy)

        if targetReferenceHierarchy:
            self.targetReferenceHierarchy.extend(targetReferenceHierarchy)


@abstract
class AbstractFunctionalChainContainer(CapellaElement):

    ownedFunctionalChains = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedFunctionalChains=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFunctionalChains:
            self.ownedFunctionalChains.extend(ownedFunctionalChains)


class ComponentPortAllocationEnd(CapellaElement):

    port = EReference(ordered=True, unique=True, containment=False, derived=False)
    part = EReference(ordered=True, unique=True, containment=False, derived=False)
    _owningComponentPortAllocation = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='owningComponentPortAllocation', transient=True)

    @property
    def owningComponentPortAllocation(self):
        raise NotImplementedError('Missing implementation for owningComponentPortAllocation')

    def __init__(self, *, port=None, part=None, owningComponentPortAllocation=None, **kwargs):

        super().__init__(**kwargs)

        if port is not None:
            self.port = port

        if part is not None:
            self.part = part

        if owningComponentPortAllocation is not None:
            self.owningComponentPortAllocation = owningComponentPortAllocation


@abstract
class SequenceLinkEnd(CapellaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ComponentExchangeEnd(InformationsExchanger, CapellaElement):

    port = EReference(ordered=True, unique=True, containment=False, derived=False)
    part = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, port=None, part=None, **kwargs):

        super().__init__(**kwargs)

        if port is not None:
            self.port = port

        if part is not None:
            self.part = part


class SequenceLink(CapellaElement, ReferenceHierarchyContext):

    condition = EReference(ordered=True, unique=True, containment=False, derived=False)
    links = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, condition=None, links=None, source=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if condition is not None:
            self.condition = condition

        if links:
            self.links.extend(links)

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target


class ControlNode(SequenceLinkEnd):

    kind = EAttribute(eType=ControlNodeKind, unique=True, derived=False, changeable=True)

    def __init__(self, *, kind=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind


class ExchangeCategory(NamedElement):

    exchanges = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, exchanges=None, **kwargs):

        super().__init__(**kwargs)

        if exchanges:
            self.exchanges.extend(exchanges)


class ExchangeContainment(Relationship):

    exchange = EReference(ordered=True, unique=True, containment=False, derived=False)
    link = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, exchange=None, link=None, **kwargs):

        super().__init__(**kwargs)

        if exchange is not None:
            self.exchange = exchange

        if link is not None:
            self.link = link


class DerivedAllocatedcomponentexchanges(EDerivedCollection):
    pass


@abstract
class ComponentExchangeAllocator(NamedElement):

    ownedComponentExchangeAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatedComponentExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedcomponentexchanges)

    def __init__(self, *, ownedComponentExchangeAllocations=None, allocatedComponentExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if ownedComponentExchangeAllocations:
            self.ownedComponentExchangeAllocations.extend(ownedComponentExchangeAllocations)

        if allocatedComponentExchanges:
            self.allocatedComponentExchanges.extend(allocatedComponentExchanges)


class ComponentExchangeCategory(NamedElement):

    exchanges = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, exchanges=None, **kwargs):

        super().__init__(**kwargs)

        if exchanges:
            self.exchanges.extend(exchanges)


class DerivedNextfunctionalchaininvolvements(EDerivedCollection):
    pass


class DerivedPreviousfunctionalchaininvolvements(EDerivedCollection):
    pass


@abstract
class FunctionalChainInvolvement(Involvement):

    nextFunctionalChainInvolvements = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedNextfunctionalchaininvolvements)
    previousFunctionalChainInvolvements = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedPreviousfunctionalchaininvolvements)
    _involvedElement = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, name='involvedElement', transient=True)

    @property
    def involvedElement(self):
        raise NotImplementedError('Missing implementation for involvedElement')

    def __init__(self, *, nextFunctionalChainInvolvements=None, previousFunctionalChainInvolvements=None, involvedElement=None, **kwargs):

        super().__init__(**kwargs)

        if nextFunctionalChainInvolvements:
            self.nextFunctionalChainInvolvements.extend(nextFunctionalChainInvolvements)

        if previousFunctionalChainInvolvements:
            self.previousFunctionalChainInvolvements.extend(previousFunctionalChainInvolvements)

        if involvedElement is not None:
            self.involvedElement = involvedElement


@abstract
class FunctionPkg(Structure):

    ownedFunctionalLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedExchanges = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    ownedExchangeSpecificationRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedCategories = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedFunctionSpecifications = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedFunctionalLinks=None, ownedExchanges=None, ownedExchangeSpecificationRealizations=None, ownedCategories=None, ownedFunctionSpecifications=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFunctionalLinks:
            self.ownedFunctionalLinks.extend(ownedFunctionalLinks)

        if ownedExchanges:
            self.ownedExchanges.extend(ownedExchanges)

        if ownedExchangeSpecificationRealizations:
            self.ownedExchangeSpecificationRealizations.extend(
                ownedExchangeSpecificationRealizations)

        if ownedCategories:
            self.ownedCategories.extend(ownedCategories)

        if ownedFunctionSpecifications:
            self.ownedFunctionSpecifications.extend(ownedFunctionSpecifications)


class DerivedInvolvedfunctionalchaininvolvements(EDerivedCollection):
    pass


class DerivedInvolvedfunctions(EDerivedCollection):
    pass


class DerivedInvolvedfunctionalexchanges(EDerivedCollection):
    pass


class DerivedInvolvedelements(EDerivedCollection):
    pass


class DerivedEnactedfunctions(EDerivedCollection):
    pass


class DerivedEnactedfunctionalblocks(EDerivedCollection):
    pass


class DerivedFirstfunctionalchaininvolvements(EDerivedCollection):
    pass


class DerivedInvolvingcapabilities(EDerivedCollection):
    pass


class DerivedInvolvingcapabilityrealizations(EDerivedCollection):
    pass


class DerivedRealizedfunctionalchains(EDerivedCollection):
    pass


class DerivedRealizingfunctionalchains(EDerivedCollection):
    pass


class FunctionalChain(NamedElement, InvolverElement, InvolvedElement):

    kind = EAttribute(eType=FunctionalChainKind, unique=True, derived=False, changeable=True)
    ownedFunctionalChainInvolvements = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFunctionalChainRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    involvedFunctionalChainInvolvements = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedfunctionalchaininvolvements)
    involvedFunctions = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedfunctions)
    involvedFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedfunctionalexchanges)
    involvedElements = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedInvolvedelements)
    enactedFunctions = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedEnactedfunctions)
    enactedFunctionalBlocks = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedEnactedfunctionalblocks)
    availableInStates = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)
    firstFunctionalChainInvolvements = EReference(ordered=True, unique=True, containment=False,
                                                  derived=True, upper=-1, transient=True, derived_class=DerivedFirstfunctionalchaininvolvements)
    involvingCapabilities = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilities)
    involvingCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilityrealizations)
    realizedFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedRealizedfunctionalchains)
    realizingFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRealizingfunctionalchains)
    preCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    postCondition = EReference(ordered=True, unique=True, containment=False, derived=False)
    ownedSequenceNodes = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedSequenceLinks = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)

    def __init__(self, *, kind=None, ownedFunctionalChainInvolvements=None, ownedFunctionalChainRealizations=None, involvedFunctionalChainInvolvements=None, involvedFunctions=None, involvedFunctionalExchanges=None, involvedElements=None, enactedFunctions=None, enactedFunctionalBlocks=None, availableInStates=None, firstFunctionalChainInvolvements=None, involvingCapabilities=None, involvingCapabilityRealizations=None, realizedFunctionalChains=None, realizingFunctionalChains=None, preCondition=None, postCondition=None, ownedSequenceNodes=None, ownedSequenceLinks=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if ownedFunctionalChainInvolvements:
            self.ownedFunctionalChainInvolvements.extend(ownedFunctionalChainInvolvements)

        if ownedFunctionalChainRealizations:
            self.ownedFunctionalChainRealizations.extend(ownedFunctionalChainRealizations)

        if involvedFunctionalChainInvolvements:
            self.involvedFunctionalChainInvolvements.extend(involvedFunctionalChainInvolvements)

        if involvedFunctions:
            self.involvedFunctions.extend(involvedFunctions)

        if involvedFunctionalExchanges:
            self.involvedFunctionalExchanges.extend(involvedFunctionalExchanges)

        if involvedElements:
            self.involvedElements.extend(involvedElements)

        if enactedFunctions:
            self.enactedFunctions.extend(enactedFunctions)

        if enactedFunctionalBlocks:
            self.enactedFunctionalBlocks.extend(enactedFunctionalBlocks)

        if availableInStates:
            self.availableInStates.extend(availableInStates)

        if firstFunctionalChainInvolvements:
            self.firstFunctionalChainInvolvements.extend(firstFunctionalChainInvolvements)

        if involvingCapabilities:
            self.involvingCapabilities.extend(involvingCapabilities)

        if involvingCapabilityRealizations:
            self.involvingCapabilityRealizations.extend(involvingCapabilityRealizations)

        if realizedFunctionalChains:
            self.realizedFunctionalChains.extend(realizedFunctionalChains)

        if realizingFunctionalChains:
            self.realizingFunctionalChains.extend(realizingFunctionalChains)

        if preCondition is not None:
            self.preCondition = preCondition

        if postCondition is not None:
            self.postCondition = postCondition

        if ownedSequenceNodes:
            self.ownedSequenceNodes.extend(ownedSequenceNodes)

        if ownedSequenceLinks:
            self.ownedSequenceLinks.extend(ownedSequenceLinks)


class FunctionalChainReference(FunctionalChainInvolvement):

    _referencedFunctionalChain = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='referencedFunctionalChain', transient=True)

    @property
    def referencedFunctionalChain(self):
        raise NotImplementedError('Missing implementation for referencedFunctionalChain')

    def __init__(self, *, referencedFunctionalChain=None, **kwargs):

        super().__init__(**kwargs)

        if referencedFunctionalChain is not None:
            self.referencedFunctionalChain = referencedFunctionalChain


@abstract
class AbstractFunctionalArchitecture(ModellingArchitecture):

    ownedFunctionPkg = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedComponentExchanges = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeCategories = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFunctionalLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedFunctionalAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedFunctionPkg=None, ownedComponentExchanges=None, ownedComponentExchangeCategories=None, ownedFunctionalLinks=None, ownedFunctionalAllocations=None, ownedComponentExchangeRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFunctionPkg is not None:
            self.ownedFunctionPkg = ownedFunctionPkg

        if ownedComponentExchanges:
            self.ownedComponentExchanges.extend(ownedComponentExchanges)

        if ownedComponentExchangeCategories:
            self.ownedComponentExchangeCategories.extend(ownedComponentExchangeCategories)

        if ownedFunctionalLinks:
            self.ownedFunctionalLinks.extend(ownedFunctionalLinks)

        if ownedFunctionalAllocations:
            self.ownedFunctionalAllocations.extend(ownedFunctionalAllocations)

        if ownedComponentExchangeRealizations:
            self.ownedComponentExchangeRealizations.extend(ownedComponentExchangeRealizations)


class DerivedExchanges(EDerivedCollection):
    pass


class ExchangeLink(NamedRelationship):

    exchanges = EReference(ordered=True, unique=True, containment=False,
                           derived=True, upper=-1, transient=True, derived_class=DerivedExchanges)
    exchangeContainmentLinks = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownedExchangeContainments = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    sources = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    destinations = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, exchanges=None, exchangeContainmentLinks=None, ownedExchangeContainments=None, sources=None, destinations=None, **kwargs):

        super().__init__(**kwargs)

        if exchanges:
            self.exchanges.extend(exchanges)

        if exchangeContainmentLinks:
            self.exchangeContainmentLinks.extend(exchangeContainmentLinks)

        if ownedExchangeContainments:
            self.ownedExchangeContainments.extend(ownedExchangeContainments)

        if sources:
            self.sources.extend(sources)

        if destinations:
            self.destinations.extend(destinations)


@abstract
class AbstractFunctionAllocation(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class FunctionalChainRealization(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ExchangeSpecificationRealization(Allocation):

    _realizedExchangeSpecification = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedExchangeSpecification', transient=True)
    _realizingExchangeSpecification = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingExchangeSpecification', transient=True)

    @property
    def realizedExchangeSpecification(self):
        raise NotImplementedError('Missing implementation for realizedExchangeSpecification')

    @property
    def realizingExchangeSpecification(self):
        raise NotImplementedError('Missing implementation for realizingExchangeSpecification')

    def __init__(self, *, realizedExchangeSpecification=None, realizingExchangeSpecification=None, **kwargs):

        super().__init__(**kwargs)

        if realizedExchangeSpecification is not None:
            self.realizedExchangeSpecification = realizedExchangeSpecification

        if realizingExchangeSpecification is not None:
            self.realizingExchangeSpecification = realizingExchangeSpecification


class FunctionalExchangeRealization(Allocation):

    _realizedFunctionalExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizedFunctionalExchange', transient=True)
    _realizingFunctionalExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingFunctionalExchange', transient=True)

    @property
    def realizedFunctionalExchange(self):
        raise NotImplementedError('Missing implementation for realizedFunctionalExchange')

    @property
    def realizingFunctionalExchange(self):
        raise NotImplementedError('Missing implementation for realizingFunctionalExchange')

    def __init__(self, *, realizedFunctionalExchange=None, realizingFunctionalExchange=None, **kwargs):

        super().__init__(**kwargs)

        if realizedFunctionalExchange is not None:
            self.realizedFunctionalExchange = realizedFunctionalExchange

        if realizingFunctionalExchange is not None:
            self.realizingFunctionalExchange = realizingFunctionalExchange


class ComponentExchangeAllocation(Allocation):

    _componentExchangeAllocated = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='componentExchangeAllocated', transient=True)
    _componentExchangeAllocator = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='componentExchangeAllocator', transient=True)

    @property
    def componentExchangeAllocated(self):
        raise NotImplementedError('Missing implementation for componentExchangeAllocated')

    @property
    def componentExchangeAllocator(self):
        raise NotImplementedError('Missing implementation for componentExchangeAllocator')

    def __init__(self, *, componentExchangeAllocated=None, componentExchangeAllocator=None, **kwargs):

        super().__init__(**kwargs)

        if componentExchangeAllocated is not None:
            self.componentExchangeAllocated = componentExchangeAllocated

        if componentExchangeAllocator is not None:
            self.componentExchangeAllocator = componentExchangeAllocator


class ComponentPortAllocation(Allocation):

    ownedComponentPortAllocationEnds = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    _allocatedPort = EReference(ordered=True, unique=True, containment=False,
                                derived=True, name='allocatedPort', transient=True)
    _allocatingPort = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, name='allocatingPort', transient=True)

    @property
    def allocatedPort(self):
        raise NotImplementedError('Missing implementation for allocatedPort')

    @property
    def allocatingPort(self):
        raise NotImplementedError('Missing implementation for allocatingPort')

    def __init__(self, *, ownedComponentPortAllocationEnds=None, allocatedPort=None, allocatingPort=None, **kwargs):

        super().__init__(**kwargs)

        if ownedComponentPortAllocationEnds:
            self.ownedComponentPortAllocationEnds.extend(ownedComponentPortAllocationEnds)

        if allocatedPort is not None:
            self.allocatedPort = allocatedPort

        if allocatingPort is not None:
            self.allocatingPort = allocatingPort


class FunctionalChainInvolvementLink(FunctionalChainInvolvement, ReferenceHierarchyContext):

    exchangeContext = EReference(ordered=True, unique=True, containment=False, derived=False)
    exchangedItems = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, exchangeContext=None, exchangedItems=None, source=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if exchangeContext is not None:
            self.exchangeContext = exchangeContext

        if exchangedItems:
            self.exchangedItems.extend(exchangedItems)

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target


class DerivedOutgoingexchangespecificationrealizations(EDerivedCollection):
    pass


class DerivedIncomingexchangespecificationrealizations(EDerivedCollection):
    pass


@abstract
class ExchangeSpecification(NamedElement, ActivityExchange):

    _containingLink = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, name='containingLink', transient=True)
    link = EReference(ordered=True, unique=True, containment=False, derived=False)
    outgoingExchangeSpecificationRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingexchangespecificationrealizations)
    incomingExchangeSpecificationRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedIncomingexchangespecificationrealizations)

    @property
    def containingLink(self):
        raise NotImplementedError('Missing implementation for containingLink')

    def __init__(self, *, containingLink=None, link=None, outgoingExchangeSpecificationRealizations=None, incomingExchangeSpecificationRealizations=None, **kwargs):

        super().__init__(**kwargs)

        if containingLink is not None:
            self.containingLink = containingLink

        if link is not None:
            self.link = link

        if outgoingExchangeSpecificationRealizations:
            self.outgoingExchangeSpecificationRealizations.extend(
                outgoingExchangeSpecificationRealizations)

        if incomingExchangeSpecificationRealizations:
            self.incomingExchangeSpecificationRealizations.extend(
                incomingExchangeSpecificationRealizations)


class ComponentFunctionalAllocation(AbstractFunctionAllocation):

    _function = EReference(ordered=True, unique=True, containment=False,
                           derived=True, name='function', transient=True)
    _block = EReference(ordered=True, unique=True, containment=False,
                        derived=True, name='block', transient=True)

    @property
    def function(self):
        raise NotImplementedError('Missing implementation for function')

    @property
    def block(self):
        raise NotImplementedError('Missing implementation for block')

    def __init__(self, *, function=None, block=None, **kwargs):

        super().__init__(**kwargs)

        if function is not None:
            self.function = function

        if block is not None:
            self.block = block


class FunctionRealization(AbstractFunctionAllocation):

    _allocatedFunction = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedFunction', transient=True)
    _allocatingFunction = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingFunction', transient=True)

    @property
    def allocatedFunction(self):
        raise NotImplementedError('Missing implementation for allocatedFunction')

    @property
    def allocatingFunction(self):
        raise NotImplementedError('Missing implementation for allocatingFunction')

    def __init__(self, *, allocatedFunction=None, allocatingFunction=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedFunction is not None:
            self.allocatedFunction = allocatedFunction

        if allocatingFunction is not None:
            self.allocatingFunction = allocatingFunction


class ComponentExchangeFunctionalExchangeAllocation(AbstractFunctionAllocation):

    _allocatedFunctionalExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedFunctionalExchange', transient=True)
    _allocatingComponentExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingComponentExchange', transient=True)

    @property
    def allocatedFunctionalExchange(self):
        raise NotImplementedError('Missing implementation for allocatedFunctionalExchange')

    @property
    def allocatingComponentExchange(self):
        raise NotImplementedError('Missing implementation for allocatingComponentExchange')

    def __init__(self, *, allocatedFunctionalExchange=None, allocatingComponentExchange=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedFunctionalExchange is not None:
            self.allocatedFunctionalExchange = allocatedFunctionalExchange

        if allocatingComponentExchange is not None:
            self.allocatingComponentExchange = allocatingComponentExchange


class ComponentExchangeRealization(ExchangeSpecificationRealization):

    _allocatedComponentExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedComponentExchange', transient=True)
    _allocatingComponentExchange = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingComponentExchange', transient=True)

    @property
    def allocatedComponentExchange(self):
        raise NotImplementedError('Missing implementation for allocatedComponentExchange')

    @property
    def allocatingComponentExchange(self):
        raise NotImplementedError('Missing implementation for allocatingComponentExchange')

    def __init__(self, *, allocatedComponentExchange=None, allocatingComponentExchange=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedComponentExchange is not None:
            self.allocatedComponentExchange = allocatedComponentExchange

        if allocatingComponentExchange is not None:
            self.allocatingComponentExchange = allocatingComponentExchange


class DerivedOutgoinginvolvementlinks(EDerivedCollection):
    pass


class DerivedIncominginvolvementlinks(EDerivedCollection):
    pass


class FunctionalChainInvolvementFunction(FunctionalChainInvolvement, SequenceLinkEnd):

    outgoingInvolvementLinks = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedOutgoinginvolvementlinks)
    incomingInvolvementLinks = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedIncominginvolvementlinks)

    def __init__(self, *, outgoingInvolvementLinks=None, incomingInvolvementLinks=None, **kwargs):

        super().__init__(**kwargs)

        if outgoingInvolvementLinks:
            self.outgoingInvolvementLinks.extend(outgoingInvolvementLinks)

        if incomingInvolvementLinks:
            self.incomingInvolvementLinks.extend(incomingInvolvementLinks)


class DerivedFunctionalallocations(EDerivedCollection):
    pass


class DerivedAllocatedfunctions(EDerivedCollection):
    pass


@abstract
class AbstractFunctionalBlock(ModellingBlock):

    ownedFunctionalAllocation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchanges = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeCategories = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    functionalAllocations = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedFunctionalallocations)
    allocatedFunctions = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedfunctions)
    inExchangeLinks = EReference(ordered=True, unique=True,
                                 containment=False, derived=False, upper=-1)
    outExchangeLinks = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)

    def __init__(self, *, ownedFunctionalAllocation=None, ownedComponentExchanges=None, ownedComponentExchangeCategories=None, functionalAllocations=None, allocatedFunctions=None, inExchangeLinks=None, outExchangeLinks=None, **kwargs):

        super().__init__(**kwargs)

        if ownedFunctionalAllocation:
            self.ownedFunctionalAllocation.extend(ownedFunctionalAllocation)

        if ownedComponentExchanges:
            self.ownedComponentExchanges.extend(ownedComponentExchanges)

        if ownedComponentExchangeCategories:
            self.ownedComponentExchangeCategories.extend(ownedComponentExchangeCategories)

        if functionalAllocations:
            self.functionalAllocations.extend(functionalAllocations)

        if allocatedFunctions:
            self.allocatedFunctions.extend(allocatedFunctions)

        if inExchangeLinks:
            self.inExchangeLinks.extend(inExchangeLinks)

        if outExchangeLinks:
            self.outExchangeLinks.extend(outExchangeLinks)


class DerivedSubfunctionspecifications(EDerivedCollection):
    pass


class FunctionSpecification(Namespace, AbstractActivity):

    inExchangeLinks = EReference(ordered=True, unique=True,
                                 containment=False, derived=False, upper=-1)
    outExchangeLinks = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    ownedFunctionPorts = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    subFunctionSpecifications = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedSubfunctionspecifications)

    def __init__(self, *, inExchangeLinks=None, outExchangeLinks=None, ownedFunctionPorts=None, subFunctionSpecifications=None, **kwargs):

        super().__init__(**kwargs)

        if inExchangeLinks:
            self.inExchangeLinks.extend(inExchangeLinks)

        if outExchangeLinks:
            self.outExchangeLinks.extend(outExchangeLinks)

        if ownedFunctionPorts:
            self.ownedFunctionPorts.extend(ownedFunctionPorts)

        if subFunctionSpecifications:
            self.subFunctionSpecifications.extend(subFunctionSpecifications)


class DerivedFunctionalexchanges(EDerivedCollection):
    pass


class FunctionalExchangeSpecification(ExchangeSpecification):

    functionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedFunctionalexchanges)

    def __init__(self, *, functionalExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if functionalExchanges:
            self.functionalExchanges.extend(functionalExchanges)


class DerivedAllocatorcomponentports(EDerivedCollection):
    pass


class DerivedRealizedfunctionports(EDerivedCollection):
    pass


class DerivedRealizingfunctionports(EDerivedCollection):
    pass


@abstract
class FunctionPort(Port, TypedElement, AbstractEvent):

    representedComponentPort = EReference(
        ordered=True, unique=True, containment=False, derived=False)
    allocatorComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedAllocatorcomponentports)
    realizedFunctionPorts = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedfunctionports)
    realizingFunctionPorts = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingfunctionports)

    def __init__(self, *, representedComponentPort=None, allocatorComponentPorts=None, realizedFunctionPorts=None, realizingFunctionPorts=None, **kwargs):

        super().__init__(**kwargs)

        if representedComponentPort is not None:
            self.representedComponentPort = representedComponentPort

        if allocatorComponentPorts:
            self.allocatorComponentPorts.extend(allocatorComponentPorts)

        if realizedFunctionPorts:
            self.realizedFunctionPorts.extend(realizedFunctionPorts)

        if realizingFunctionPorts:
            self.realizingFunctionPorts.extend(realizingFunctionPorts)


class DerivedAllocatedfunctionalexchanges(EDerivedCollection):
    pass


class DerivedIncomingcomponentexchangerealizations(EDerivedCollection):
    pass


class DerivedOutgoingcomponentexchangerealizations(EDerivedCollection):
    pass


class DerivedOutgoingcomponentexchangefunctionalexchangeallocations(EDerivedCollection):
    pass


class DerivedCategories(EDerivedCollection):
    pass


class DerivedAllocatorphysicallinks(EDerivedCollection):
    pass


class DerivedRealizedcomponentexchanges(EDerivedCollection):
    pass


class DerivedRealizingcomponentexchanges(EDerivedCollection):
    pass


class ComponentExchange(AbstractEvent, AbstractEventOperation, NamedElement, ExchangeSpecification):

    kind = EAttribute(eType=ComponentExchangeKind, unique=True, derived=False, changeable=True)
    oriented = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=False)
    allocatedFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedfunctionalexchanges)
    incomingComponentExchangeRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedIncomingcomponentexchangerealizations)
    outgoingComponentExchangeRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingcomponentexchangerealizations)
    outgoingComponentExchangeFunctionalExchangeAllocations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingcomponentexchangefunctionalexchangeallocations)
    ownedComponentExchangeFunctionalExchangeAllocations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedComponentExchangeEnds = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    _sourcePort = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='sourcePort', transient=True)
    _sourcePart = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='sourcePart', transient=True)
    _targetPort = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='targetPort', transient=True)
    _targetPart = EReference(ordered=True, unique=True, containment=False,
                             derived=True, name='targetPart', transient=True)
    categories = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedCategories)
    allocatorPhysicalLinks = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedAllocatorphysicallinks)
    realizedComponentExchanges = EReference(ordered=True, unique=True, containment=False,
                                            derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcomponentexchanges)
    realizingComponentExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcomponentexchanges)

    @property
    def sourcePort(self):
        raise NotImplementedError('Missing implementation for sourcePort')

    @property
    def sourcePart(self):
        raise NotImplementedError('Missing implementation for sourcePart')

    @property
    def targetPort(self):
        raise NotImplementedError('Missing implementation for targetPort')

    @property
    def targetPart(self):
        raise NotImplementedError('Missing implementation for targetPart')

    def __init__(self, *, kind=None, oriented=None, allocatedFunctionalExchanges=None, incomingComponentExchangeRealizations=None, outgoingComponentExchangeRealizations=None, outgoingComponentExchangeFunctionalExchangeAllocations=None, ownedComponentExchangeFunctionalExchangeAllocations=None, ownedComponentExchangeRealizations=None, ownedComponentExchangeEnds=None, sourcePort=None, sourcePart=None, targetPort=None, targetPart=None, categories=None, allocatorPhysicalLinks=None, realizedComponentExchanges=None, realizingComponentExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if oriented is not None:
            self.oriented = oriented

        if allocatedFunctionalExchanges:
            self.allocatedFunctionalExchanges.extend(allocatedFunctionalExchanges)

        if incomingComponentExchangeRealizations:
            self.incomingComponentExchangeRealizations.extend(incomingComponentExchangeRealizations)

        if outgoingComponentExchangeRealizations:
            self.outgoingComponentExchangeRealizations.extend(outgoingComponentExchangeRealizations)

        if outgoingComponentExchangeFunctionalExchangeAllocations:
            self.outgoingComponentExchangeFunctionalExchangeAllocations.extend(
                outgoingComponentExchangeFunctionalExchangeAllocations)

        if ownedComponentExchangeFunctionalExchangeAllocations:
            self.ownedComponentExchangeFunctionalExchangeAllocations.extend(
                ownedComponentExchangeFunctionalExchangeAllocations)

        if ownedComponentExchangeRealizations:
            self.ownedComponentExchangeRealizations.extend(ownedComponentExchangeRealizations)

        if ownedComponentExchangeEnds:
            self.ownedComponentExchangeEnds.extend(ownedComponentExchangeEnds)

        if sourcePort is not None:
            self.sourcePort = sourcePort

        if sourcePart is not None:
            self.sourcePart = sourcePart

        if targetPort is not None:
            self.targetPort = targetPort

        if targetPart is not None:
            self.targetPart = targetPart

        if categories:
            self.categories.extend(categories)

        if allocatorPhysicalLinks:
            self.allocatorPhysicalLinks.extend(allocatorPhysicalLinks)

        if realizedComponentExchanges:
            self.realizedComponentExchanges.extend(realizedComponentExchanges)

        if realizingComponentExchanges:
            self.realizingComponentExchanges.extend(realizingComponentExchanges)


class DerivedInvolvingfunctionalchains(EDerivedCollection):
    pass


class DerivedAllocatingcomponentexchanges(EDerivedCollection):
    pass


class DerivedIncomingcomponentexchangefunctionalexchangerealizations(EDerivedCollection):
    pass


class DerivedIncomingfunctionalexchangerealizations(EDerivedCollection):
    pass


class DerivedOutgoingfunctionalexchangerealizations(EDerivedCollection):
    pass


class DerivedCategories(EDerivedCollection):
    pass


class DerivedRealizedfunctionalexchanges(EDerivedCollection):
    pass


class DerivedRealizingfunctionalexchanges(EDerivedCollection):
    pass


class FunctionalExchange(NamedElement, Relationship, InvolvedElement, ObjectFlow, AbstractEvent, AbstractEventOperation):

    exchangeSpecifications = EReference(
        ordered=True, unique=True, containment=False, derived=False, upper=-1)
    involvingFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingfunctionalchains)
    exchangedItems = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    allocatingComponentExchanges = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingcomponentexchanges)
    incomingComponentExchangeFunctionalExchangeRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedIncomingcomponentexchangefunctionalexchangerealizations)
    incomingFunctionalExchangeRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedIncomingfunctionalexchangerealizations)
    outgoingFunctionalExchangeRealizations = EReference(
        ordered=True, unique=True, containment=False, derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingfunctionalexchangerealizations)
    categories = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedCategories)
    ownedFunctionalExchangeRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    _sourceFunctionOutputPort = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='sourceFunctionOutputPort', transient=True)
    _targetFunctionInputPort = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='targetFunctionInputPort', transient=True)
    realizedFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedRealizedfunctionalexchanges)
    realizingFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                              derived=True, upper=-1, transient=True, derived_class=DerivedRealizingfunctionalexchanges)

    @property
    def sourceFunctionOutputPort(self):
        raise NotImplementedError('Missing implementation for sourceFunctionOutputPort')

    @property
    def targetFunctionInputPort(self):
        raise NotImplementedError('Missing implementation for targetFunctionInputPort')

    def __init__(self, *, exchangeSpecifications=None, involvingFunctionalChains=None, exchangedItems=None, allocatingComponentExchanges=None, incomingComponentExchangeFunctionalExchangeRealizations=None, incomingFunctionalExchangeRealizations=None, outgoingFunctionalExchangeRealizations=None, categories=None, ownedFunctionalExchangeRealizations=None, sourceFunctionOutputPort=None, targetFunctionInputPort=None, realizedFunctionalExchanges=None, realizingFunctionalExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if exchangeSpecifications:
            self.exchangeSpecifications.extend(exchangeSpecifications)

        if involvingFunctionalChains:
            self.involvingFunctionalChains.extend(involvingFunctionalChains)

        if exchangedItems:
            self.exchangedItems.extend(exchangedItems)

        if allocatingComponentExchanges:
            self.allocatingComponentExchanges.extend(allocatingComponentExchanges)

        if incomingComponentExchangeFunctionalExchangeRealizations:
            self.incomingComponentExchangeFunctionalExchangeRealizations.extend(
                incomingComponentExchangeFunctionalExchangeRealizations)

        if incomingFunctionalExchangeRealizations:
            self.incomingFunctionalExchangeRealizations.extend(
                incomingFunctionalExchangeRealizations)

        if outgoingFunctionalExchangeRealizations:
            self.outgoingFunctionalExchangeRealizations.extend(
                outgoingFunctionalExchangeRealizations)

        if categories:
            self.categories.extend(categories)

        if ownedFunctionalExchangeRealizations:
            self.ownedFunctionalExchangeRealizations.extend(ownedFunctionalExchangeRealizations)

        if sourceFunctionOutputPort is not None:
            self.sourceFunctionOutputPort = sourceFunctionOutputPort

        if targetFunctionInputPort is not None:
            self.targetFunctionInputPort = targetFunctionInputPort

        if realizedFunctionalExchanges:
            self.realizedFunctionalExchanges.extend(realizedFunctionalExchanges)

        if realizingFunctionalExchanges:
            self.realizingFunctionalExchanges.extend(realizingFunctionalExchanges)


class DerivedComponentexchanges(EDerivedCollection):
    pass


class DerivedAllocatedfunctionports(EDerivedCollection):
    pass


class DerivedDelegatedcomponentports(EDerivedCollection):
    pass


class DerivedDelegatingcomponentports(EDerivedCollection):
    pass


class DerivedAllocatingphysicalports(EDerivedCollection):
    pass


class DerivedRealizedcomponentports(EDerivedCollection):
    pass


class DerivedRealizingcomponentports(EDerivedCollection):
    pass


class ComponentPort(Port, InformationsExchanger, Property):

    orientation = EAttribute(eType=OrientationPortKind, unique=True, derived=False, changeable=True)
    kind = EAttribute(eType=ComponentPortKind, unique=True, derived=False, changeable=True)
    componentExchanges = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedComponentexchanges)
    allocatedFunctionPorts = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedfunctionports)
    delegatedComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedDelegatedcomponentports)
    delegatingComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedDelegatingcomponentports)
    allocatingPhysicalPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingphysicalports)
    realizedComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizedcomponentports)
    realizingComponentPorts = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedRealizingcomponentports)

    def __init__(self, *, orientation=None, kind=None, componentExchanges=None, allocatedFunctionPorts=None, delegatedComponentPorts=None, delegatingComponentPorts=None, allocatingPhysicalPorts=None, realizedComponentPorts=None, realizingComponentPorts=None, **kwargs):

        super().__init__(**kwargs)

        if orientation is not None:
            self.orientation = orientation

        if kind is not None:
            self.kind = kind

        if componentExchanges:
            self.componentExchanges.extend(componentExchanges)

        if allocatedFunctionPorts:
            self.allocatedFunctionPorts.extend(allocatedFunctionPorts)

        if delegatedComponentPorts:
            self.delegatedComponentPorts.extend(delegatedComponentPorts)

        if delegatingComponentPorts:
            self.delegatingComponentPorts.extend(delegatingComponentPorts)

        if allocatingPhysicalPorts:
            self.allocatingPhysicalPorts.extend(allocatingPhysicalPorts)

        if realizedComponentPorts:
            self.realizedComponentPorts.extend(realizedComponentPorts)

        if realizingComponentPorts:
            self.realizingComponentPorts.extend(realizingComponentPorts)


class DerivedIncomingfunctionalexchanges(EDerivedCollection):
    pass


class FunctionInputPort(FunctionPort, InputPin):

    incomingExchangeItems = EReference(ordered=True, unique=True,
                                       containment=False, derived=False, upper=-1)
    incomingFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedIncomingfunctionalexchanges)

    def __init__(self, *, incomingExchangeItems=None, incomingFunctionalExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if incomingExchangeItems:
            self.incomingExchangeItems.extend(incomingExchangeItems)

        if incomingFunctionalExchanges:
            self.incomingFunctionalExchanges.extend(incomingFunctionalExchanges)


class DerivedOutgoingfunctionalexchanges(EDerivedCollection):
    pass


class FunctionOutputPort(FunctionPort, OutputPin):

    outgoingExchangeItems = EReference(ordered=True, unique=True,
                                       containment=False, derived=False, upper=-1)
    outgoingFunctionalExchanges = EReference(ordered=True, unique=True, containment=False,
                                             derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingfunctionalexchanges)

    def __init__(self, *, outgoingExchangeItems=None, outgoingFunctionalExchanges=None, **kwargs):

        super().__init__(**kwargs)

        if outgoingExchangeItems:
            self.outgoingExchangeItems.extend(outgoingExchangeItems)

        if outgoingFunctionalExchanges:
            self.outgoingFunctionalExchanges.extend(outgoingFunctionalExchanges)


class DerivedSubfunctions(EDerivedCollection):
    pass


class DerivedOutfunctionrealizations(EDerivedCollection):
    pass


class DerivedInfunctionrealizations(EDerivedCollection):
    pass


class DerivedComponentfunctionalallocations(EDerivedCollection):
    pass


class DerivedAllocationblocks(EDerivedCollection):
    pass


class DerivedInvolvingcapabilities(EDerivedCollection):
    pass


class DerivedInvolvingcapabilityrealizations(EDerivedCollection):
    pass


class DerivedInvolvingfunctionalchains(EDerivedCollection):
    pass


@abstract
class AbstractFunction(Namespace, InvolvedElement, AbstractInstance, AbstractFunctionalChainContainer, CallBehaviorAction, AbstractEvent):

    kind = EAttribute(eType=FunctionKind, unique=True, derived=False, changeable=True)
    condition = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    ownedFunctions = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    ownedFunctionRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedFunctionalExchanges = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    subFunctions = EReference(ordered=True, unique=True, containment=False,
                              derived=True, upper=-1, transient=True, derived_class=DerivedSubfunctions)
    outFunctionRealizations = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedOutfunctionrealizations)
    inFunctionRealizations = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedInfunctionrealizations)
    componentFunctionalAllocations = EReference(ordered=True, unique=True, containment=False,
                                                derived=True, upper=-1, transient=True, derived_class=DerivedComponentfunctionalallocations)
    allocationBlocks = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedAllocationblocks)
    availableInStates = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)
    involvingCapabilities = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilities)
    involvingCapabilityRealizations = EReference(ordered=True, unique=True, containment=False,
                                                 derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingcapabilityrealizations)
    involvingFunctionalChains = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedInvolvingfunctionalchains)
    _linkedStateMachine = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='linkedStateMachine', transient=True)
    _linkedFunctionSpecification = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='linkedFunctionSpecification', transient=True)

    @property
    def linkedStateMachine(self):
        raise NotImplementedError('Missing implementation for linkedStateMachine')

    @property
    def linkedFunctionSpecification(self):
        raise NotImplementedError('Missing implementation for linkedFunctionSpecification')

    def __init__(self, *, kind=None, condition=None, ownedFunctions=None, ownedFunctionRealizations=None, ownedFunctionalExchanges=None, subFunctions=None, outFunctionRealizations=None, inFunctionRealizations=None, componentFunctionalAllocations=None, allocationBlocks=None, availableInStates=None, involvingCapabilities=None, involvingCapabilityRealizations=None, involvingFunctionalChains=None, linkedStateMachine=None, linkedFunctionSpecification=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if condition is not None:
            self.condition = condition

        if ownedFunctions:
            self.ownedFunctions.extend(ownedFunctions)

        if ownedFunctionRealizations:
            self.ownedFunctionRealizations.extend(ownedFunctionRealizations)

        if ownedFunctionalExchanges:
            self.ownedFunctionalExchanges.extend(ownedFunctionalExchanges)

        if subFunctions:
            self.subFunctions.extend(subFunctions)

        if outFunctionRealizations:
            self.outFunctionRealizations.extend(outFunctionRealizations)

        if inFunctionRealizations:
            self.inFunctionRealizations.extend(inFunctionRealizations)

        if componentFunctionalAllocations:
            self.componentFunctionalAllocations.extend(componentFunctionalAllocations)

        if allocationBlocks:
            self.allocationBlocks.extend(allocationBlocks)

        if availableInStates:
            self.availableInStates.extend(availableInStates)

        if involvingCapabilities:
            self.involvingCapabilities.extend(involvingCapabilities)

        if involvingCapabilityRealizations:
            self.involvingCapabilityRealizations.extend(involvingCapabilityRealizations)

        if involvingFunctionalChains:
            self.involvingFunctionalChains.extend(involvingFunctionalChains)

        if linkedStateMachine is not None:
            self.linkedStateMachine = linkedStateMachine

        if linkedFunctionSpecification is not None:
            self.linkedFunctionSpecification = linkedFunctionSpecification
