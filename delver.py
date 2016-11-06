# -*- coding: utf-8 -*-

def delve(filename):
    examples = []

    import codecs
    try:
        with codecs.open(filename, """r""", encoding="""utf-8""") as f:
        # \_ on Unix, despite 'r' mentioned, the mode will be set to 'rb'
            for line in f:
                _next = filter(lambda v: v != '\n', line)
                # \_ in text mode, this should take no effect on Windows:
                #    all end-of-lines should be altered automatically
                if _next:  # if is not empty string
                    examples.append(_next)
    except IOError:
        return [], -1

    return examples, len(examples)
