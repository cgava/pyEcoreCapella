
from .information import getEClassifier, eClassifiers
from .information import name, nsURI, nsPrefix, eClass
from .information import AbstractInstance, AggregationKind, AssociationPkg, Association, Class, Collection, AbstractCollectionValue, CollectionValue, CollectionValueReference, DataPkg, DomainElement, KeyPart, MultiplicityElement, Operation, OperationAllocation, Parameter, ParameterDirection, PassingMode, Property, SynchronismKind, Service, Union, UnionKind, UnionProperty, Unit, Port, PortRealization, PortAllocation, ExchangeItem, ExchangeItemElement, ExchangeItemInstance, InformationRealization, ExchangeMechanism, ElementKind, CollectionKind, ExchangeItemRealization, AbstractEventOperation

from information.communication import Signal, Message, Exception, MessageReference
from capellacore import GeneralizableElement, EnumerationPropertyLiteral, GeneralClass, Generalization, AbstractPropertyValue, Type, TypedElement, EnumerationPropertyType, NamingRule, Type, Feature, PropertyValuePkg, PropertyValueGroup, Trace
from cs import Interface
from capellacommon import GenericTrace, StateEvent, StateMachine
from modellingcore import AbstractConstraint, AbstractExchangeItem, AbstractTrace, ModelElement, AbstractTypedElement, AbstractInformationFlow, AbstractType, ValueSpecification, AbstractParameterSet, TraceableElement
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from information.datatype import DataType
from information.datavalue import NumericValue, DataValue
from interaction import InstanceRole, SequenceMessage

from .communication import Signal, CommunicationLink, MessageReference, Message, CommunicationLinkExchanger, Exception, SignalInstance, MessageReferencePkg, CommunicationItem
from .datatype import DataType, StringType, BooleanType, PhysicalQuantity, Enumeration, NumericType
from .datavalue import NumericReference, ComplexValue, AbstractExpressionValue, BinaryExpression, ComplexValueReference, BooleanReference, EnumerationLiteral, UnaryExpression, ValuePart, NumericValue, AbstractBooleanValue, EnumerationReference, AbstractComplexValue, AbstractStringValue, StringReference, DataValue, LiteralBooleanValue, AbstractEnumerationValue, DataValueContainer
from . import information
from . import communication

from . import datatype

from . import datavalue


__all__ = ['AbstractInstance', 'AggregationKind', 'AssociationPkg', 'Association', 'Class', 'Collection', 'AbstractCollectionValue', 'CollectionValue', 'CollectionValueReference', 'DataPkg', 'DomainElement', 'KeyPart', 'MultiplicityElement', 'Operation', 'OperationAllocation', 'Parameter', 'ParameterDirection', 'PassingMode',
           'Property', 'SynchronismKind', 'Service', 'Union', 'UnionKind', 'UnionProperty', 'Unit', 'Port', 'PortRealization', 'PortAllocation', 'ExchangeItem', 'ExchangeItemElement', 'ExchangeItemInstance', 'InformationRealization', 'ExchangeMechanism', 'ElementKind', 'CollectionKind', 'ExchangeItemRealization', 'AbstractEventOperation']

eSubpackages = [communication, datatype, datavalue]
eSuperPackage = None
information.eSubpackages = eSubpackages
information.eSuperPackage = eSuperPackage

