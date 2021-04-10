
#print('communication.cross_init starting')


information.communication.SignalInstance._staticEClass = False
information.communication.SignalInstance.eClass.eSuperTypes.extend((
    information.AbstractInstance.eClass,
))


#print('communication.cross_init done')
