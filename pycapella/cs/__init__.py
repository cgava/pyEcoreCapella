print('cs.__init__.py loading')
from pyecore.resources import global_registry
from .cs import getEClassifier, eClassifiers
from .cs import name, nsURI, nsPrefix, eClass
from .cs import AbstractDeploymentLink, AbstractPathInvolvedElement, AbstractPhysicalArtifact, AbstractPhysicalLinkEnd, AbstractPhysicalPathLink, ArchitectureAllocation, Block, BlockArchitecture, BlockArchitecturePkg, Component, ComponentArchitecture, ComponentPkg, ComponentRealization, DeployableElement, DeploymentTarget, ExchangeItemAllocation, Interface, InterfaceAllocation, InterfaceAllocator, InterfaceImplementation, InterfacePkg, InterfaceUse, Part, PhysicalLink, PhysicalLinkCategory, PhysicalLinkEnd, PhysicalLinkRealization, PhysicalPath, PhysicalPathInvolvement, PhysicalPathRealization, PhysicalPathReference, PhysicalPort, PhysicalPortRealization, ProvidedInterfaceLink, RequiredInterfaceLink
from . import cs

__all__ = ['AbstractDeploymentLink', 'AbstractPathInvolvedElement', 'AbstractPhysicalArtifact', 'AbstractPhysicalLinkEnd', 'AbstractPhysicalPathLink', 'ArchitectureAllocation', 'Block', 'BlockArchitecture', 'BlockArchitecturePkg', 'Component', 'ComponentArchitecture', 'ComponentPkg', 'ComponentRealization', 'DeployableElement', 'DeploymentTarget', 'ExchangeItemAllocation', 'Interface',
           'InterfaceAllocation', 'InterfaceAllocator', 'InterfaceImplementation', 'InterfacePkg', 'InterfaceUse', 'Part', 'PhysicalLink', 'PhysicalLinkCategory', 'PhysicalLinkEnd', 'PhysicalLinkRealization', 'PhysicalPath', 'PhysicalPathInvolvement', 'PhysicalPathRealization', 'PhysicalPathReference', 'PhysicalPort', 'PhysicalPortRealization', 'ProvidedInterfaceLink', 'RequiredInterfaceLink']

eSubpackages = []
eSuperPackage = None
cs.eSubpackages = eSubpackages
cs.eSuperPackage = eSuperPackage

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [cs] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('cs.__init__.py loaded')
