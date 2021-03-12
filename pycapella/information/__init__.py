print('information.__init__.py loading')
from pyecore.resources import global_registry
from .information import getEClassifier, eClassifiers
from .information import name, nsURI, nsPrefix, eClass
from .information import AbstractCollectionValue, AbstractEventOperation, AbstractInstance, AggregationKind, Association, AssociationPkg, Class, Collection, CollectionKind, CollectionValue, CollectionValueReference, DataPkg, DomainElement, ElementKind, ExchangeItem, ExchangeItemElement, ExchangeItemInstance, ExchangeItemRealization, ExchangeMechanism, InformationRealization, KeyPart, MultiplicityElement, Operation, OperationAllocation, Parameter, ParameterDirection, PassingMode, Port, PortAllocation, PortRealization, Property, Service, SynchronismKind, Union, UnionKind, UnionProperty, Unit
from . import information
from . import communication

from . import datatype

from . import datavalue


__all__ = ['AbstractCollectionValue', 'AbstractEventOperation', 'AbstractInstance', 'AggregationKind', 'Association', 'AssociationPkg', 'Class', 'Collection', 'CollectionKind', 'CollectionValue', 'CollectionValueReference', 'DataPkg', 'DomainElement', 'ElementKind', 'ExchangeItem', 'ExchangeItemElement', 'ExchangeItemInstance',
           'ExchangeItemRealization', 'ExchangeMechanism', 'InformationRealization', 'KeyPart', 'MultiplicityElement', 'Operation', 'OperationAllocation', 'Parameter', 'ParameterDirection', 'PassingMode', 'Port', 'PortAllocation', 'PortRealization', 'Property', 'Service', 'SynchronismKind', 'Union', 'UnionKind', 'UnionProperty', 'Unit']

eSubpackages = [communication, datatype, datavalue]
eSuperPackage = None
information.eSubpackages = eSubpackages
information.eSuperPackage = eSuperPackage

otherClassifiers = [AggregationKind, ParameterDirection, PassingMode,
                    SynchronismKind, UnionKind, ExchangeMechanism, ElementKind, CollectionKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [information] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('information.__init__.py loaded')
