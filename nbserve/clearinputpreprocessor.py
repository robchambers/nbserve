"""Module containing a preprocessor that removes the inputs from code cells"""

from IPython.nbconvert.preprocessors.base import Preprocessor

class ClearInputPreprocessor(Preprocessor):
    """
    Removes the input from all code cells in a notebook.
    """

    def preprocess_cell(self, cell, resources, cell_index):
        """
        Apply a transformation on each cell. See base.py for details.
        """
        if cell.cell_type == 'code':
            if hasattr(cell, 'input'):
                del cell['input']
            #cell.outputs = []
            #cell.execution_count = None
                # collapse?
                # delete outputs[i]['prompt_number']?
                # delete cell['prompt_number']?
        return cell, resources