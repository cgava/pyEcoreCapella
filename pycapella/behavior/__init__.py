#print('behavior.__init__.py loading')
from pyecore.resources import global_registry
from .behavior import getEClassifier, eClassifiers
from .behavior import name, nsURI, nsPrefix, eClass
from .behavior import AbstractBehavior, AbstractEvent, AbstractMessageEvent, AbstractSignal, AbstractSignalEvent, AbstractTimeEvent, TimeExpression
from . import behavior

__all__ = ['AbstractBehavior', 'AbstractEvent', 'AbstractMessageEvent',
           'AbstractSignal', 'AbstractSignalEvent', 'AbstractTimeEvent', 'TimeExpression']

eSubpackages = []
eSuperPackage = None
behavior.eSubpackages = eSubpackages
behavior.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [behavior] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('behavior.__init__.py loaded')
