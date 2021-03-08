
#print('libraries.cross_init starting')


ModelInformation.ownedReferences.eType = LibraryReference
ModelInformation.version.eType = ModelVersion
LibraryReference.library.eType = ModelInformation
LibraryReference.version.eType = ModelVersion

#print('libraries.cross_init done')
