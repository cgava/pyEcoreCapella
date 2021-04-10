#print('activity.__init__.py loading')
from pyecore.resources import global_registry
from .activity import getEClassifier, eClassifiers
from .activity import name, nsURI, nsPrefix, eClass
from .activity import AbstractAction, AbstractActivity, AcceptEventAction, ActivityEdge, ActivityExchange, ActivityGroup, ActivityNode, ActivityPartition, CallAction, CallBehaviorAction, ControlFlow, ExceptionHandler, ExecutableNode, InputPin, InterruptibleActivityRegion, InvocationAction, ObjectFlow, ObjectNode, ObjectNodeKind, ObjectNodeOrderingKind, OutputPin, Pin, SendSignalAction, StructuredActivityNode, ValuePin
from . import activity

__all__ = ['AbstractAction', 'AbstractActivity', 'AcceptEventAction', 'ActivityEdge', 'ActivityExchange', 'ActivityGroup', 'ActivityNode', 'ActivityPartition', 'CallAction', 'CallBehaviorAction', 'ControlFlow', 'ExceptionHandler',
           'ExecutableNode', 'InputPin', 'InterruptibleActivityRegion', 'InvocationAction', 'ObjectFlow', 'ObjectNode', 'ObjectNodeKind', 'ObjectNodeOrderingKind', 'OutputPin', 'Pin', 'SendSignalAction', 'StructuredActivityNode', 'ValuePin']

eSubpackages = []
eSuperPackage = None
activity.eSubpackages = eSubpackages
activity.eSuperPackage = eSuperPackage

otherClassifiers = [ObjectNodeOrderingKind, ObjectNodeKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [activity] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('activity.__init__.py loaded')
