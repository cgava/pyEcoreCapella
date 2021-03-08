from pyecore.resources import ResourceSet
from pyecoregen.ecore import EcoreGenerator

rset = ResourceSet()
uri_mapper = rset.uri_mapper
uri_mapper['platform:/plugin/org.polarsys.kitalpha.emde/model'] = '../../org.polarsys.kitalpha.emde/model'

for mm in ('../mm/org.polarsys.capella.common.data.def/model/Behavior.ecore',
            '../mm/org.polarsys.capella.common.data.def/model/ModellingCore.ecore',
            '../mm/org.polarsys.capella.common.data.def/model/Activity.ecore',
            '../mm/org.polarsys.kitalpha.emde/model/eMDE.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/CapellaCommon.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/CapellaCore.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/CapellaModeller.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/CompositeStructure.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/ContextArchitecture.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/EPBSArchitecture.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/FunctionalAnalysis.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/Information.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/Interaction.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/LogicalArchitecture.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/OperationalAnalysis.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/PhysicalArchitecture.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/Requirement.ecore',
            '../mm/org.polarsys.capella.core.data.def/model/SharedModel.ecore',

            '../mm/org.polarsys.capella.common.libraries.gen/model/libraries.ecore'
           ):
    print("generating ",mm)
    mm_root = rset.get_resource(mm).contents[0]
    EcoreGenerator(auto_register_package=True).generate(mm_root, outfolder='../pyEcoreCapella')

basepath="../pyEcoreCapella/"
cat =  basepath + "__init__.inc "
cat += basepath + "activity/cross_init.inc "
cat += basepath + "behavior/cross_init.inc "
cat += basepath + "capellacommon/cross_init.inc "
cat += basepath + "capellacore/cross_init.inc "
cat += basepath + "capellamodeller/cross_init.inc "
cat += basepath + "cs/cross_init.inc "
cat += basepath + "ctx/cross_init.inc "
cat += basepath + "emde/cross_init.inc "
cat += basepath + "epbs/cross_init.inc "
cat += basepath + "fa/cross_init.inc "
cat += basepath + "information/communication/cross_init.inc "
cat += basepath + "information/datatype/cross_init.inc "
cat += basepath + "information/datavalue/cross_init.inc "
cat += basepath + "information/cross_init.inc "
cat += basepath + "interaction/cross_init.inc "
cat += basepath + "la/cross_init.inc "
cat += basepath + "libraries/cross_init.inc "
cat += basepath + "modellingcore/cross_init.inc "
cat += basepath + "oa/cross_init.inc "
cat += basepath + "pa/cross_init.inc "
cat += basepath + "pa/deployment/cross_init.inc "
cat += basepath + "requirement/cross_init.inc "
cat += basepath + "sharedmodel/cross_init.inc "


import os
try:
    os.system("rm -f "+basepath+"__init__.py")
except:
    print('rm -f __init__.py failed')
os.system("cat  " +cat+ ">" + basepath + "__init__.py")
os.system("for i in `find " + basepath + " -name '*.py'` ; do sed -i -re 's/#print/print/' $i ; done")