#print('ctx.__init__.py loading')
from pyecore.resources import global_registry
from .ctx import getEClassifier, eClassifiers
from .ctx import name, nsURI, nsPrefix, eClass
from .ctx import Capability, CapabilityExploitation, CapabilityInvolvement, CapabilityPkg, Mission, MissionInvolvement, MissionPkg, OperationalAnalysisRealization, SystemAnalysis, SystemCommunication, SystemCommunicationHook, SystemComponent, SystemComponentPkg, SystemFunction, SystemFunctionPkg
from . import ctx

__all__ = ['Capability', 'CapabilityExploitation', 'CapabilityInvolvement', 'CapabilityPkg', 'Mission', 'MissionInvolvement', 'MissionPkg', 'OperationalAnalysisRealization',
           'SystemAnalysis', 'SystemCommunication', 'SystemCommunicationHook', 'SystemComponent', 'SystemComponentPkg', 'SystemFunction', 'SystemFunctionPkg']

eSubpackages = []
eSuperPackage = None
ctx.eSubpackages = eSubpackages
ctx.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [ctx] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('ctx.__init__.py loaded')
