# -*- coding: utf-8 -*-

from lexem import no_space_conjunction
from mapping import create_map

def tokenize(example):
    """Returns a list of tokens."""
    _map = create_map(example)
    tokens = []
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
