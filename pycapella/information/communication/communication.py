print('communication.communication loading')
"""Definition of meta model 'communication'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from behavior import AbstractSignal
from capellacore import CapellaElement, Classifier, Relationship, Structure, VisibilityKind
from information.datavalue import DataValueContainer
# from information import AbstractInstance


name = 'communication'
nsURI = 'http://www.polarsys.org/capella/core/information/communication/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.information.communication'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
CommunicationLinkKind = EEnum('CommunicationLinkKind', literals=[
                              'UNSET', 'PRODUCE', 'CONSUME', 'SEND', 'RECEIVE', 'CALL', 'EXECUTE', 'WRITE', 'ACCESS', 'ACQUIRE', 'TRANSMIT'])

CommunicationLinkProtocol = EEnum('CommunicationLinkProtocol', literals=[
                                  'UNSET', 'UNICAST', 'MULTICAST', 'BROADCAST', 'SYNCHRONOUS', 'ASYNCHRONOUS', 'READ', 'ACCEPT'])


class DerivedProduce(EDerivedCollection):
    pass


class DerivedConsume(EDerivedCollection):
    pass


class DerivedSend(EDerivedCollection):
    pass


class DerivedReceive(EDerivedCollection):
    pass


class DerivedCall(EDerivedCollection):
    pass


class DerivedExecute(EDerivedCollection):
    pass


class DerivedWrite(EDerivedCollection):
    pass


class DerivedAccess(EDerivedCollection):
    pass


class DerivedAcquire(EDerivedCollection):
    pass


class DerivedTransmit(EDerivedCollection):
    pass


@abstract
class CommunicationLinkExchanger(EObject, metaclass=MetaEClass):

    ownedCommunicationLinks = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    produce = EReference(ordered=True, unique=True, containment=False,
                         derived=True, upper=-1, transient=True, derived_class=DerivedProduce)
    consume = EReference(ordered=True, unique=True, containment=False,
                         derived=True, upper=-1, transient=True, derived_class=DerivedConsume)
    send = EReference(ordered=True, unique=True, containment=False, derived=True,
                      upper=-1, transient=True, derived_class=DerivedSend)
    receive = EReference(ordered=True, unique=True, containment=False,
                         derived=True, upper=-1, transient=True, derived_class=DerivedReceive)
    call = EReference(ordered=True, unique=True, containment=False, derived=True,
                      upper=-1, transient=True, derived_class=DerivedCall)
    execute = EReference(ordered=True, unique=True, containment=False,
                         derived=True, upper=-1, transient=True, derived_class=DerivedExecute)
    write = EReference(ordered=True, unique=True, containment=False, derived=True,
                       upper=-1, transient=True, derived_class=DerivedWrite)
    access = EReference(ordered=True, unique=True, containment=False, derived=True,
                        upper=-1, transient=True, derived_class=DerivedAccess)
    acquire = EReference(ordered=True, unique=True, containment=False,
                         derived=True, upper=-1, transient=True, derived_class=DerivedAcquire)
    transmit = EReference(ordered=True, unique=True, containment=False,
                          derived=True, upper=-1, transient=True, derived_class=DerivedTransmit)

    def __init__(self, *, ownedCommunicationLinks=None, produce=None, consume=None, send=None, receive=None, call=None, execute=None, write=None, access=None, acquire=None, transmit=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if ownedCommunicationLinks:
            self.ownedCommunicationLinks.extend(ownedCommunicationLinks)

        if produce:
            self.produce.extend(produce)

        if consume:
            self.consume.extend(consume)

        if send:
            self.send.extend(send)

        if receive:
            self.receive.extend(receive)

        if call:
            self.call.extend(call)

        if execute:
            self.execute.extend(execute)

        if write:
            self.write.extend(write)

        if access:
            self.access.extend(access)

        if acquire:
            self.acquire.extend(acquire)

        if transmit:
            self.transmit.extend(transmit)


class CommunicationLink(CapellaElement):

    kind = EAttribute(eType=CommunicationLinkKind, unique=True, derived=False, changeable=True)
    protocol = EAttribute(eType=CommunicationLinkProtocol,
                          unique=True, derived=False, changeable=True)
    exchangeItem = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, kind=None, protocol=None, exchangeItem=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if protocol is not None:
            self.protocol = protocol

        if exchangeItem is not None:
            self.exchangeItem = exchangeItem


class MessageReference(Relationship):

    message = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, message=None, **kwargs):

        super().__init__(**kwargs)

        if message is not None:
            self.message = message


@abstract
class MessageReferencePkg(Structure):

    ownedMessageReferences = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedMessageReferences=None, **kwargs):

        super().__init__(**kwargs)

        if ownedMessageReferences:
            self.ownedMessageReferences.extend(ownedMessageReferences)


class DerivedProperties(EDerivedCollection):
    pass


@abstract
class CommunicationItem(Classifier, DataValueContainer):

    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)
    ownedStateMachines = EReference(ordered=True, unique=True,
                                    containment=True, derived=False, upper=-1)
    properties = EReference(ordered=True, unique=True, containment=False,
                            derived=True, upper=-1, transient=True, derived_class=DerivedProperties)

    def __init__(self, *, visibility=None, ownedStateMachines=None, properties=None, **kwargs):

        super().__init__(**kwargs)

        if visibility is not None:
            self.visibility = visibility

        if ownedStateMachines:
            self.ownedStateMachines.extend(ownedStateMachines)

        if properties:
            self.properties.extend(properties)


class Exception(CommunicationItem):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Message(CommunicationItem):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class SignalInstance(EObject, metaclass=MetaEClass):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Signal(CommunicationItem, AbstractSignal):

    signalInstances = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, signalInstances=None, **kwargs):

        super().__init__(**kwargs)

        if signalInstances:
            self.signalInstances.extend(signalInstances)

print('communication.communication loaded')
