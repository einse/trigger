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

def no_space_conjunction(tag1, tag2):
    """If two tags represent one number and one letter."""
    if tag1 == 'L' and tag2 == 'N':
        return True
    elif tag1 == 'N' and tag2 == 'L':
        return True
    else:
        return False
