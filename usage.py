# -*- coding: utf-8 -*-

def print_usage():
    print """Usage: python2 tokenizer.py [OPTIONS]
OPTIONS can be provided in any order:
    --help .........Invoke this message
    scan ...........Read filenames of the current directory and its
                    subdirectories, and tokenize them
    <int> ..........Print only first <int> strings (default is 20)
    -t .............Print lists of tokens (for the first <int> strings)\
"""

def print_usage_and_halt():
    print_usage()
    import sys
    sys.exit()
