"""Definition of meta model 'modellingcore'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from emde import ExtensibleElement


name = 'modellingcore'
nsURI = 'http://www.polarsys.org/capella/common/core/1.4.0'
nsPrefix = 'org.polarsys.capella.common.data.core'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)
ParameterEffectKind = EEnum('ParameterEffectKind', literals=['create', 'read', 'update', 'delete'])

RateKind = EEnum('RateKind', literals=['Unspecified', 'Continuous', 'Discrete'])


class DerivedConstraints(EDerivedCollection):
    pass


@abstract
class ModelElement(ExtensibleElement):

    id = EAttribute(eType=EString, unique=True, derived=False, changeable=True, iD=True)
    sid = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    constraints = EReference(ordered=True, unique=True, containment=False,
                             derived=True, upper=-1, transient=True, derived_class=DerivedConstraints)
    ownedConstraints = EReference(ordered=True, unique=True,
                                  containment=True, derived=False, upper=-1)
    ownedMigratedElements = EReference(ordered=True, unique=True,
                                       containment=True, derived=False, upper=-1)

    def __init__(self, *, id=None, sid=None, constraints=None, ownedConstraints=None, ownedMigratedElements=None, **kwargs):

        super().__init__(**kwargs)

        if id is not None:
            self.id = id

        if sid is not None:
            self.sid = sid

        if constraints:
            self.constraints.extend(constraints)

        if ownedConstraints:
            self.ownedConstraints.extend(ownedConstraints)

        if ownedMigratedElements:
            self.ownedMigratedElements.extend(ownedMigratedElements)

    def destroy(self):

        raise NotImplementedError('operation destroy(...) not yet implemented')

    def getFullLabel(self):

        raise NotImplementedError('operation getFullLabel(...) not yet implemented')

    def getLabel(self):

        raise NotImplementedError('operation getLabel(...) not yet implemented')

    def hasUnnamedLabel(self):

        raise NotImplementedError('operation hasUnnamedLabel(...) not yet implemented')


@abstract
class AbstractRelationship(ModelElement):

    realizedFlow = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, realizedFlow=None, **kwargs):

        super().__init__(**kwargs)

        if realizedFlow is not None:
            self.realizedFlow = realizedFlow


@abstract
class AbstractNamedElement(ModelElement):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, **kwargs):

        super().__init__(**kwargs)

        if name is not None:
            self.name = name


class DerivedIncominginformationflows(EDerivedCollection):
    pass


class DerivedOutgoinginformationflows(EDerivedCollection):
    pass


class DerivedInformationflows(EDerivedCollection):
    pass


@abstract
class InformationsExchanger(ModelElement):

    incomingInformationFlows = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedIncominginformationflows)
    outgoingInformationFlows = EReference(ordered=True, unique=True, containment=False,
                                          derived=True, upper=-1, transient=True, derived_class=DerivedOutgoinginformationflows)
    informationFlows = EReference(ordered=True, unique=True, containment=False,
                                  derived=True, upper=-1, transient=True, derived_class=DerivedInformationflows)

    def __init__(self, *, incomingInformationFlows=None, outgoingInformationFlows=None, informationFlows=None, **kwargs):

        super().__init__(**kwargs)

        if incomingInformationFlows:
            self.incomingInformationFlows.extend(incomingInformationFlows)

        if outgoingInformationFlows:
            self.outgoingInformationFlows.extend(outgoingInformationFlows)

        if informationFlows:
            self.informationFlows.extend(informationFlows)


class DerivedIncomingtraces(EDerivedCollection):
    pass


class DerivedOutgoingtraces(EDerivedCollection):
    pass


@abstract
class TraceableElement(ModelElement):

    incomingTraces = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedIncomingtraces)
    outgoingTraces = EReference(ordered=True, unique=True, containment=False,
                                derived=True, upper=-1, transient=True, derived_class=DerivedOutgoingtraces)

    def __init__(self, *, incomingTraces=None, outgoingTraces=None, **kwargs):

        super().__init__(**kwargs)

        if incomingTraces:
            self.incomingTraces.extend(incomingTraces)

        if outgoingTraces:
            self.outgoingTraces.extend(outgoingTraces)


@abstract
class FinalizableElement(ModelElement):

    final = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, final=None, **kwargs):

        super().__init__(**kwargs)

        if final is not None:
            self.final = final


@abstract
class PublishableElement(ModelElement):

    visibleInDoc = EAttribute(eType=EBoolean, unique=True, derived=False,
                              changeable=True, default_value=True)
    visibleInLM = EAttribute(eType=EBoolean, unique=True, derived=False,
                             changeable=True, default_value=True)

    def __init__(self, *, visibleInDoc=None, visibleInLM=None, **kwargs):

        super().__init__(**kwargs)

        if visibleInDoc is not None:
            self.visibleInDoc = visibleInDoc

        if visibleInLM is not None:
            self.visibleInLM = visibleInLM


@abstract
class AbstractConstraint(ModelElement):

    constrainedElements = EReference(ordered=True, unique=True,
                                     containment=False, derived=False, upper=-1)
    ownedSpecification = EReference(ordered=True, unique=True, containment=True, derived=False)
    _context = EReference(ordered=True, unique=True, containment=False,
                          derived=True, name='context', transient=True)

    @property
    def context(self):
        raise NotImplementedError('Missing implementation for context')

    def __init__(self, *, constrainedElements=None, ownedSpecification=None, context=None, **kwargs):

        super().__init__(**kwargs)

        if constrainedElements:
            self.constrainedElements.extend(constrainedElements)

        if ownedSpecification is not None:
            self.ownedSpecification = ownedSpecification

        if context is not None:
            self.context = context


class DerivedAbstracttypedelements(EDerivedCollection):
    pass


@abstract
class AbstractType(AbstractNamedElement):

    abstractTypedElements = EReference(ordered=True, unique=True, containment=False,
                                       derived=True, upper=-1, transient=True, derived_class=DerivedAbstracttypedelements)

    def __init__(self, *, abstractTypedElements=None, **kwargs):

        super().__init__(**kwargs)

        if abstractTypedElements:
            self.abstractTypedElements.extend(abstractTypedElements)


@abstract
class AbstractTypedElement(AbstractNamedElement):

    abstractType = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, abstractType=None, **kwargs):

        super().__init__(**kwargs)

        if abstractType is not None:
            self.abstractType = abstractType


@abstract
class AbstractTrace(TraceableElement):

    targetElement = EReference(ordered=True, unique=True, containment=False, derived=False)
    sourceElement = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, targetElement=None, sourceElement=None, **kwargs):

        super().__init__(**kwargs)

        if targetElement is not None:
            self.targetElement = targetElement

        if sourceElement is not None:
            self.sourceElement = sourceElement


@abstract
class AbstractParameterSet(AbstractNamedElement):

    ownedConditions = EReference(ordered=True, unique=True,
                                 containment=True, derived=False, upper=-1)
    probability = EReference(ordered=True, unique=True, containment=True, derived=False)
    parameters = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, ownedConditions=None, probability=None, parameters=None, **kwargs):

        super().__init__(**kwargs)

        if ownedConditions:
            self.ownedConditions.extend(ownedConditions)

        if probability is not None:
            self.probability = probability

        if parameters:
            self.parameters.extend(parameters)


@abstract
class IState(AbstractNamedElement):

    referencedStates = EReference(ordered=True, unique=True,
                                  containment=False, derived=False, upper=-1)
    exploitedStates = EReference(ordered=True, unique=True,
                                 containment=False, derived=False, upper=-1)

    def __init__(self, *, referencedStates=None, exploitedStates=None, **kwargs):

        super().__init__(**kwargs)

        if referencedStates:
            self.referencedStates.extend(referencedStates)

        if exploitedStates:
            self.exploitedStates.extend(exploitedStates)


@abstract
class ValueSpecification(AbstractTypedElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class AbstractParameter(AbstractTypedElement):

    isException = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isStream = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    isOptional = EAttribute(eType=EBoolean, unique=True, derived=False, changeable=True)
    kindOfRate = EAttribute(eType=RateKind, unique=True, derived=False, changeable=True)
    effect = EAttribute(eType=ParameterEffectKind, unique=True, derived=False, changeable=True)
    rate = EReference(ordered=True, unique=True, containment=True, derived=False)
    probability = EReference(ordered=True, unique=True, containment=True, derived=False)
    parameterSet = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, isException=None, isStream=None, isOptional=None, kindOfRate=None, effect=None, rate=None, probability=None, parameterSet=None, **kwargs):

        super().__init__(**kwargs)

        if isException is not None:
            self.isException = isException

        if isStream is not None:
            self.isStream = isStream

        if isOptional is not None:
            self.isOptional = isOptional

        if kindOfRate is not None:
            self.kindOfRate = kindOfRate

        if effect is not None:
            self.effect = effect

        if rate is not None:
            self.rate = rate

        if probability is not None:
            self.probability = probability

        if parameterSet:
            self.parameterSet.extend(parameterSet)


@abstract
class AbstractInformationFlow(AbstractNamedElement, AbstractRelationship):

    realizations = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    convoyedInformations = EReference(ordered=True, unique=True,
                                      containment=False, derived=False, upper=-1)
    source = EReference(ordered=True, unique=True, containment=False, derived=False)
    target = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, realizations=None, convoyedInformations=None, source=None, target=None, **kwargs):

        super().__init__(**kwargs)

        if realizations:
            self.realizations.extend(realizations)

        if convoyedInformations:
            self.convoyedInformations.extend(convoyedInformations)

        if source is not None:
            self.source = source

        if target is not None:
            self.target = target


@abstract
class AbstractExchangeItem(AbstractType):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
