
#print('information.cross_init starting')


information.communication.CommunicationItem.ownedStateMachines.eType = capellacommon.StateMachine
information.communication.CommunicationItem.properties.eType = information.Property
information.communication.MessageReference.message.eType = information.communication.Message
information.communication.MessageReferencePkg.ownedMessageReferences.eType = information.communication.MessageReference
information.communication.Signal.signalInstances.eType = information.communication.SignalInstance
information.communication.CommunicationLink.exchangeItem.eType = information.ExchangeItem
information.communication.CommunicationLinkExchanger.ownedCommunicationLinks.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.produce.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.consume.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.send.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.receive.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.call.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.execute.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.write.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.access.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.acquire.eType = information.communication.CommunicationLink
information.communication.CommunicationLinkExchanger.transmit.eType = information.communication.CommunicationLink
information.datatype.DataType._defaultValue.eType = information.datavalue.DataValue
information.datatype.DataType._nullValue.eType = information.datavalue.DataValue
information.datatype.DataType.ownedInformationRealizations.eType = information.InformationRealization
information.datatype.BooleanType.ownedLiterals.eType = information.datavalue.LiteralBooleanValue
information.datatype.BooleanType.ownedDefaultValue.eType = information.datavalue.AbstractBooleanValue
information.datatype.Enumeration.ownedLiterals.eType = information.datavalue.EnumerationLiteral
information.datatype.Enumeration.ownedDefaultValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedNullValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedMinValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.ownedMaxValue.eType = information.datavalue.AbstractEnumerationValue
information.datatype.Enumeration.domainType.eType = information.datatype.DataType
information.datatype.StringType.ownedDefaultValue.eType = information.datavalue.AbstractStringValue
information.datatype.StringType.ownedNullValue.eType = information.datavalue.AbstractStringValue
information.datatype.StringType.ownedMinLength.eType = information.datavalue.NumericValue
information.datatype.StringType.ownedMaxLength.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedDefaultValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedNullValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedMinValue.eType = information.datavalue.NumericValue
information.datatype.NumericType.ownedMaxValue.eType = information.datavalue.NumericValue
information.datatype.PhysicalQuantity.unit.eType = information.Unit
information.datavalue.DataValue._type.eType = capellacore.Type
information.datavalue.DataValueContainer.ownedDataValues.eType = information.datavalue.DataValue
information.datavalue.AbstractBooleanValue._booleanType.eType = information.datatype.BooleanType
information.datavalue.BooleanReference.referencedValue.eType = information.datavalue.AbstractBooleanValue
information.datavalue.BooleanReference.referencedProperty.eType = information.Property
information.datavalue.AbstractEnumerationValue._enumerationType.eType = information.datatype.Enumeration
information.datavalue.EnumerationLiteral.domainValue.eType = information.datavalue.DataValue
information.datavalue.EnumerationReference.referencedValue.eType = information.datavalue.AbstractEnumerationValue
information.datavalue.EnumerationReference.referencedProperty.eType = information.Property
information.datavalue.AbstractStringValue._stringType.eType = information.datatype.StringType
information.datavalue.StringReference.referencedValue.eType = information.datavalue.AbstractStringValue
information.datavalue.StringReference.referencedProperty.eType = information.Property
information.datavalue.NumericValue.unit.eType = information.Unit
information.datavalue.NumericValue._numericType.eType = information.datatype.NumericType
information.datavalue.NumericReference.referencedValue.eType = information.datavalue.NumericValue
information.datavalue.NumericReference.referencedProperty.eType = information.Property
information.datavalue.AbstractComplexValue._complexType.eType = capellacore.Classifier
information.datavalue.ComplexValue.ownedParts.eType = information.datavalue.ValuePart
information.datavalue.ComplexValueReference.referencedValue.eType = information.datavalue.AbstractComplexValue
information.datavalue.ComplexValueReference.referencedProperty.eType = information.Property
information.datavalue.ValuePart.referencedProperty.eType = information.Property
information.datavalue.ValuePart.ownedValue.eType = information.datavalue.DataValue
information.datavalue.AbstractExpressionValue._expressionType.eType = information.datatype.DataType
information.datavalue.BinaryExpression.ownedLeftOperand.eType = information.datavalue.DataValue
information.datavalue.BinaryExpression.ownedRightOperand.eType = information.datavalue.DataValue
information.datavalue.UnaryExpression.ownedOperand.eType = information.datavalue.DataValue
information.AbstractInstance.representingInstanceRoles.eType = interaction.InstanceRole
information.AssociationPkg.ownedAssociations.eType = information.Association
information.Association.ownedMembers.eType = information.Property
information.Association.navigableMembers.eType = information.Property
information.Class.keyParts.eType = information.KeyPart
information.Class.ownedStateMachines.eType = capellacommon.StateMachine
information.Class.ownedDataValues.eType = information.datavalue.DataValue
information.Class.ownedInformationRealizations.eType = information.InformationRealization
information.Collection.type.eType = capellacore.Type
information.Collection.index.eType = information.datatype.DataType
information.Collection.containedOperations.eType = information.Operation
information.CollectionValue.ownedElements.eType = information.datavalue.DataValue
information.CollectionValue.ownedDefaultElement.eType = information.datavalue.DataValue
information.CollectionValueReference.referencedValue.eType = information.AbstractCollectionValue
information.CollectionValueReference.referencedProperty.eType = information.Property
information.DataPkg.ownedDataPkgs.eType = information.DataPkg
information.DataPkg.ownedClasses.eType = information.Class
information.DataPkg.ownedKeyParts.eType = information.KeyPart
information.DataPkg.ownedCollections.eType = information.Collection
information.DataPkg.ownedUnits.eType = information.Unit
information.DataPkg.ownedDataTypes.eType = information.datatype.DataType
information.DataPkg.ownedSignals.eType = information.communication.Signal
information.DataPkg.ownedMessages.eType = information.communication.Message
information.DataPkg.ownedExceptions.eType = information.communication.Exception
information.DataPkg.ownedStateEvents.eType = capellacommon.StateEvent
information.KeyPart.property.eType = information.Property
information.MultiplicityElement.ownedDefaultValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMinValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMaxValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedNullValue.eType = information.datavalue.DataValue
information.MultiplicityElement.ownedMinCard.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMinLength.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMaxCard.eType = information.datavalue.NumericValue
information.MultiplicityElement.ownedMaxLength.eType = information.datavalue.NumericValue
information.Operation.ownedParameters.eType = information.Parameter
information.Operation.ownedOperationAllocation.eType = information.OperationAllocation
information.Operation.ownedExchangeItemRealizations.eType = information.ExchangeItemRealization
information.OperationAllocation._allocatedOperation.eType = information.Operation
information.OperationAllocation._allocatingOperation.eType = information.Operation
information.Property._association.eType = information.Association
information.Service.thrownExceptions.eType = information.communication.Exception
information.Service.messages.eType = information.communication.Message
information.Service.messageReferences.eType = information.communication.MessageReference
information.Union.discriminant.eType = information.UnionProperty
information.Union.defaultProperty.eType = information.UnionProperty
information.Union.containedUnionProperties.eType = information.UnionProperty
information.UnionProperty.qualifier.eType = information.datavalue.DataValue
information.Port.ownedProtocols.eType = capellacommon.StateMachine
information.Port.providedInterfaces.eType = cs.Interface
information.Port.requiredInterfaces.eType = cs.Interface
information.Port.ownedPortRealizations.eType = information.PortRealization
information.Port.ownedPortAllocations.eType = information.PortAllocation
information.ExchangeItem.ownedElements.eType = information.ExchangeItemElement
information.ExchangeItem.ownedInformationRealizations.eType = information.InformationRealization
information.ExchangeItem.ownedExchangeItemInstances.eType = information.ExchangeItemInstance
information.ExchangeItem.allocatorInterfaces.eType = cs.Interface
information.ExchangeItemElement.referencedProperties.eType = information.Property
information.ExchangeItemRealization._realizedItem.eType = modellingcore.AbstractExchangeItem
information.ExchangeItemRealization._realizingOperation.eType = information.Operation
information.AbstractEventOperation.invokingSequenceMessages.eType = interaction.SequenceMessage
information.datatype.DataType.realizedDataTypes.eType = information.datatype.DataType
information.datatype.DataType.realizingDataTypes.eType = information.datatype.DataType
information.datatype.DataType.realizingDataTypes.eOpposite = information.datatype.DataType.realizedDataTypes
information.Class.realizedClasses.eType = information.Class
information.Class.realizingClasses.eType = information.Class
information.Class.realizingClasses.eOpposite = information.Class.realizedClasses
information.Operation.allocatingOperations.eType = information.Operation
information.Operation.allocatedOperations.eType = information.Operation
information.Operation.allocatedOperations.eOpposite = information.Operation.allocatingOperations
information.Operation.realizedExchangeItems.eType = information.ExchangeItem
information.Port.incomingPortRealizations.eType = information.PortRealization
information.Port.outgoingPortRealizations.eType = information.PortRealization
information.Port.incomingPortAllocations.eType = information.PortAllocation
information.Port.outgoingPortAllocations.eType = information.PortAllocation
information.PortRealization._realizedPort.eType = information.Port
information.PortRealization._realizedPort.eOpposite = information.Port.incomingPortRealizations
information.PortRealization._realizingPort.eType = information.Port
information.PortRealization._realizingPort.eOpposite = information.Port.outgoingPortRealizations
information.PortAllocation._allocatedPort.eType = information.Port
information.PortAllocation._allocatedPort.eOpposite = information.Port.incomingPortAllocations
information.PortAllocation._allocatingPort.eType = information.Port
information.PortAllocation._allocatingPort.eOpposite = information.Port.outgoingPortAllocations
information.ExchangeItem.realizedExchangeItems.eType = information.ExchangeItem
information.ExchangeItem.realizingExchangeItems.eType = information.ExchangeItem
information.ExchangeItem.realizingExchangeItems.eOpposite = information.ExchangeItem.realizedExchangeItems
information.ExchangeItem.realizingOperations.eType = information.Operation
information.ExchangeItem.realizingOperations.eOpposite = information.Operation.realizedExchangeItems


information.DataPkg._staticEClass = False
information.DataPkg.eClass.eSuperTypes.extend((
    capellacore.AbstractDependenciesPkg.eClass,
    capellacore.AbstractExchangeItemPkg.eClass,
    information.AssociationPkg.eClass,
    information.datavalue.DataValueContainer.eClass,
    information.communication.MessageReferencePkg.eClass,
))

information.communication.SignalInstance._staticEClass = False
information.communication.SignalInstance.eClass.eSuperTypes.extend((
    information.AbstractInstance.eClass,
))


#print('information.cross_init done')
