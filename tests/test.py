from pyecore.resources import ResourceSet, URI, global_registry

import pyecore.ecore as Ecore
import pyEcoreCapella as pyEcoreCapella

for i in global_registry.keys():
    print(i)



exit(0)
rset = ResourceSet()
resource = rset.get_resource(URI('./test.empty.project/test.empty.project.melodymodeller'))