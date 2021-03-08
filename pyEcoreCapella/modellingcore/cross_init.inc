
#print('modellingcore.cross_init starting')


ModelElement.constraints.eType = AbstractConstraint
ModelElement.ownedConstraints.eType = AbstractConstraint
ModelElement.ownedMigratedElements.eType = ModelElement
InformationsExchanger.incomingInformationFlows.eType = AbstractInformationFlow
InformationsExchanger.outgoingInformationFlows.eType = AbstractInformationFlow
InformationsExchanger.informationFlows.eType = AbstractInformationFlow
TraceableElement.incomingTraces.eType = AbstractTrace
TraceableElement.outgoingTraces.eType = AbstractTrace
AbstractType.abstractTypedElements.eType = AbstractTypedElement
AbstractTypedElement.abstractType.eType = AbstractType
AbstractTrace.targetElement.eType = TraceableElement
AbstractTrace.sourceElement.eType = TraceableElement
AbstractConstraint.constrainedElements.eType = ModelElement
AbstractConstraint.ownedSpecification.eType = ValueSpecification
AbstractConstraint._context.eType = ModelElement
AbstractParameter.rate.eType = ValueSpecification
AbstractParameter.probability.eType = ValueSpecification
AbstractParameterSet.ownedConditions.eType = AbstractConstraint
AbstractParameterSet.probability.eType = ValueSpecification
AbstractInformationFlow.convoyedInformations.eType = AbstractExchangeItem
AbstractInformationFlow.source.eType = InformationsExchanger
AbstractInformationFlow.target.eType = InformationsExchanger
IState.referencedStates.eType = IState
IState.exploitedStates.eType = IState
AbstractRelationship.realizedFlow.eType = AbstractInformationFlow
AbstractParameter.parameterSet.eType = AbstractParameterSet
AbstractParameterSet.parameters.eType = AbstractParameter
AbstractParameterSet.parameters.eOpposite = AbstractParameter.parameterSet
AbstractInformationFlow.realizations.eType = AbstractRelationship
AbstractInformationFlow.realizations.eOpposite = AbstractRelationship.realizedFlow

#print('modellingcore.cross_init done')
