# -*- coding: utf-8 -*-

from usage import print_usage, print_usage_and_halt
from delver import delve
from filewalker import scan
from rating import print_rating


# Set up variables

target_folder = u"""./"""
favorite_tokens = set()
forbidden_tokens = set()
blacklist = set()

limit_for_print = 5

allow_filewalking = False
allow_txt_file = True
allow_print_tokens = False

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
            allow_print_tokens = True
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
for i, examples in enumerate(examples):
    if i >= limit_for_print:
        break
    i = i + 1
    print i, examples
print ''

# Print tokens lists
if allow_print_tokens:
    for i, _list in enumerate(tokens_lists):
        if i >= limit_for_print:
            break
        i = i + 1
        print """Tokens list no.""", i
        for j, token in enumerate(_list):
            j = j + 1
            print j, token
        print '\n'

# Print counts
print """count:""", count, """\ncount2:""", count2

# Print rating
allow_rating = raw_input("""Print words rating? [Y/n]: """);
if allow_rating == '':
    allow_rating = 'Y'
if allow_rating == 'Y' or allow_rating == 'y':
    count, count2, count3 = print_rating(tokens_lists, blacklist)
    print """all:""", count, """\nreal:""", count2,\
                               """\nwhite:""", count3
else:
    pass
