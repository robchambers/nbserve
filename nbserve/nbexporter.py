import os.path
try:
    from jupyter.nbconvert.exporters.html import HTMLExporter
except ImportError:
    from nbconvert import HTMLExporter

try:
    from jupyter.utils.traitlets import List
except ImportError:
    from traitlets import List

template_dir = os.path.join(os.path.split(__file__)[0],'templates')

class NBExporter(HTMLExporter):
    template_path = List(['.', template_dir], config=True)

    def _template_file_default(self):
        return 'nbserve'

