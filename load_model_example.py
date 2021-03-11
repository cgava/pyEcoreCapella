# # Issue with my own virtalenv, please, don't pay attention
# import sys
# import os
#
# sys.path.append("../pyecoregen")
# sys.path.append("../pyecore")

from pyecore.resources import ResourceSet, URI, global_registry

import pycapella

rset = ResourceSet()
resource = rset.get_resource(URI('./tests/test.empty.project/test.empty.project.melodymodeller'))
