from IPython.nbconvert.exporters.html import HTMLExporter, TemplateExporter

from runipy.notebook_runner import NotebookRunner, NotebookError

def instrumented_notebook(nb, skip_exceptions=False):


    def iter_cells(worksheet):
        runner = None
        for cell in worksheet.cells:
            if cell.cell_type == 'code':
                try:
                    if runner is None:
                        print "Making notebook runner..."
                        runner = NotebookRunner(nb)
                        print "Made."
                    print "Running cell..."
                    runner.run_cell(cell)
                    print "Run."
                except NotebookError:
                    if not skip_exceptions:
                        raise
            yield cell

    nbc = nb.copy()
    nbc['worksheets'] = [iter_cells(ws) for ws in nb['worksheets']]
    return nbc

    # This is an ugly little bit to deal with a sporadic
    #  'queue empty' bug in iPython that only seems to
    #  happen on the integration servers...
    #  see https://github.com/paulgb/runipy/issues/36
    # N_RUN_RETRIES = 4
    # from Queue import Empty
    # for i in range(N_RUN_RETRIES):
    #     try:
    #         runner = NotebookRunner(nb['content'])
    #         print "Running notebook"
    #         runner.run_notebook()
    #         break
    #     except Empty as e:
    #         if i >= (N_RUN_RETRIES - 1):
    #             raise

class StreamingRunningHTMLExporter(HTMLExporter):

    def from_notebook_node(self, nb, resources=None, **kw):
        """
        Convert a notebook from a notebook node instance.

        Parameters
        ----------
        nb : :class:`~{nbformat_mod}.nbbase.NotebookNode`
          Notebook node
        resources : dict
          Additional resources that can be accessed read/write by
          preprocessors and filters.
        """
        nb_copy, resources = super(TemplateExporter, self).from_notebook_node(nb, resources, **kw)
        resources.setdefault('raw_mimetypes', self.raw_mimetypes)

        inb = instrumented_notebook(nb_copy)


        self._load_template()

        # assert resources is None

        if self.template is not None:
            output = self.template.stream(nb=inb, resources=resources)
        else:
            raise IOError('template file "%s" could not be found' % self.template_file)
        return output, resources
