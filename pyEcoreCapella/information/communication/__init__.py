
from .communication import getEClassifier, eClassifiers
from .communication import name, nsURI, nsPrefix, eClass
from .communication import CommunicationItem, Exception, Message, MessageReference, MessageReferencePkg, Signal, SignalInstance, CommunicationLinkKind, CommunicationLinkProtocol, CommunicationLink, CommunicationLinkExchanger

from capellacore import GeneralizableElement, EnumerationPropertyLiteral, Trace, Generalization, AbstractPropertyValue, TypedElement, EnumerationPropertyType, NamingRule, Type, Feature, PropertyValuePkg, PropertyValueGroup
from capellacommon import GenericTrace, StateMachine
from modellingcore import AbstractConstraint, AbstractTrace, AbstractTypedElement, ModelElement, AbstractInformationFlow, AbstractType
from requirement import RequirementsTrace, Requirement
from emde import ElementExtension
from information.datavalue import NumericValue, DataValue
from information import ExchangeItem, Property, Association, Property
from interaction import InstanceRole

from . import communication
from .. import information


__all__ = ['CommunicationItem', 'Exception', 'Message', 'MessageReference', 'MessageReferencePkg', 'Signal',
           'SignalInstance', 'CommunicationLinkKind', 'CommunicationLinkProtocol', 'CommunicationLink', 'CommunicationLinkExchanger']

eSubpackages = []
eSuperPackage = information
communication.eSubpackages = eSubpackages
communication.eSuperPackage = eSuperPackage


otherClassifiers = [CommunicationLinkKind, CommunicationLinkProtocol]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)
