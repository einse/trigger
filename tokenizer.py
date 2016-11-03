# -*- coding: utf-8 -*-

#
# Output functions
#

def header(*strings):
    print ''
    print '#'
    for string in strings:
        print '#', string
    print '#'
    print ''

def show(*strings, **keyworded):
    print ''
    print '~'
    for string in strings:
        print '~', string
    for string in keyworded:
        pass  # edit
    print '~'
    print ''


#
# Program setting
#

#~ favorite_tokens = set([u'Снимок', u'scrot', u'мкрк'])
favorite_tokens = set([u'диз', u'мкрк'])
forbidden_tokens = set([u'Снимок'])
filter_input_strings = True

limit_for_print = 100

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


#
# Create a list for strings
#
examples = []


#
# Read names of files
#

if allow_filewalking:
    names = []
    import os
    # TODO: Raise an exception, if directory doesn't exist.
    # TODO: Only scan the current directory(?)
    images_folder = os.getenv("""HOME""") + u"""/Изображения"""
    for root, directories, filenames in os.walk(images_folder):
        for filename in filenames:
            names.append(filename)
    for i, v in enumerate(names):
        if filter_input_strings:
            found = False
            for favorite in favorite_tokens:
                if v.find(favorite) == -1:
                    continue
                else:
                    found = True
            if not found:
                continue
            found = False
            for forbidden in forbidden_tokens:
                if v.find(forbidden) == -1:
                    continue
                else:
                    found = True
            if found:
                continue
        examples.append(v)
    show("""Count of read filenames:""", len(names))
    show("""Count of input strings for tokenizer:""", len(examples))
    del names[:]  # Is it necessary? Wouldn't GC erase it by himself?


#
# Read strings from a simple text file (.txt)
#

if allow_txt_file:
    import codecs
    # TODO: Raise an exception, if file doesn't exist;
    # print message: "The file 'examples.txt' is not found."
    f = codecs.open('examples.txt', 'r', encoding='utf-8')
    # \_ despite 'r' mentioned, the mode will be set to 'rb' (on Unix)
    for line in f:
        new_example = filter(lambda v: v != '\n', line)
        # \_ in text mode, this should take no effect on Windows:
        #    all end-of-lines should be altered automatically
        if new_example:
            examples.append(new_example)
    f.close()
# To learn more on reading files in Python 2:
# https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files


#
# Create a lexem category map for every input string
#
maps = []
examples = sorted(examples, reverse=True)

def lexem_category(unicode_character):
    """Returns Unicode Category name of the symbol."""
    import unicodedata
    return unicodedata.category(unicode_character)

def lexem_type(unicode_character):
    """Returns the 1st symbol of Unicode Category name of the symbol."""
    return lexem_category(unicode_character)[:1]

header("""Create a lexem category map for every input string""")
iterations_count = 0
for number, sentence in enumerate(examples):
    iterations_count = iterations_count + 1
    number = number + 1
    number_length = len(str(number))
    sentence_map = ''
    for position, symbol in enumerate(sentence):
        sentence_map = sentence_map + lexem_type(symbol)
    maps.append(sentence_map)
    if iterations_count <= limit_for_print:
        print number, sentence
        print ' ' * number_length, sentence_map


#
# Print lexem category maps
#

#~ header("""Print lexem category maps""")
#~ iterations_count = 0
#~ for number, _map in enumerate(maps):
    #~ iterations_count = iterations_count + 1
    #~ if iterations_count > limit_for_print:
        #~ break
    #~ number = number + 1
    #~ print number, _map


#
# Create a portion: lists of tokens (by one list per every input sentence)
#
portion = []

def no_space_conjunction(tag1, tag2):
    """If two tags represent one number and one letter."""
    if tag1 == 'L' and tag2 == 'N':
        return True
    elif tag1 == 'N' and tag2 == 'L':
        return True
    else:
        return False

for example_number, sentence in enumerate(examples):
    tokens = []
    stack = []
    previous_tag = ''
    for position, symbol in enumerate(sentence):
        tag = maps[example_number][position]
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
    portion.append(tokens)


#
# Print first N tokens of the current input portion
# (where N is limit_for_print)
#

if allow_print_tokens:
    iterations_count = 0
    for number, sentence in enumerate(portion):
        iterations_count = iterations_count + 1
        if iterations_count > limit_for_print:
            break
        number = number + 1
        header('=' * 72, """Tokens list no.:""", number)
        for seat, token in enumerate(sentence):
            print seat, token


#
# Gather tokens into statistics dictionary named words
#
words = {}

for number, sentence in enumerate(portion):
    for seat, token in enumerate(sentence):
        if token in words:
            words[token] = words[token] + 1
        else:
            words[token] = 0


#
# Print words rating
# (top:
limit_for_rating_output = 50

asterisks = """*""" * 72
header(asterisks,
       """Top""", limit_for_rating_output, """words""",
       asterisks)

nominees = sorted(words.keys(),
                  key=lambda v: words[v],
                  reverse=True)[:limit_for_rating_output*2]
real_words = filter(lambda v: lexem_type(v[0]) == 'L', nominees)
black_list = set([u'png', u'scrot', u'x', u'Снимок', u'экрана', u'от'])
white_list = filter(lambda v: v not in black_list, real_words)

print u'{:5} {:5} {}'.format('Place', 'Freq.', 'Token')
for place, token in enumerate(white_list):
    if place >= limit_for_rating_output:
        break
    print u'{:5} {:5} {}'.format(place+1, words[token], token)

show("""Tokens Index volume:""", len(words.keys()))
