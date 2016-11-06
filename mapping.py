# -*- coding: utf-8 -*-

from lexem import lexem_type

def create_map(example):
    """Returns a string filled by lexem categories' first symbols."""
    _map = ''
    for position, symbol in enumerate(example):
        _map = _map + lexem_type(symbol)
    return _map
