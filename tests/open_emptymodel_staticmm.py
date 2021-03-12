# manual setting of sys.path, for testing purpose only, please setup your virtual env as desired
# import os
# import sys
#
# sys.path.append("../pyecoregen")
# sys.path.append("../pyecore")
# sys.path.append("../pycapella")

from pyecore.resources import ResourceSet, URI, global_registry

import pycapella

rset = ResourceSet()
resource = rset.get_resource(URI('test.empty.project/test.empty.project.melodymodeller'))