CommunicationItem.ownedStateMachines.eType = StateMachine
CommunicationItem.properties.eType = Property
MessageReference.message.eType = Message
MessageReferencePkg.ownedMessageReferences.eType = MessageReference
Signal.signalInstances.eType = SignalInstance
CommunicationLink.exchangeItem.eType = ExchangeItem
CommunicationLinkExchanger.ownedCommunicationLinks.eType = CommunicationLink
CommunicationLinkExchanger.produce.eType = CommunicationLink
CommunicationLinkExchanger.consume.eType = CommunicationLink
CommunicationLinkExchanger.send.eType = CommunicationLink
CommunicationLinkExchanger.receive.eType = CommunicationLink
CommunicationLinkExchanger.call.eType = CommunicationLink
CommunicationLinkExchanger.execute.eType = CommunicationLink
CommunicationLinkExchanger.write.eType = CommunicationLink
CommunicationLinkExchanger.access.eType = CommunicationLink
CommunicationLinkExchanger.acquire.eType = CommunicationLink
CommunicationLinkExchanger.transmit.eType = CommunicationLink
DataType._defaultValue.eType = DataValue
DataType._nullValue.eType = DataValue
DataType.ownedInformationRealizations.eType = InformationRealization
BooleanType.ownedLiterals.eType = LiteralBooleanValue
BooleanType.ownedDefaultValue.eType = AbstractBooleanValue
Enumeration.ownedLiterals.eType = EnumerationLiteral
Enumeration.ownedDefaultValue.eType = AbstractEnumerationValue
Enumeration.ownedNullValue.eType = AbstractEnumerationValue
Enumeration.ownedMinValue.eType = AbstractEnumerationValue
Enumeration.ownedMaxValue.eType = AbstractEnumerationValue
Enumeration.domainType.eType = DataType
StringType.ownedDefaultValue.eType = AbstractStringValue
StringType.ownedNullValue.eType = AbstractStringValue
StringType.ownedMinLength.eType = NumericValue
StringType.ownedMaxLength.eType = NumericValue
NumericType.ownedDefaultValue.eType = NumericValue
NumericType.ownedNullValue.eType = NumericValue
NumericType.ownedMinValue.eType = NumericValue
NumericType.ownedMaxValue.eType = NumericValue
PhysicalQuantity.unit.eType = Unit
DataValue._type.eType = Type
DataValueContainer.ownedDataValues.eType = DataValue
AbstractBooleanValue._booleanType.eType = BooleanType
BooleanReference.referencedValue.eType = AbstractBooleanValue
BooleanReference.referencedProperty.eType = Property
AbstractEnumerationValue._enumerationType.eType = Enumeration
EnumerationLiteral.domainValue.eType = DataValue
EnumerationReference.referencedValue.eType = AbstractEnumerationValue
EnumerationReference.referencedProperty.eType = Property
AbstractStringValue._stringType.eType = StringType
StringReference.referencedValue.eType = AbstractStringValue
StringReference.referencedProperty.eType = Property
NumericValue.unit.eType = Unit
NumericValue._numericType.eType = NumericType
NumericReference.referencedValue.eType = NumericValue
NumericReference.referencedProperty.eType = Property
AbstractComplexValue._complexType.eType = Classifier
ComplexValue.ownedParts.eType = ValuePart
ComplexValueReference.referencedValue.eType = AbstractComplexValue
ComplexValueReference.referencedProperty.eType = Property
ValuePart.referencedProperty.eType = Property
ValuePart.ownedValue.eType = DataValue
AbstractExpressionValue._expressionType.eType = DataType
BinaryExpression.ownedLeftOperand.eType = DataValue
BinaryExpression.ownedRightOperand.eType = DataValue
UnaryExpression.ownedOperand.eType = DataValue
AbstractInstance.representingInstanceRoles.eType = InstanceRole
AssociationPkg.ownedAssociations.eType = Association
Association.ownedMembers.eType = Property
Association.navigableMembers.eType = Property
Class.keyParts.eType = KeyPart
Class.ownedStateMachines.eType = StateMachine
Class.ownedDataValues.eType = DataValue
Class.ownedInformationRealizations.eType = InformationRealization
Collection.type.eType = Type
Collection.index.eType = DataType
Collection.containedOperations.eType = Operation
CollectionValue.ownedElements.eType = DataValue
CollectionValue.ownedDefaultElement.eType = DataValue
CollectionValueReference.referencedValue.eType = AbstractCollectionValue
CollectionValueReference.referencedProperty.eType = Property
DataPkg.ownedDataPkgs.eType = DataPkg
DataPkg.ownedClasses.eType = Class
DataPkg.ownedKeyParts.eType = KeyPart
DataPkg.ownedCollections.eType = Collection
DataPkg.ownedUnits.eType = Unit
DataPkg.ownedDataTypes.eType = DataType
DataPkg.ownedSignals.eType = Signal
DataPkg.ownedMessages.eType = Message
DataPkg.ownedExceptions.eType = Exception
DataPkg.ownedStateEvents.eType = StateEvent
KeyPart.property.eType = Property
MultiplicityElement.ownedDefaultValue.eType = DataValue
MultiplicityElement.ownedMinValue.eType = DataValue
MultiplicityElement.ownedMaxValue.eType = DataValue
MultiplicityElement.ownedNullValue.eType = DataValue
MultiplicityElement.ownedMinCard.eType = NumericValue
MultiplicityElement.ownedMinLength.eType = NumericValue
MultiplicityElement.ownedMaxCard.eType = NumericValue
MultiplicityElement.ownedMaxLength.eType = NumericValue
Operation.ownedParameters.eType = Parameter
Operation.ownedOperationAllocation.eType = OperationAllocation
Operation.ownedExchangeItemRealizations.eType = ExchangeItemRealization
OperationAllocation._allocatedOperation.eType = Operation
OperationAllocation._allocatingOperation.eType = Operation
Property._association.eType = Association
Service.thrownExceptions.eType = Exception
Service.messages.eType = Message
Service.messageReferences.eType = MessageReference
Union.discriminant.eType = UnionProperty
Union.defaultProperty.eType = UnionProperty
Union.containedUnionProperties.eType = UnionProperty
UnionProperty.qualifier.eType = DataValue
Port.ownedProtocols.eType = StateMachine
Port.providedInterfaces.eType = Interface
Port.requiredInterfaces.eType = Interface
Port.ownedPortRealizations.eType = PortRealization
Port.ownedPortAllocations.eType = PortAllocation
ExchangeItem.ownedElements.eType = ExchangeItemElement
ExchangeItem.ownedInformationRealizations.eType = InformationRealization
ExchangeItem.ownedExchangeItemInstances.eType = ExchangeItemInstance
ExchangeItem.allocatorInterfaces.eType = Interface
ExchangeItemElement.referencedProperties.eType = Property
ExchangeItemRealization._realizedItem.eType = AbstractExchangeItem
ExchangeItemRealization._realizingOperation.eType = Operation
AbstractEventOperation.invokingSequenceMessages.eType = SequenceMessage
DataType.realizedDataTypes.eType = DataType
DataType.realizingDataTypes.eType = DataType
DataType.realizingDataTypes.eOpposite = DataType.realizedDataTypes
Class.realizedClasses.eType = Class
Class.realizingClasses.eType = Class
Class.realizingClasses.eOpposite = Class.realizedClasses
Operation.allocatingOperations.eType = Operation
Operation.allocatedOperations.eType = Operation
Operation.allocatedOperations.eOpposite = Operation.allocatingOperations
Operation.realizedExchangeItems.eType = ExchangeItem
Port.incomingPortRealizations.eType = PortRealization
Port.outgoingPortRealizations.eType = PortRealization
Port.incomingPortAllocations.eType = PortAllocation
Port.outgoingPortAllocations.eType = PortAllocation
PortRealization._realizedPort.eType = Port
PortRealization._realizedPort.eOpposite = Port.incomingPortRealizations
PortRealization._realizingPort.eType = Port
PortRealization._realizingPort.eOpposite = Port.outgoingPortRealizations
PortAllocation._allocatedPort.eType = Port
PortAllocation._allocatedPort.eOpposite = Port.incomingPortAllocations
PortAllocation._allocatingPort.eType = Port
PortAllocation._allocatingPort.eOpposite = Port.outgoingPortAllocations
ExchangeItem.realizedExchangeItems.eType = ExchangeItem
ExchangeItem.realizingExchangeItems.eType = ExchangeItem
ExchangeItem.realizingExchangeItems.eOpposite = ExchangeItem.realizedExchangeItems
ExchangeItem.realizingOperations.eType = Operation
ExchangeItem.realizingOperations.eOpposite = Operation.realizedExchangeItems

otherClassifiers = [AggregationKind, ParameterDirection, PassingMode,
                    SynchronismKind, UnionKind, ExchangeMechanism, ElementKind, CollectionKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
