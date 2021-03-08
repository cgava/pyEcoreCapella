from pyecore.resources import ResourceSet, URI, global_registry

import pyecore.ecore as Ecore
import pyEcoreCapella.emde as eMDE
import pyEcoreCapella.modellingcore as ModellingCore
import pyEcoreCapella.behavior as Behavior
import pyEcoreCapella.activity as Activity
import pyEcoreCapella.capellacommon as CapellaCommon
import pyEcoreCapella.capellacore as CapellaCore
import pyEcoreCapella.information as Information
import pyEcoreCapella.interaction as Interaction
import pyEcoreCapella.cs as CS
import pyEcoreCapella.ctx as CTX
import pyEcoreCapella.epbs as EPBS
import pyEcoreCapella.fa as FA
import pyEcoreCapella.la as LA
import pyEcoreCapella.oa as OA
import pyEcoreCapella.pa as PA
import pyEcoreCapella.requirement as Requirement
import pyEcoreCapella.sharedmodel as SharedModel
import pyEcoreCapella.capellamodeller as CapellaModeller
import pyEcoreCapella.libraries as Libraries

global_registry[Ecore.nsURI] = Ecore
global_registry[Activity.nsURI] = Activity
global_registry[CapellaCommon.nsURI] = CapellaCommon
global_registry[CapellaCore.nsURI] = CapellaCore
global_registry[Information.nsURI] = Information
global_registry[Interaction.nsURI] = Interaction
global_registry[CS.nsURI] = CS
global_registry[CTX.nsURI] = CTX
global_registry[EPBS.nsURI] = EPBS
global_registry[FA.nsURI] = FA
global_registry[LA.nsURI] = LA
global_registry[OA.nsURI] = OA
global_registry[PA.nsURI] = PA
global_registry[Requirement.nsURI] = Requirement
global_registry[SharedModel.nsURI] = SharedModel
global_registry[CapellaModeller.nsURI] = CapellaModeller
global_registry[eMDE.nsURI] = eMDE
global_registry[Libraries.nsURI] = Libraries


rset = ResourceSet()
resource = rset.get_resource(URI('./test.empty.project/test.empty.project.melodymodeller'))