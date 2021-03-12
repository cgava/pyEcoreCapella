
#print('libraries.cross_init starting')


libraries.ModelInformation.ownedReferences.eType = libraries.LibraryReference
libraries.ModelInformation.version.eType = libraries.ModelVersion
libraries.LibraryReference.library.eType = libraries.ModelInformation
libraries.LibraryReference.version.eType = libraries.ModelVersion

#print('libraries.cross_init done')
