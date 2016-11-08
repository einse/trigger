# -*- coding: utf-8 -*-

from usage import print_usage, print_usage_and_halt
from delver import delve
from filewalker import scan
from rating import print_rating
from duplicates import search_for_duplicates
from output import output, clear_output_file


# Set up variables

target_folder = u"""./"""
trgr_output_file_name = """trgr_output.txt"""
t = trgr_output_file_name

favorite_tokens = set()
forbidden_tokens = set()
blacklist = set()

limit_for_print = 5  # TODO: when changed, update the usage info

a = False  # allow_writing_to_files
allow_filewalking = False
allow_txt_file = True
allow_printing_tokens = False

if __name__ == """__main__""":
    import sys
    arguments = sys.argv
    arguments_length = len(arguments)
    for argument in arguments:
        if argument.isdigit():
            limit_for_print = int(argument)
        if argument == """scan""":
            allow_filewalking, allow_txt_file = \
                allow_txt_file, allow_filewalking
        if argument == """-t""":
            allow_printing_tokens = True
        if argument == """-o""":
            a = True
        if argument == """delve""":
            pass
        if argument == """--images""":
            import os
            target_folder = os.getenv("""HOME""") + u"""/Изображения"""
        if argument == """--filter""":
            favorite_tokens = set([u'диз', u'мкрк', u'фэт'])
            blacklist = set([u'png', u'scrot', u'x',
                  u'Снимок', u'экрана', u'от'])
        if argument == """--help""":
            print_usage_and_halt()


# Create a list for strings
examples = []

# Create a list for tokens lists
tokens_lists = []

# Erase output file
if a:
    clear_output_file(t)


# Read strings from a simple text file (.txt)
if allow_txt_file:
    read, count, lists, count2 = delve("""trgr_examples.txt""")
    if count != -1:
        examples.extend(read)
        tokens_lists.extend(lists)
    else:
        print_usage_and_halt()

# Scan file system
if allow_filewalking:
    read, count, lists, count2 =\
            scan(target_folder, favorite_tokens, forbidden_tokens)
    if count != -1:
        examples.extend(read)
        tokens_lists.extend(lists)

# Sort examples
#~ examples = sorted(examples, reverse=True)
# TODO: Learn to sort 'tokens_lists'

# Print examples
for i, example in enumerate(examples):
    if i >= limit_for_print:
        break
    i = i + 1
    output(a, t, i, example)
output(a, t, """""")

# Print tokens lists
if allow_printing_tokens:
    for i, _list in enumerate(tokens_lists):
        if i >= limit_for_print:
            break
        i = i + 1
        output(a, t, """Tokens list no.""", i)
        for j, token in enumerate(_list):
            j = j + 1
            output(j, token)
        output(a, t, """\n""")

# Print counts
output(a, t, """count:""", count, """\ncount2:""", count2)

# Print rating
allow_rating = raw_input("""Print words rating? [Y/n]: """);
if allow_rating == """""":
    allow_rating = """Y"""
if allow_rating == """Y""" or allow_rating == """y""":
    count, count2, count3 = print_rating(a, t, tokens_lists, blacklist)
    output(a, t, """all:""", count, """\nreal:""", count2,\
                               """\nwhite:""", count3)
else:
    pass

# Search for duplicate names
duplicates_count, duplicates_rates = search_for_duplicates(examples)
for i, name in enumerate(duplicates_rates):
    output(a, t, u"""{} {}x: {}""".format(i+1, duplicates_rates[name], name))
output(a, t, """Duplicates count:""", duplicates_count)
