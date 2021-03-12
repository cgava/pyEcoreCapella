print('emde.emde loading')
"""Definition of meta model 'emde'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'emde'
nsURI = 'http://www.polarsys.org/kitalpha/emde/1.0.0'
nsPrefix = 'emde'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class Element(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class ExtensibleElement(Element):

    ownedExtensions = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedExtensions=None, **kwargs):

        super().__init__(**kwargs)

        if ownedExtensions:
            self.ownedExtensions.extend(ownedExtensions)


@abstract
class ElementExtension(ExtensibleElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

print('emde.emde loaded')
