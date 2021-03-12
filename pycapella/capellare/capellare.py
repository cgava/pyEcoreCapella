#print('re.re loading')
"""Definition of meta model 're'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from emde import ElementExtension, ExtensibleElement


name = 're'
nsURI = 'http://www.polarsys.org/capella/common/re/1.4.0'
nsPrefix = 're'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
CatalogElementKind = EEnum('CatalogElementKind', literals=['REC', 'RPL', 'REC_RPL', 'GROUPING'])


@abstract
class ReElementContainer(EObject, metaclass=MetaEClass):

    ownedElements = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedElements=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if ownedElements:
            self.ownedElements.extend(ownedElements)


@abstract
class ReAbstractElement(ExtensibleElement):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)

    def __init__(self, *, id=None, **kwargs):

        super().__init__(**kwargs)

        if id is not None:
            self.id = id


@abstract
class ReNamedElement(ReAbstractElement):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class CatalogElementLink(ReAbstractElement):

    unsynchronizedFeatures = EAttribute(
        eType=EString, unique=True, derived=False, changeable=True, upper=-1)
    suffixed = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)
    origin = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, source=None, target=None, origin=None, unsynchronizedFeatures=None, suffixed=None, **kwargs):

        super().__init__(**kwargs)

        if unsynchronizedFeatures:
            self.unsynchronizedFeatures.extend(unsynchronizedFeatures)

        if suffixed is not None:
            self.suffixed = suffixed

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target

        if origin is not None:
            self.origin = origin


@abstract
class ReDescriptionElement(ReNamedElement):

    description = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, description=None, **kwargs):

        super().__init__(**kwargs)

        if description is not None:
            self.description = description


class CompliancyDefinitionPkg(ReNamedElement):

    ownedDefinitions = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedDefinitions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDefinitions:
            self.ownedDefinitions.extend(ownedDefinitions)


class CatalogElementPkg(ReNamedElement, ReElementContainer):

    ownedElementPkgs = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedElementPkgs=None, **kwargs):

        super().__init__(**kwargs)

        if ownedElementPkgs:
            self.ownedElementPkgs.extend(ownedElementPkgs)


class CompliancyDefinition(ReDescriptionElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DerivedReferencedelements(EDerivedCollection):
    pass


class DerivedReplicatedelements(EDerivedCollection):
    pass


class CatalogElement(ReDescriptionElement, ReElementContainer):

    kind = EAttribute(eType=CatalogElementKind, unique=True, derived=False,
                      changeable=True, default_value=CatalogElementKind.REC)
    author = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    environment = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    suffix = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    purpose = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    readOnly = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=False)
    version = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    tags = EAttribute(eType=EString, unique=True, derived=False, changeable=True, upper=-1)
    origin = EReference(ordered=True, unique=True, containment=False, derived=False)
    currentCompliancy = EReference(ordered=True, unique=True, containment=False, derived=False)
    defaultReplicaCompliancy = EReference(
        ordered=True, unique=True, containment=False, derived=False)
    ownedLinks = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    referencedElements = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedReferencedelements)
    replicatedElements = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedReplicatedelements)

    def __init__(self, *, kind=None, author=None, environment=None, suffix=None, purpose=None, readOnly=None, version=None, tags=None, origin=None, currentCompliancy=None, defaultReplicaCompliancy=None, ownedLinks=None, referencedElements=None, replicatedElements=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if author is not None:
            self.author = author

        if environment is not None:
            self.environment = environment

        if suffix is not None:
            self.suffix = suffix

        if purpose is not None:
            self.purpose = purpose

        if readOnly is not None:
            self.readOnly = readOnly

        if version is not None:
            self.version = version

        if tags:
            self.tags.extend(tags)

        if origin is not None:
            self.origin = origin

        if currentCompliancy is not None:
            self.currentCompliancy = currentCompliancy

        if defaultReplicaCompliancy is not None:
            self.defaultReplicaCompliancy = defaultReplicaCompliancy

        if ownedLinks:
            self.ownedLinks.extend(ownedLinks)

        if referencedElements:
            self.referencedElements.extend(referencedElements)

        if replicatedElements:
            self.replicatedElements.extend(replicatedElements)


class RecCatalog(CatalogElementPkg, ElementExtension):

    ownedCompliancyDefinitionPkg = EReference(
        ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedCompliancyDefinitionPkg=None, **kwargs):

        super().__init__(**kwargs)

        if ownedCompliancyDefinitionPkg is not None:
            self.ownedCompliancyDefinitionPkg = ownedCompliancyDefinitionPkg


class GroupingElementPkg(CatalogElementPkg, ElementExtension):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

#print('re.re loaded')
