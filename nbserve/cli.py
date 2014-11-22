#!/usr/bin/env python
"""
Command Line Interface.
"""

import nbserve
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog=nbserve.__progname__,
        description=nbserve.__description__,
        version='%s %s' % (nbserve.__progname__, nbserve.__version__))

    parser.add_argument("working_directory", nargs='?', default=".", type=str)
    parser.add_argument("-p", dest="port", action="store", default=None, type=int)
    parser.add_argument("--no-debug", dest="debug", action="store_false", default=True)

    args = parser.parse_args()


    nbserve.set_working_directory(args.working_directory)

    print "Running. For usage info and options, type %s -h." % nbserve.__progname__
    print "Press Ctrl-C or similar to stop."

    nbserve.flask_app.run(debug=args.debug, port=args.port)

if __name__ == "__main__":
    main()
