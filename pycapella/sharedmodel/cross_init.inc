
#print('sharedmodel.cross_init starting')


sharedmodel.SharedPkg.ownedDataPkg.eType = information.DataPkg
sharedmodel.SharedPkg.ownedGenericPkg.eType = sharedmodel.GenericPkg
sharedmodel.GenericPkg.subGenericPkgs.eType = sharedmodel.GenericPkg
sharedmodel.GenericPkg.capellaElements.eType = capellacore.CapellaElement

#print('sharedmodel.cross_init done')
