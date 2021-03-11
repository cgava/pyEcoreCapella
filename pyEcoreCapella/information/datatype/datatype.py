print('datatype.datatype loading')
"""Definition of meta model 'datatype'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import GeneralizableElement, VisibilityKind
from information.datavalue import DataValueContainer
from modellingcore import FinalizableElement


name = 'datatype'
nsURI = 'http://www.polarsys.org/capella/core/information/datatype/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.information.datatype'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
NumericTypeKind = EEnum('NumericTypeKind', literals=['INTEGER', 'FLOAT'])


class DerivedRealizeddatatypes(EDerivedCollection):
    pass


class DerivedRealizingdatatypes(EDerivedCollection):
    pass


@abstract
class DataType(GeneralizableElement, DataValueContainer, FinalizableElement):

    discrete = EAttribute(eType=EBoolean, unique=True, derived=False,
                          changeable=True, default_value=True)
    minInclusive = EAttribute(eType=EBoolean, unique=True, derived=False,
                              changeable=True, default_value=True)
    maxInclusive = EAttribute(eType=EBoolean, unique=True, derived=False,
                              changeable=True, default_value=True)
    pattern = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    visibility = EAttribute(eType=VisibilityKind, unique=True, derived=False, changeable=True)
    _defaultValue = EReference(ordered=True, unique=True, containment=False,
                               derived=True, name='defaultValue', transient=True)
    _nullValue = EReference(ordered=True, unique=True, containment=False,
                            derived=True, name='nullValue', transient=True)
    ownedInformationRealizations = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    realizedDataTypes = EReference(ordered=True, unique=True, containment=False,
                                   derived=True, upper=-1, transient=True, derived_class=DerivedRealizeddatatypes)
    realizingDataTypes = EReference(ordered=True, unique=True, containment=False,
                                    derived=True, upper=-1, transient=True, derived_class=DerivedRealizingdatatypes)

    @property
    def defaultValue(self):
        raise NotImplementedError('Missing implementation for defaultValue')

    @property
    def nullValue(self):
        raise NotImplementedError('Missing implementation for nullValue')

    def __init__(self, *, discrete=None, minInclusive=None, maxInclusive=None, pattern=None, visibility=None, defaultValue=None, nullValue=None, ownedInformationRealizations=None, realizedDataTypes=None, realizingDataTypes=None, **kwargs):

        super().__init__(**kwargs)

        if discrete is not None:
            self.discrete = discrete

        if minInclusive is not None:
            self.minInclusive = minInclusive

        if maxInclusive is not None:
            self.maxInclusive = maxInclusive

        if pattern is not None:
            self.pattern = pattern

        if visibility is not None:
            self.visibility = visibility

        if defaultValue is not None:
            self.defaultValue = defaultValue

        if nullValue is not None:
            self.nullValue = nullValue

        if ownedInformationRealizations:
            self.ownedInformationRealizations.extend(ownedInformationRealizations)

        if realizedDataTypes:
            self.realizedDataTypes.extend(realizedDataTypes)

        if realizingDataTypes:
            self.realizingDataTypes.extend(realizingDataTypes)


class BooleanType(DataType):

    ownedLiterals = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedLiterals=None, ownedDefaultValue=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLiterals:
            self.ownedLiterals.extend(ownedLiterals)

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue


class Enumeration(DataType):

    ownedLiterals = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedNullValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    domainType = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, ownedLiterals=None, ownedDefaultValue=None, ownedNullValue=None, ownedMinValue=None, ownedMaxValue=None, domainType=None, **kwargs):

        super().__init__(**kwargs)

        if ownedLiterals:
            self.ownedLiterals.extend(ownedLiterals)

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue

        if ownedNullValue is not None:
            self.ownedNullValue = ownedNullValue

        if ownedMinValue is not None:
            self.ownedMinValue = ownedMinValue

        if ownedMaxValue is not None:
            self.ownedMaxValue = ownedMaxValue

        if domainType is not None:
            self.domainType = domainType


class StringType(DataType):

    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedNullValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinLength = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxLength = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ownedDefaultValue=None, ownedNullValue=None, ownedMinLength=None, ownedMaxLength=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue

        if ownedNullValue is not None:
            self.ownedNullValue = ownedNullValue

        if ownedMinLength is not None:
            self.ownedMinLength = ownedMinLength

        if ownedMaxLength is not None:
            self.ownedMaxLength = ownedMaxLength


class NumericType(DataType):

    kind = EAttribute(eType=NumericTypeKind, unique=True, derived=False,
                      changeable=True, default_value=NumericTypeKind.INTEGER)
    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedNullValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxValue = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, kind=None, ownedDefaultValue=None, ownedNullValue=None, ownedMinValue=None, ownedMaxValue=None, **kwargs):

        super().__init__(**kwargs)

        if kind is not None:
            self.kind = kind

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue

        if ownedNullValue is not None:
            self.ownedNullValue = ownedNullValue

        if ownedMinValue is not None:
            self.ownedMinValue = ownedMinValue

        if ownedMaxValue is not None:
            self.ownedMaxValue = ownedMaxValue


class PhysicalQuantity(NumericType):

    unit = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, unit=None, **kwargs):

        super().__init__(**kwargs)

        if unit is not None:
            self.unit = unit

print('datatype.datatype loaded')
