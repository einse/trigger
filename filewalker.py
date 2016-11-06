# -*- coding: utf-8 -*-

from tokenizer import tokenize

def scan(path, favorite_tokens = set(), forbidden_tokens = set()):
    all_names = []
    all_tokens = []

    import os
    for root, directories, filenames in os.walk(path):
    # \_ note that if 'target_folder' is invalid no error will be thrown
        for filename in filenames:
            example = filename
            current_tokens = tokenize(example)

            allow_adding = False
            for token in current_tokens:
                for favorite in favorite_tokens:
                    if favorite == token:
                        allow_adding = True
                for forbidden in forbidden_tokens:
                    if forbidden == token:
                        allow_adding = False

            if allow_adding:
                all_names.append(example)
                all_tokens.append(current_tokens)
            else:
                continue

    return all_names, all_tokens
