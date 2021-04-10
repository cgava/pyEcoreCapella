#print('fa.__init__.py loading')
from pyecore.resources import global_registry
from .fa import getEClassifier, eClassifiers
from .fa import name, nsURI, nsPrefix, eClass
from .fa import AbstractFunction, AbstractFunctionalArchitecture, AbstractFunctionalBlock, AbstractFunctionalChainContainer, AbstractFunctionAllocation, ComponentExchange, ComponentExchangeAllocation, ComponentExchangeAllocator, ComponentExchangeCategory, ComponentExchangeEnd, ComponentExchangeFunctionalExchangeAllocation, ComponentExchangeKind, ComponentExchangeRealization, ComponentFunctionalAllocation, ComponentPort, ComponentPortAllocation, ComponentPortAllocationEnd, ComponentPortKind, ControlNode, ControlNodeKind, ExchangeCategory, ExchangeContainment, ExchangeLink, ExchangeSpecification, ExchangeSpecificationRealization, FunctionalChain, FunctionalChainInvolvement, FunctionalChainInvolvementFunction, FunctionalChainInvolvementLink, FunctionalChainKind, FunctionalChainRealization, FunctionalChainReference, FunctionalExchange, FunctionalExchangeRealization, FunctionalExchangeSpecification, FunctionInputPort, FunctionKind, FunctionOutputPort, FunctionPkg, FunctionPort, FunctionRealization, FunctionSpecification, OrientationPortKind, ReferenceHierarchyContext, SequenceLink, SequenceLinkEnd
from . import fa

__all__ = ['AbstractFunction', 'AbstractFunctionalArchitecture', 'AbstractFunctionalBlock', 'AbstractFunctionalChainContainer', 'AbstractFunctionAllocation', 'ComponentExchange', 'ComponentExchangeAllocation', 'ComponentExchangeAllocator', 'ComponentExchangeCategory', 'ComponentExchangeEnd', 'ComponentExchangeFunctionalExchangeAllocation', 'ComponentExchangeKind', 'ComponentExchangeRealization', 'ComponentFunctionalAllocation', 'ComponentPort', 'ComponentPortAllocation', 'ComponentPortAllocationEnd', 'ComponentPortKind', 'ControlNode', 'ControlNodeKind', 'ExchangeCategory', 'ExchangeContainment',
           'ExchangeLink', 'ExchangeSpecification', 'ExchangeSpecificationRealization', 'FunctionalChain', 'FunctionalChainInvolvement', 'FunctionalChainInvolvementFunction', 'FunctionalChainInvolvementLink', 'FunctionalChainKind', 'FunctionalChainRealization', 'FunctionalChainReference', 'FunctionalExchange', 'FunctionalExchangeRealization', 'FunctionalExchangeSpecification', 'FunctionInputPort', 'FunctionKind', 'FunctionOutputPort', 'FunctionPkg', 'FunctionPort', 'FunctionRealization', 'FunctionSpecification', 'OrientationPortKind', 'ReferenceHierarchyContext', 'SequenceLink', 'SequenceLinkEnd']

eSubpackages = []
eSuperPackage = None
fa.eSubpackages = eSubpackages
fa.eSuperPackage = eSuperPackage

otherClassifiers = [FunctionalChainKind, FunctionKind, ComponentExchangeKind,
                    ComponentPortKind, OrientationPortKind, ControlNodeKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [fa] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('fa.__init__.py loaded')
