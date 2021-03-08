from pyecore.resources import ResourceSet
from pyecoregen.ecore import EcoreGenerator

rset = ResourceSet()
uri_mapper = rset.uri_mapper
uri_mapper['platform:/plugin/org.polarsys.kitalpha.emde/model'] = '../../org.polarsys.kitalpha.emde/model'

for mm in ('../mm/org.polarsys.capella.common.data.def/model/Behavior.ecore',
            '../mm/org.polarsys.capella.common.data.def/model/ModellingCore.ecore',
            '../mm/org.polarsys.capella.common.data.def/model/Activity.ecore',
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

            '../mm/org.polarsys.capella.common.libraries.gen/model/libraries.ecore',
            '../mm/org.polarsys.kitalpha.emde/model/eMDE.ecore',
            ):
    print("generating ",mm)
    mm_root = rset.get_resource(mm).contents[0]
    EcoreGenerator().generate(mm_root, outfolder='../pyEcoreCapella')
