# -*- coding: utf-8 -*-

#
# Core functions (?)
#

def lexem_category(character):
    """Returns Unicode Category name of the symbol."""
    # TODO: Raise an exception, if not unicode character (?)
    unicode_character = u'' + character
    #~ unicode_character = character
    # \_ Handle 'TypeError'
    import unicodedata
    category = unicodedata.category(unicode_character)
    return category

def lexem_type(character):
    """Returns the 1st symbol of Unicode Category name of the symbol."""
    return lexem_category(character)[:1]


#
# Output functions
#

def header(*strings):
    print """"""
    print """#"""
    for string in strings:
        print """#""", string
    print """#"""
    print """"""

def show(*strings, **keyworded):
    print """"""
    print """~"""
    for string in strings:
        print """~""", string
    for string in keyworded:
        pass
    print """~"""
    print """"""

def print_usage():
    print """Usage: python2 tokenizer.py [OPTIONS]
OPTIONS can be provided in any order:
    --help .........Invoke this message
    scan ...........Read filenames of the current directory and its
                    subdirectories, and tokenize them
    <int> ..........Print only first <int> strings (default is 100)
    -t .............Print lists of tokens (for the first <int> strings)\
"""

def print_usage_and_halt():
    print_usage()
    import sys
    sys.exit()
