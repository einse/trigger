# -*- coding: utf-8 -*-

def search_for_duplicates(examples):
    """If there are any duplicates in given strings list.
Returns count of duplicate names & dictionary containing numbers of
repeating for every duplicate name."""
    nur = {}  # names' uniqueness rate
    for name in examples:
        if name in nur:
            nur[name] = nur[name] + 1
        else:
            nur[name] = 1
    duplicates_count = 0
    duplicates_dictionary = {}
    for name in nur.keys():
        if nur[name] > 1:
            duplicates_count = duplicates_count + 1
            duplicates_dictionary[name] = nur[name]
    return duplicates_count, duplicates_dictionary
