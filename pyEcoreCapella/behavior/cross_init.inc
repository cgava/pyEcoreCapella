
#print('behavior.cross_init starting')


AbstractBehavior.ownedParameterSet.eType = AbstractParameterSet
AbstractBehavior.ownedParameter.eType = AbstractParameter
AbstractTimeEvent.when.eType = TimeExpression
AbstractSignalEvent.signal.eType = AbstractSignal
TimeExpression.observations.eType = AbstractNamedElement
TimeExpression.expression.eType = ValueSpecification

#print('behavior.cross_init done')
