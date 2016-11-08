# -*- coding: utf-8 -*-

def clear_output_file(filename):
    import codecs
    with codecs.open(filename, """w""", encoding="utf-8") as f:
        f.write("""""")

def output(allow_writing_to_files, filename, *strings):
    for string in strings:
        print string,
    print """"""
    if allow_writing_to_files:
        import codecs
        with codecs.open(filename, """a""", encoding="utf-8") as f:
            for string in strings:
                f.write(unicode(string))
                f.write(""" """)
            f.write("""\n""")
