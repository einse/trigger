# -*- coding: utf-8 -*-

from tokenizer import tokenize

def delve(filename):
    all_names = []
    all_tokens = []
    import codecs
    try:
        with codecs.open(filename, """r""", encoding="""utf-8""") as f:
        # \_ on Unix, despite 'r' mentioned, the mode will be set to 'rb'
            for line in f:
                current_name = filter(lambda v: v != '\n', line)
                # \_ in text mode, this should take no effect on Windows:
                #    all end-of-lines should be altered automatically
                if current_name:  # if is not empty string
                    current_tokens = tokenize(current_name)
                    all_names.append(current_name)
                    all_tokens.append(current_tokens)
    except IOError:
        return [], -1, [], -1
    return all_names, len(all_names), all_tokens, len(all_tokens)
