#print('re.__init__.py loading')
from pyecore.resources import global_registry
from .re import getEClassifier, eClassifiers
from .re import name, nsURI, nsPrefix, eClass
from .re import CatalogElement, CatalogElementKind, CatalogElementLink, CatalogElementPkg, CompliancyDefinition, CompliancyDefinitionPkg, GroupingElementPkg, ReAbstractElement, RecCatalog, ReDescriptionElement, ReElementContainer, ReNamedElement
from . import re

__all__ = ['CatalogElement', 'CatalogElementKind', 'CatalogElementLink', 'CatalogElementPkg', 'CompliancyDefinition', 'CompliancyDefinitionPkg',
           'GroupingElementPkg', 'ReAbstractElement', 'RecCatalog', 'ReDescriptionElement', 'ReElementContainer', 'ReNamedElement']

eSubpackages = []
eSuperPackage = None
re.eSubpackages = eSubpackages
re.eSuperPackage = eSuperPackage

otherClassifiers = [CatalogElementKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [re] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('re.__init__.py loaded')
