from pyecore.resources import ResourceSet, URI, global_registry

import pyecore.ecore as Ecore
import pyEcoreCapella as pyEcoreCapella

rset = ResourceSet()
resource = rset.get_resource(URI('./test.empty.project/test.empty.project.melodymodeller'))