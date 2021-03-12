print('communication.__init__.py loading')
from pyecore.resources import global_registry
from .communication import getEClassifier, eClassifiers
from .communication import name, nsURI, nsPrefix, eClass
from .communication import CommunicationItem, CommunicationLink, CommunicationLinkExchanger, CommunicationLinkKind, CommunicationLinkProtocol, Exception, Message, MessageReference, MessageReferencePkg, Signal, SignalInstance
from . import communication
from .. import information


__all__ = ['CommunicationItem', 'CommunicationLink', 'CommunicationLinkExchanger', 'CommunicationLinkKind',
           'CommunicationLinkProtocol', 'Exception', 'Message', 'MessageReference', 'MessageReferencePkg', 'Signal', 'SignalInstance']

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

register_packages = [communication] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('communication.__init__.py loaded')
