
#print('sharedmodel.cross_init starting')


SharedPkg.ownedDataPkg.eType = DataPkg
SharedPkg.ownedGenericPkg.eType = GenericPkg
GenericPkg.subGenericPkgs.eType = GenericPkg
GenericPkg.capellaElements.eType = CapellaElement

#print('sharedmodel.cross_init done')
