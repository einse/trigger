# -*- coding: utf-8 -*-


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


def create_map(example):
    """Returns a string filled by lexem categories' first symbols."""
    _map = ''
    for position, symbol in enumerate(example):
        _map = _map + lexem_type(symbol)
    return _map


def tokenize(example):
    """Returns a list of tokens."""
    _map = create_map(example)
    tokens = []

    def no_space_conjunction(tag1, tag2):
        """If two tags represent one number and one letter."""
        if tag1 == 'L' and tag2 == 'N':
            return True
        elif tag1 == 'N' and tag2 == 'L':
            return True
        else:
            return False

    stack = []
    previous_tag = ''

    for position, symbol in enumerate(example):
        tag = _map[position]
        #~ print position, symbol, tag, previous_tag
        if tag == 'L' or tag == 'N':
            if no_space_conjunction(tag, previous_tag):
                if stack:
                    tokens.append(''.join(stack))
                    del stack[:]
                else:
                    pass  # should be never reached
            stack.append(symbol)
        else:
            if stack:
                tokens.append(''.join(stack))
                del stack[:]
            tokens.append(symbol)
        previous_tag = tag
    else:
        if stack:
            tokens.append(''.join(stack))
            del stack[:]

    return tokens


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
