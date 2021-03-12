print('datatype.__init__.py loading')
from pyecore.resources import global_registry
from .datatype import getEClassifier, eClassifiers
from .datatype import name, nsURI, nsPrefix, eClass
from .datatype import BooleanType, DataType, Enumeration, NumericType, NumericTypeKind, PhysicalQuantity, StringType
from . import datatype
from .. import information


__all__ = ['BooleanType', 'DataType', 'Enumeration', 'NumericType',
           'NumericTypeKind', 'PhysicalQuantity', 'StringType']

eSubpackages = []
eSuperPackage = information
datatype.eSubpackages = eSubpackages
datatype.eSuperPackage = eSuperPackage

otherClassifiers = [NumericTypeKind]

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [datatype] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack


print('datatype.__init__.py loaded')
