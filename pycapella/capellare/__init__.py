#print('re.__init__.py loading')
from pyecore.resources import global_registry
from .capellare import getEClassifier, eClassifiers
from .capellare import name, nsURI, nsPrefix, eClass
from .capellare import CatalogElement, CatalogElementKind, CatalogElementLink, CatalogElementPkg, CompliancyDefinition, CompliancyDefinitionPkg, GroupingElementPkg, ReAbstractElement, RecCatalog, ReDescriptionElement, ReElementContainer, ReNamedElement
from . import capellare

__all__ = ['CatalogElement', 'CatalogElementKind', 'CatalogElementLink', 'CatalogElementPkg', 'CompliancyDefinition', 'CompliancyDefinitionPkg',
           'GroupingElementPkg', 'ReAbstractElement', 'RecCatalog', 'ReDescriptionElement', 'ReElementContainer', 'ReNamedElement']

eSubpackages = []
eSuperPackage = None
capellare.eSubpackages = eSubpackages
capellare.eSuperPackage = eSuperPackage

otherClassifiers = [CatalogElementKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [capellare] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


#print('re.__init__.py loaded')
