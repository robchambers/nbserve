"""HTML Exporter class"""

#-----------------------------------------------------------------------------
# Copyright (c) 2013, the IPython Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

import os.path

from IPython.nbconvert import preprocessors
from IPython.config import Config
from IPython.nbconvert.exporters.html import HTMLExporter
from IPython.utils.traitlets import MetaHasTraits, Unicode, List, Dict, Any

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------
template_dir = os.path.join(os.path.split(__file__)[0],'templates')

class NBExporter(HTMLExporter):
    template_path = List(['.', template_dir], config=True)

    def _template_file_default(self):
        return 'nbserve'

