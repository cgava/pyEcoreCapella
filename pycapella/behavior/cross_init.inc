
#print('behavior.cross_init starting')


behavior.AbstractBehavior.ownedParameterSet.eType = modellingcore.AbstractParameterSet
behavior.AbstractBehavior.ownedParameter.eType = modellingcore.AbstractParameter
behavior.AbstractTimeEvent.when.eType = behavior.TimeExpression
behavior.AbstractSignalEvent.signal.eType = behavior.AbstractSignal
behavior.TimeExpression.observations.eType = modellingcore.AbstractNamedElement
behavior.TimeExpression.expression.eType = modellingcore.ValueSpecification

#print('behavior.cross_init done')
