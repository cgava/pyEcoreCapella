#print('deployment.__init__.py loading')
from pyecore.resources import global_registry
from .deployment import getEClassifier, eClassifiers
from .deployment import name, nsURI, nsPrefix, eClass
from .deployment import AbstractPhysicalInstance, ComponentInstance, ConnectionInstance, DeploymentAspect, DeploymentConfiguration, InstanceDeploymentLink, PartDeploymentLink, PortInstance, TypeDeploymentLink
from . import deployment
from .. import pa


__all__ = ['AbstractPhysicalInstance', 'ComponentInstance', 'ConnectionInstance', 'DeploymentAspect',
           'DeploymentConfiguration', 'InstanceDeploymentLink', 'PartDeploymentLink', 'PortInstance', 'TypeDeploymentLink']

eSubpackages = []
eSuperPackage = pa
deployment.eSubpackages = eSubpackages
deployment.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [deployment] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('deployment.__init__.py loaded')
