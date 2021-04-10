"""Definition of meta model 'information'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pycapella2.behavior import AbstractEvent, AbstractSignal
from pycapella2.capellacore import AbstractDependenciesPkg, AbstractExchangeItemPkg, Allocation, CapellaElement, Classifier, Feature, GeneralClass, GeneralizableElement, NamedElement, NamedRelationship, Relationship, Structure, TypedElement, VisibilityKind
from pycapella2.information.datavalue import DataValue, DataValueContainer
from pycapella2.modellingcore import AbstractExchangeItem, AbstractParameter, FinalizableElement


name = 'information'
nsURI = 'http://www.polarsys.org/capella/core/information/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.information'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
AggregationKind = EEnum('AggregationKind', literals=[
                        'UNSET', 'ASSOCIATION', 'AGGREGATION', 'COMPOSITION'])

ParameterDirection = EEnum('ParameterDirection', literals=[
                           'IN', 'OUT', 'INOUT', 'RETURN', 'EXCEPTION', 'UNSET'])

PassingMode = EEnum('PassingMode', literals=['UNSET', 'BY_REF', 'BY_VALUE'])

SynchronismKind = EEnum('SynchronismKind', literals=['UNSET', 'SYNCHRONOUS', 'ASYNCHRONOUS'])

UnionKind = EEnum('UnionKind', literals=['UNION', 'VARIANT'])

ExchangeMechanism = EEnum('ExchangeMechanism', literals=[
                          'UNSET', 'FLOW', 'OPERATION', 'EVENT', 'SHARED_DATA'])

ElementKind = EEnum('ElementKind', literals=['TYPE', 'MEMBER'])

CollectionKind = EEnum('CollectionKind', literals=['ARRAY', 'SEQUENCE'])


@abstract
class MultiplicityElement(CapellaElement):

    ordered = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    unique = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    minInclusive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    maxInclusive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedNullValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinCard = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinLength = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxCard = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxLength = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ordered=None, unique=None, minInclusive=None, maxInclusive=None, ownedDefaultValue=None, ownedMinValue=None, ownedMaxValue=None, ownedNullValue=None, ownedMinCard=None, ownedMinLength=None, ownedMaxCard=None, ownedMaxLength=None, **kwargs):

        super().__init__(**kwargs)

        if ordered is not None:
            self.ordered = ordered

        if unique is not None:
            self.unique = unique

        if minInclusive is not None:
            self.minInclusive = minInclusive

        if maxInclusive is not None:
            self.maxInclusive = maxInclusive

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue

        if ownedMinValue is not None:
            self.ownedMinValue = ownedMinValue

        if ownedMaxValue is not None:
            self.ownedMaxValue = ownedMaxValue

        if ownedNullValue is not None:
            self.ownedNullValue = ownedNullValue

        if ownedMinCard is not None:
            self.ownedMinCard = ownedMinCard

        if ownedMinLength is not None:
            self.ownedMinLength = ownedMinLength

        if ownedMaxCard is not None:
            self.ownedMaxCard = ownedMaxCard

        if ownedMaxLength is not None:
            self.ownedMaxLength = ownedMaxLength


class KeyPart(Relationship):

    property = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, property=None, **kwargs):

        super().__init__(**kwargs)

        if property is not None:
            self.property = property


class Unit(NamedElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedIncomingportrealizations(EDerivedCollection):
    pass


class DerivedOutgoingportrealizations(EDerivedCollection):
    pass


class DerivedIncomingportallocations(EDerivedCollection):
    pass


class DerivedOutgoingportallocations(EDerivedCollection):
    pass


@abstract
class Port(NamedElement):

    incomingPortRealizations = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedIncomingportrealizations)
    outgoingPortRealizations = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingportrealizations)
    ownedProtocols = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    incomingPortAllocations = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedIncomingportallocations)
    outgoingPortAllocations = EReference(ordered=True, unique=True, containment=False,
                                         derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingportallocations)
    providedInterfaces = EReference(ordered=True, unique=True,
                                    containment=False, derived=False, upper=-1)
    requiredInterfaces = EReference(ordered=True, unique=True,
                                    containment=False, derived=False, upper=-1)
    ownedPortRealizations = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)
    ownedPortAllocations = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)

    def __init__(self, *, incomingPortRealizations=None, outgoingPortRealizations=None, ownedProtocols=None, incomingPortAllocations=None, outgoingPortAllocations=None, providedInterfaces=None, requiredInterfaces=None, ownedPortRealizations=None, ownedPortAllocations=None, **kwargs):

        super().__init__(**kwargs)

        if incomingPortRealizations:
            self.incomingPortRealizations.extend(incomingPortRealizations)

        if outgoingPortRealizations:
            self.outgoingPortRealizations.extend(outgoingPortRealizations)

        if ownedProtocols:
            self.ownedProtocols.extend(ownedProtocols)

        if incomingPortAllocations:
            self.incomingPortAllocations.extend(incomingPortAllocations)

        if outgoingPortAllocations:
            self.outgoingPortAllocations.extend(outgoingPortAllocations)

        if providedInterfaces:
            self.providedInterfaces.extend(providedInterfaces)

        if requiredInterfaces:
            self.requiredInterfaces.extend(requiredInterfaces)

        if ownedPortRealizations:
            self.ownedPortRealizations.extend(ownedPortRealizations)

        if ownedPortAllocations:
            self.ownedPortAllocations.extend(ownedPortAllocations)


class DerivedInvokingsequencemessages(EDerivedCollection):
    pass


@abstract
class AbstractEventOperation(NamedElement):

    invokingSequenceMessages = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedInvokingsequencemessages)

    def __init__(self, *, invokingSequenceMessages=None, **kwargs):

        super().__init__(**kwargs)

        if invokingSequenceMessages:
            self.invokingSequenceMessages.extend(invokingSequenceMessages)


@abstract
class AssociationPkg(Structure):

    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)
    ownedAssociations = EReference(ordered=True, unique=True,
                                   containment=True, derived=False, upper=-1)

    def __init__(self, *, visibility=None, ownedAssociations=None, **kwargs):

        super().__init__(**kwargs)

        if visibility is not None:
            self.visibility = visibility

        if ownedAssociations:
            self.ownedAssociations.extend(ownedAssociations)


class Association(NamedRelationship):

    ownedMembers = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    navigableMembers = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)

    def __init__(self, *, ownedMembers=None, navigableMembers=None, **kwargs):

        super().__init__(**kwargs)

        if ownedMembers:
            self.ownedMembers.extend(ownedMembers)

        if navigableMembers:
            self.navigableMembers.extend(navigableMembers)


class OperationAllocation(Allocation):

    _allocatedOperation = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatedOperation', transient=True)
    _allocatingOperation = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='allocatingOperation', transient=True)

    @property
    def allocatedOperation(self):
        raise NotImplementedError('Missing implementation for allocatedOperation')

    @property
    def allocatingOperation(self):
        raise NotImplementedError('Missing implementation for allocatingOperation')

    def __init__(self, *, allocatedOperation=None, allocatingOperation=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedOperation is not None:
            self.allocatedOperation = allocatedOperation

        if allocatingOperation is not None:
            self.allocatingOperation = allocatingOperation


class PortRealization(Allocation):

    _realizedPort = EReference(ordered=True, unique=True, containment=False,
                               derived=True, name='realizedPort', transient=True)
    _realizingPort = EReference(ordered=True, unique=True, containment=False,
                                derived=True, name='realizingPort', transient=True)

    @property
    def realizedPort(self):
        raise NotImplementedError('Missing implementation for realizedPort')

    @property
    def realizingPort(self):
        raise NotImplementedError('Missing implementation for realizingPort')

    def __init__(self, *, realizedPort=None, realizingPort=None, **kwargs):

        super().__init__(**kwargs)

        if realizedPort is not None:
            self.realizedPort = realizedPort

        if realizingPort is not None:
            self.realizingPort = realizingPort


class PortAllocation(Allocation):

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

    def __init__(self, *, allocatedPort=None, allocatingPort=None, **kwargs):

        super().__init__(**kwargs)

        if allocatedPort is not None:
            self.allocatedPort = allocatedPort

        if allocatingPort is not None:
            self.allocatingPort = allocatingPort


class InformationRealization(Allocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ExchangeItemRealization(Allocation):

    _realizedItem = EReference(ordered=True, unique=True, containment=False,
                               derived=True, name='realizedItem', transient=True)
    _realizingOperation = EReference(
        ordered=True, unique=True, containment=False, derived=True, name='realizingOperation', transient=True)

    @property
    def realizedItem(self):
        raise NotImplementedError('Missing implementation for realizedItem')

    @property
    def realizingOperation(self):
        raise NotImplementedError('Missing implementation for realizingOperation')

    def __init__(self, *, realizedItem=None, realizingOperation=None, **kwargs):

        super().__init__(**kwargs)

        if realizedItem is not None:
            self.realizedItem = realizedItem

        if realizingOperation is not None:
            self.realizingOperation = realizingOperation


@abstract
class AbstractCollectionValue(DataValue):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class CollectionValue(AbstractCollectionValue):

    ownedElements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedDefaultElement = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedElements=None, ownedDefaultElement=None, **kwargs):

        super().__init__(**kwargs)

        if ownedElements:
            self.ownedElements.extend(ownedElements)

        if ownedDefaultElement is not None:
            self.ownedDefaultElement = ownedDefaultElement


class CollectionValueReference(AbstractCollectionValue):

    referencedValue = EReference(ordered=True, unique=True, containment=False, derived=False)
    referencedProperty = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, referencedValue=None, referencedProperty=None, **kwargs):

        super().__init__(**kwargs)

        if referencedValue is not None:
            self.referencedValue = referencedValue

        if referencedProperty is not None:
            self.referencedProperty = referencedProperty


class DerivedAllocatingoperations(EDerivedCollection):
    pass


class DerivedAllocatedoperations(EDerivedCollection):
    pass


class DerivedRealizedexchangeitems(EDerivedCollection):
    pass


@abstract
class Operation(Feature, AbstractEvent, AbstractEventOperation):

    ownedParameters = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    allocatingOperations = EReference(ordered=True, unique=True, containment=False,
                                      derived=True, upper=-1, transient=True, derived_class=DerivedAllocatingoperations)
    allocatedOperations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedAllocatedoperations)
    ownedOperationAllocation = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedExchangeItemRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedExchangeItems = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedexchangeitems)

    def __init__(self, *, ownedParameters=None, allocatingOperations=None, allocatedOperations=None, ownedOperationAllocation=None, ownedExchangeItemRealizations=None, realizedExchangeItems=None, **kwargs):

        super().__init__(**kwargs)

        if ownedParameters:
            self.ownedParameters.extend(ownedParameters)

        if allocatingOperations:
            self.allocatingOperations.extend(allocatingOperations)

        if allocatedOperations:
            self.allocatedOperations.extend(allocatedOperations)

        if ownedOperationAllocation:
            self.ownedOperationAllocation.extend(ownedOperationAllocation)

        if ownedExchangeItemRealizations:
            self.ownedExchangeItemRealizations.extend(ownedExchangeItemRealizations)

        if realizedExchangeItems:
            self.realizedExchangeItems.extend(realizedExchangeItems)


class ExchangeItemElement(NamedElement, MultiplicityElement, TypedElement):

    kind = EAttribute(eType=ElementKind, unique=True, derived=False, changeable=True)
    direction = EAttribute(eType=ParameterDirection, unique=True, derived=False, changeable=True)
    composite = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    referencedProperties = EReference(ordered=True, unique=True,
                                      containment=False, derived=False, upper=-1)

    def __init__(self, *, kind=None, direction=None, composite=None, referencedProperties=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if direction is not None:
            self.direction = direction

        if composite is not None:
            self.composite = composite

        if referencedProperties:
            self.referencedProperties.extend(referencedProperties)


class Parameter(TypedElement, MultiplicityElement, AbstractParameter):

    direction = EAttribute(eType=ParameterDirection, unique=True, derived=False, changeable=True)
    passingMode = EAttribute(eType=PassingMode, unique=True, derived=False, changeable=True)

    def __init__(self, *, direction=None, passingMode=None, **kwargs):

        super().__init__(**kwargs)

        if direction is not None:
            self.direction = direction

        if passingMode is not None:
            self.passingMode = passingMode


class Property(Feature, TypedElement, MultiplicityElement, FinalizableElement):

    aggregationKind = EAttribute(eType=AggregationKind, unique=True,
                                 derived=False, changeable=True, default_value=AggregationKind.UNSET)
    isDerived = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isReadOnly = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isPartOfKey = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    _association = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='association', transient=True)

    @property
    def association(self):
        raise NotImplementedError('Missing implementation for association')

    def __init__(self, *, aggregationKind=None, isDerived=None, isReadOnly=None, isPartOfKey=None, association=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationKind is not None:
            self.aggregationKind = aggregationKind

        if isDerived is not None:
            self.isDerived = isDerived

        if isReadOnly is not None:
            self.isReadOnly = isReadOnly

        if isPartOfKey is not None:
            self.isPartOfKey = isPartOfKey

        if association is not None:
            self.association = association


class DerivedMessages(EDerivedCollection):
    pass


class Service(Operation):

    synchronismKind = EAttribute(eType=SynchronismKind, unique=True, derived=False, changeable=True)
    thrownExceptions = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    messages = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedMessages)
    messageReferences = EReference(ordered=True, unique=True,
                                   containment=False, derived=False, upper=-1)

    def __init__(self, *, synchronismKind=None, thrownExceptions=None, messages=None, messageReferences=None, **kwargs):

        super().__init__(**kwargs)

        if synchronismKind is not None:
            self.synchronismKind = synchronismKind

        if thrownExceptions:
            self.thrownExceptions.extend(thrownExceptions)

        if messages:
            self.messages.extend(messages)

        if messageReferences:
            self.messageReferences.extend(messageReferences)


class DerivedRepresentinginstanceroles(EDerivedCollection):
    pass


@abstract
class AbstractInstance(Property):

    representingInstanceRoles = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRepresentinginstanceroles)

    def __init__(self, *, representingInstanceRoles=None, **kwargs):

        super().__init__(**kwargs)

        if representingInstanceRoles:
            self.representingInstanceRoles.extend(representingInstanceRoles)


class DerivedRealizedclasses(EDerivedCollection):
    pass


class DerivedRealizingclasses(EDerivedCollection):
    pass


class Class(GeneralClass):

    isPrimitive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    keyParts = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    ownedStateMachines = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    ownedDataValues = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedInformationRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedClasses = EReference(ordered=True, unique=True, containment=False,
                                 derived=True, upper=-1, transient=True, derived_class=DerivedRealizedclasses)
    realizingClasses = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedRealizingclasses)

    def __init__(self, *, isPrimitive=None, keyParts=None, ownedStateMachines=None, ownedDataValues=None, ownedInformationRealizations=None, realizedClasses=None, realizingClasses=None, **kwargs):

        super().__init__(**kwargs)

        if isPrimitive is not None:
            self.isPrimitive = isPrimitive

        if keyParts:
            self.keyParts.extend(keyParts)

        if ownedStateMachines:
            self.ownedStateMachines.extend(ownedStateMachines)

        if ownedDataValues:
            self.ownedDataValues.extend(ownedDataValues)

        if ownedInformationRealizations:
            self.ownedInformationRealizations.extend(ownedInformationRealizations)

        if realizedClasses:
            self.realizedClasses.extend(realizedClasses)

        if realizingClasses:
            self.realizingClasses.extend(realizingClasses)


# Inheritance definition for DataPkg moved in root package initialization
# to fix circular imports with MessageReferencePkg


class DataPkg(EObject, metaclass=MetaEClass):

    ownedDataPkgs = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedClasses = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedKeyParts = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedCollections = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedUnits = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedDataTypes = EReference(ordered=True, unique=True,
                                containment=True, derived=False, upper=-1)
    ownedSignals = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedMessages = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedExceptions = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    ownedStateEvents = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedDataPkgs=None, ownedClasses=None, ownedKeyParts=None, ownedCollections=None, ownedUnits=None, ownedDataTypes=None, ownedSignals=None, ownedMessages=None, ownedExceptions=None, ownedStateEvents=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDataPkgs:
            self.ownedDataPkgs.extend(ownedDataPkgs)

        if ownedClasses:
            self.ownedClasses.extend(ownedClasses)

        if ownedKeyParts:
            self.ownedKeyParts.extend(ownedKeyParts)

        if ownedCollections:
            self.ownedCollections.extend(ownedCollections)

        if ownedUnits:
            self.ownedUnits.extend(ownedUnits)

        if ownedDataTypes:
            self.ownedDataTypes.extend(ownedDataTypes)

        if ownedSignals:
            self.ownedSignals.extend(ownedSignals)

        if ownedMessages:
            self.ownedMessages.extend(ownedMessages)

        if ownedExceptions:
            self.ownedExceptions.extend(ownedExceptions)

        if ownedStateEvents:
            self.ownedStateEvents.extend(ownedStateEvents)


class UnionProperty(Property):

    qualifier = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, qualifier=None, **kwargs):

        super().__init__(**kwargs)

        if qualifier:
            self.qualifier.extend(qualifier)


class DomainElement(Class):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedContainedunionproperties(EDerivedCollection):
    pass


class Union(Class):

    kind = EAttribute(eType=UnionKind, unique=True, derived=False, changeable=True)
    discriminant = EReference(ordered=True, unique=True, containment=False, derived=False)
    defaultProperty = EReference(ordered=True, unique=True, containment=False, derived=False)
    containedUnionProperties = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedContainedunionproperties)

    def __init__(self, *, kind=None, discriminant=None, defaultProperty=None, containedUnionProperties=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if discriminant is not None:
            self.discriminant = discriminant

        if defaultProperty is not None:
            self.defaultProperty = defaultProperty

        if containedUnionProperties:
            self.containedUnionProperties.extend(containedUnionProperties)


class ExchangeItemInstance(AbstractInstance):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedContainedoperations(EDerivedCollection):
    pass


class Collection(Classifier, MultiplicityElement, DataValueContainer, FinalizableElement):

    isPrimitive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)
    kind = EAttribute(eType=CollectionKind, unique=True, derived=False, changeable=True)
    aggregationKind = EAttribute(eType=AggregationKind, unique=True, derived=False, changeable=True)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)
    index = EReference(ordered=True, unique=False, containment=False, derived=False, upper=-1)
    containedOperations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedContainedoperations)

    def __init__(self, *, isPrimitive=None, visibility=None, kind=None, aggregationKind=None, type=None, index=None, containedOperations=None, **kwargs):

        super().__init__(**kwargs)

        if isPrimitive is not None:
            self.isPrimitive = isPrimitive

        if visibility is not None:
            self.visibility = visibility

        if kind is not None:
            self.kind = kind

        if aggregationKind is not None:
            self.aggregationKind = aggregationKind

        if type is not None:
            self.type = type

        if index:
            self.index.extend(index)

        if containedOperations:
            self.containedOperations.extend(containedOperations)


class DerivedAllocatorinterfaces(EDerivedCollection):
    pass


class DerivedRealizedexchangeitems(EDerivedCollection):
    pass


class DerivedRealizingexchangeitems(EDerivedCollection):
    pass


class DerivedRealizingoperations(EDerivedCollection):
    pass


class ExchangeItem(AbstractExchangeItem, AbstractEvent, AbstractSignal, FinalizableElement, GeneralizableElement):

    exchangeMechanism = EAttribute(eType=ExchangeMechanism, unique=True,
                                   derived=False, changeable=True)
    ownedElements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedInformationRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedExchangeItemInstances = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    allocatorInterfaces = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedAllocatorinterfaces)
    realizedExchangeItems = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedRealizedexchangeitems)
    realizingExchangeItems = EReference(ordered=True, unique=True, containment=False,
                                        derived=True, upper=-1, transient=True, derived_class=DerivedRealizingexchangeitems)
    realizingOperations = EReference(ordered=True, unique=True, containment=False,
                                     derived=True, upper=-1, transient=True, derived_class=DerivedRealizingoperations)

    def __init__(self, *, exchangeMechanism=None, ownedElements=None, ownedInformationRealizations=None, ownedExchangeItemInstances=None, allocatorInterfaces=None, realizedExchangeItems=None, realizingExchangeItems=None, realizingOperations=None, **kwargs):

        super().__init__(**kwargs)

        if exchangeMechanism is not None:
            self.exchangeMechanism = exchangeMechanism

        if ownedElements:
            self.ownedElements.extend(ownedElements)

        if ownedInformationRealizations:
            self.ownedInformationRealizations.extend(ownedInformationRealizations)

        if ownedExchangeItemInstances:
            self.ownedExchangeItemInstances.extend(ownedExchangeItemInstances)

        if allocatorInterfaces:
            self.allocatorInterfaces.extend(allocatorInterfaces)

        if realizedExchangeItems:
            self.realizedExchangeItems.extend(realizedExchangeItems)

        if realizingExchangeItems:
            self.realizingExchangeItems.extend(realizingExchangeItems)

        if realizingOperations:
            self.realizingOperations.extend(realizingOperations)
