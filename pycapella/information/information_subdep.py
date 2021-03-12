from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import CapellaElement, Feature, TypedElement
from modellingcore import FinalizableElement


AggregationKind = EEnum('AggregationKind', literals=[
                        'UNSET', 'ASSOCIATION', 'AGGREGATION', 'COMPOSITION'])

class DerivedRepresentinginstanceroles(EDerivedCollection):
    pass

@abstract
class MultiplicityElement(CapellaElement):

    ordered = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    unique = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    minInclusive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    maxInclusive = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    ownedDefaultValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedNullValue = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinCard = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMinLength = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxCard = EReference(ordered=True, unique=True, containment=True, derived=False)
    ownedMaxLength = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, ordered=None, unique=None, minInclusive=None, maxInclusive=None, ownedDefaultValue=None, ownedMinValue=None, ownedMaxValue=None, ownedNullValue=None, ownedMinCard=None, ownedMinLength=None, ownedMaxCard=None, ownedMaxLength=None, **kwargs):

        super().__init__(**kwargs)

        if ordered is not None:
            self.ordered = ordered

        if unique is not None:
            self.unique = unique

        if minInclusive is not None:
            self.minInclusive = minInclusive

        if maxInclusive is not None:
            self.maxInclusive = maxInclusive

        if ownedDefaultValue is not None:
            self.ownedDefaultValue = ownedDefaultValue

        if ownedMinValue is not None:
            self.ownedMinValue = ownedMinValue

        if ownedMaxValue is not None:
            self.ownedMaxValue = ownedMaxValue

        if ownedNullValue is not None:
            self.ownedNullValue = ownedNullValue

        if ownedMinCard is not None:
            self.ownedMinCard = ownedMinCard

        if ownedMinLength is not None:
            self.ownedMinLength = ownedMinLength

        if ownedMaxCard is not None:
            self.ownedMaxCard = ownedMaxCard

        if ownedMaxLength is not None:
            self.ownedMaxLength = ownedMaxLength

class Property(Feature, TypedElement, MultiplicityElement, FinalizableElement):

    aggregationKind = EAttribute(eType=AggregationKind, unique=True,
                                 derived=False, changeable=True, default_value=AggregationKind.UNSET)
    isDerived = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isReadOnly = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isPartOfKey = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    _association = EReference(ordered=True, unique=True, containment=False,
                              derived=True, name='association', transient=True)

    @property
    def association(self):
        raise NotImplementedError('Missing implementation for association')

    def __init__(self, *, aggregationKind=None, isDerived=None, isReadOnly=None, isPartOfKey=None, association=None, **kwargs):

        super().__init__(**kwargs)

        if aggregationKind is not None:
            self.aggregationKind = aggregationKind

        if isDerived is not None:
            self.isDerived = isDerived

        if isReadOnly is not None:
            self.isReadOnly = isReadOnly

        if isPartOfKey is not None:
            self.isPartOfKey = isPartOfKey

        if association is not None:
            self.association = association


@abstract
class AbstractInstance(Property):

    representingInstanceRoles = EReference(ordered=True, unique=True, containment=False,
                                           derived=True, upper=-1, transient=True, derived_class=DerivedRepresentinginstanceroles)

    def __init__(self, *, representingInstanceRoles=None, **kwargs):

        super().__init__(**kwargs)

        if representingInstanceRoles:
            self.representingInstanceRoles.extend(representingInstanceRoles)