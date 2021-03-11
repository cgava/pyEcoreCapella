print('deployment.deployment loading')
"""Definition of meta model 'deployment'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from capellacore import CapellaElement, NamedElement, Structure
from cs import AbstractDeploymentLink, DeployableElement, DeploymentTarget


name = 'deployment'
nsURI = 'http://www.polarsys.org/capella/core/pa/deployment/1.4.0'
nsPrefix = 'org.polarsys.capella.core.data.pa.deployment'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class AbstractPhysicalInstance(CapellaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class ConnectionInstance(AbstractPhysicalInstance):

    connectionEnds = EReference(ordered=True, unique=True,
                                containment=False, derived=False, upper=-1)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, connectionEnds=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if connectionEnds:
            self.connectionEnds.extend(connectionEnds)

        if type is not None:
            self.type = type


class PortInstance(AbstractPhysicalInstance):

    connections = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    _component = EReference(ordered=True, unique=True, containment=False,
                            derived=True, name='component', transient=True)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    @property
    def component(self):
        raise NotImplementedError('Missing implementation for component')

    def __init__(self, *, connections=None, component=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if connections:
            self.connections.extend(connections)

        if component is not None:
            self.component = component

        if type is not None:
            self.type = type


class DeploymentConfiguration(NamedElement):

    ownedDeploymentLinks = EReference(ordered=True, unique=True,
                                      containment=True, derived=False, upper=-1)
    ownedPhysicalInstances = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedDeploymentLinks=None, ownedPhysicalInstances=None, **kwargs):

        super().__init__(**kwargs)

        if ownedDeploymentLinks:
            self.ownedDeploymentLinks.extend(ownedDeploymentLinks)

        if ownedPhysicalInstances:
            self.ownedPhysicalInstances.extend(ownedPhysicalInstances)


class InstanceDeploymentLink(AbstractDeploymentLink):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PartDeploymentLink(AbstractDeploymentLink):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class TypeDeploymentLink(AbstractDeploymentLink):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DeploymentAspect(Structure):

    ownedConfigurations = EReference(ordered=True, unique=True,
                                     containment=True, derived=False, upper=-1)
    ownedDeploymentAspects = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ownedConfigurations=None, ownedDeploymentAspects=None, **kwargs):

        super().__init__(**kwargs)

        if ownedConfigurations:
            self.ownedConfigurations.extend(ownedConfigurations)

        if ownedDeploymentAspects:
            self.ownedDeploymentAspects.extend(ownedDeploymentAspects)


class DerivedPortinstances(EDerivedCollection):
    pass


class ComponentInstance(AbstractPhysicalInstance, DeployableElement, DeploymentTarget):

    portInstances = EReference(ordered=True, unique=True, containment=False,
                               derived=True, upper=-1, transient=True, derived_class=DerivedPortinstances)
    ownedAbstractPhysicalInstances = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    ownedInstanceDeploymentLinks = EReference(
        ordered=True, unique=True, containment=True, derived=False, upper=-1)
    type = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, portInstances=None, ownedAbstractPhysicalInstances=None, ownedInstanceDeploymentLinks=None, type=None, **kwargs):

        super().__init__(**kwargs)

        if portInstances:
            self.portInstances.extend(portInstances)

        if ownedAbstractPhysicalInstances:
            self.ownedAbstractPhysicalInstances.extend(ownedAbstractPhysicalInstances)

        if ownedInstanceDeploymentLinks:
            self.ownedInstanceDeploymentLinks.extend(ownedInstanceDeploymentLinks)

        if type is not None:
            self.type = type

print('deployment.deployment loaded')
