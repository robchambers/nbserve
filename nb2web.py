

"""
1) Convert a notebook --> HTML, write it out, confirm.
2) Do it w/out runipy
3) Do it as a URL.
2)
"""

from runipy.notebook_runner import NotebookRunner
from IPython.nbconvert.exporters.html import HTMLExporter
from IPython.nbformat.current import read

def print_nb(nbpath):

    notebook = read(open(nbpath), 'json')
    r = NotebookRunner(notebook)
    r.run_notebook()

    exporter = HTMLExporter()
    from IPython.nbformat.current import write
    write(r.nb, open("MyOtherNotebook.ipynb", 'w'), 'json')
    exporter = HTMLExporter(
        #config=Config({'HTMLExporter':{'default_template':args.template}})
        )

    output, resources = exporter.from_notebook_node(r.nb)
    with open('out.html', 'w') as f:
        f.write(output)
    print "Wrote Notebook."


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="nb2web")
    parser.add_argument('nbpath')
    args = parser.parse_args()
    print_nb(args.nbpath)
