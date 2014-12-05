#!/usr/bin/env python
"""
Command Line Interface.
"""
import nbserve
import argparse

def config_from_args(args=None):
    parser = argparse.ArgumentParser(
        prog=nbserve.__progname__,
        description=nbserve.__description__,
        version='%s %s' % (nbserve.__progname__, nbserve.__version__))

    parser.add_argument("working_directory", nargs='?', default=".", type=str)
    parser.add_argument("-t", dest="template", choices=['strip-input', 'collapse-input', 'full'], type=str,
                        help="Whether to strip, collapse, or show input code cells.")
    parser.add_argument("-p", dest="port", action="store", default=None, type=int)
    parser.add_argument("-r", dest="run", action="store_true",
                        help="Whether to run scripts each time they're loaded.")
    parser.add_argument("-d", dest="debug", help="Debug mode", action="store_true", default=False)


    config = parser.parse_args(args)
    return {k:v for k,v in config.__dict__.iteritems() if v is not None}

def main():
    nbserve.update_config(config_from_args())
    print "Running. For usage info and options, type %s -h." % nbserve.__progname__
    print "Press Ctrl-C or similar to stop."
    nbserve.flask_app.run(debug=nbserve.flask_app.base_config['debug'],
                          port=nbserve.flask_app.base_config['port'])

if __name__ == "__main__":
    main()
