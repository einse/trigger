# -*- coding: utf-8 -*-

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

examples = [];
examples.append(u'2016-10-25-202044_1024x600_scrot-мкрк-редактура-лишняя-запятая-паттерн-например-теория-близости.png')
examples.append(u'2016-10-26-085757_1024x600_scrot-мкрк-диз-бонтекст-типографика-знак-охраны-авторского-права-2.png')
examples.append(u'Снимок экрана от 2016-10-26 15-16-54-диз-навигация-ойкумена--железная-скоба-с-пупырышками-2.png')
examples.append(u'2016-10-26-170129_1024x600_scrot-мкрк-редактура-паттерн-предикативный-ввод--предиктивный-ввод.png')
examples.append(u'2016-10-26-170421_1024x600_scrot-мкрк-редактура-паттерн-когда-ограничиваем-число-работающих-приложений--когда-ограничивается.png')
examples.append(u'2016-10-26-171005_1024x600_scrot-диз-респаэр--гугл-кип.png')
examples.append(u'2016-10-26-171011_1024x600_scrot-мкрк-паттерн-интернет-дефис-приложения.png')
examples.append(u'2016-10-26-171720_1024x600_scrot-мкрк-вопрос-паттерн-до-отглагольное-существительное-запятая.png')
examples.append(u'2016-10-26-172559_1024x600_scrot-диз-респаэр--гугл-кип.png')
examples.append(u'2016-10-26-172902_1024x600_scrot-диз-респаэр--эс-планнер.png')
examples.append(u'2016-10-26-172905_1024x600_scrot-диз-респаэр--эс-планнер.png')
examples.append(u'2016-10-26-173119_1024x600_scrot-диз-респаэр--эс-планнер.png')
examples.append(u'2016-10-26-173122_1024x600_scrot-диз-респаэр--эс-планнер.png')
examples.append(u'2016-10-26-173124_1024x600_scrot-диз-респаэр--эс-планнер.png')
examples.append(u'2016-10-26-173440_1024x600_scrot-мкрк-редактура.png')
examples.append(u'Снимок экрана от 2016-10-26 16-03-18.png')
examples.append(u'Снимок экрана от 2016-10-25 15-09-46-диз-веб-ласт-фм--независимая-сортировка-независимая-очерёдность.png')
examples.append(u'Снимок экрана от 2016-10-26 17-57-45-диз-веб-ластфм-порядок-сортировки-очерёдность.png')
examples.append(u'2016-10-26-194815_1024x600_scrot-мкрк-термин-поверхностная-(shallow)-обработка-единиц-естественного-языка.png')
examples.append(u'2016-10-26-195157_1024x600_scrot-мкрк-термин-глубокая-обработка-единиц-естественного-языка.png')
examples.append(u'Снимок экрана от 2016-10-26 11-22-19-диз-рэа-камера-j7-2016.png')
examples.append(u'2016-10-26-201955_1024x600_scrot-мкрк-вопрос-редактура-паттерн-английский-язык-nns-vbps.png')
examples.append(u'2016-10-26-202209_1024x600_scrot-мкрк-паттерн-в-nn-запятая.png')
examples.append(u'2016-10-27-075228_1024x600_scrot-мкрк-паттерн-shallow-copy-английский-язык.png')
examples.append(u'2016-10-27-082142_1024x600_scrot-мкрк-вопрос-паттерн-запятая-как-так-запятая.png')
examples.append(u'Снимок экрана от 2016-09-26 12-11-19-мкрк-редактура-паттерн-напоследок-обособление.png')
examples.append(u'Снимок экрана от 2016-10-26 18-04-11-мкрк-вопрос-паттерн-может-быть-даже-пропуск-обособления.png')
examples.append(u'2016-10-27-083338_1024x600_scrot-мкрк-термин-зоны-сфера-дарт-ангуляр2.png')
examples.append(u'2016-10-27-084250_1024x600_scrot-диз-веб-хабр-1.png')
examples.append(u'Снимок экрана от 2016-10-27 08-43-25-диз-веб-хабр-2-ссылки-отступы.png')
examples.append(u'Снимок экрана от 2016-10-27 09-08-44-мкрк-редактура--эверхёд--паттерн-как-запятая.png')
examples.append(u'Снимок экрана от 2016-10-27 09-08-44-мкрк-редактура--эверхёд-альманах-веб-бонтекст--паттерн-как-запятая (копия).png')
examples.append(u'2016-10-27-083149_1024x600_scrot-диз-lxde-индикатор-сети.png')
examples.append(u'2016-10-27-091337_1024x600_scrot-диз-lxde-индикатор-сигнала.png')
examples.append(u'2016-10-27-091349_1024x600_scrot-диз-lxde-индикатор-сигнала.png')
examples.append(u'2016-10-27-090408_1024x600_scrot-диз-веб-дарт--ливицея.png')
examples.append(u'2016-10-27-092103_1024x600_scrot-диз-веб-дарт-поиск-length.png')
examples.append(u'2016-10-27-092343_1024x600_scrot-диз-cxp-дарт.png')
examples.append(u'2016-10-27-092544_1024x600_scrot-диз-бонтекст-типографика-веб-дарт--шапка-выравнивание-по-вертикали.png')
examples.append(u'2016-10-27-093630_1024x600_scrot-cx.png')
examples.append(u'Снимок экрана от 2016-10-26 16-18-07-ro.png')
examples.append(u'Снимок экрана от 2016-10-27 09-57-14-диз-цвета-зелёный-дарт-гитхаб.png')
examples.append(u'Снимок экрана от 2016-10-27 09-58-31-диз-веб-цвета-гитхаб-эксплор--эксплоръ-фэт')
examples.append(u'2016-10-27-101359_1024x600_scrot-мкрк-редактура-вопрос-английский-язык--запятая--артикль--смысл-невнятица.png')
examples.append(u'Снимок экрана от 2016-10-27 11-09-33-мкрк-редактура-вопрос-паттерн-необязательно--раздельно.png')
examples.append(u'2016-10-24-082047_1024x600_scrot-диз-аниме-персонажи-death-note-1-27.png')
examples.append(u'2016-10-23-123156_1024x600_scrot-диз-аниме-персонажи-death-note-1-27.png')
examples.append(u'Снимок экрана от 2016-10-27 14-46-21-мкрк-редактура-альманах-ливецея-гайдо-паттерн-начиная-с-какой-версии-haxe.png')
examples.append(u'2016-10-27-162526_1024x600_scrot-мкрк-breakes-out-of-the.png')
examples.append(u'2016-10-27-162752_1024x600_scrot-you-are-30-seconds-aways-from.png')
examples.append(u'2016-10-27-163432_1024x600_scrot-if-you-are-still-unsure-if.png')
examples.append(u'2016-10-27-164752_1024x600_scrot-мкрк-английский-язык-паттерн-another-place-where-nn-can-be-used-is--another-place-nn-can-be-used-is.png')
examples.append(u'2016-10-27-170315_1024x600_scrot-мкрк-перевод-английский-язык-паттерн-не-забудьте-vbi--remember-to-vbi.png')
examples.append(u'2016-10-27-180401_1024x600_scrot-мкрк-английский-язык-артикли.png')
examples.append(u'2016-10-27-182311_1024x600_scrot-мкрк-паттерн-thus-запятая.png')
examples.append(u'2016-10-27-203151_1024x600_scrot-вопрос-sloc.png')


#
# Create a lexem category map for every input string
#

def lexem_category(unicode_character):
    """Returns Unicode Category name of the symbol."""
    import unicodedata
    return unicodedata.category(unicode_character)

def lexem_type(unicode_character):
    """Returns the 1st symbol of Unicode Category name of the symbol."""
    return lexem_category(unicode_character)[:1]

header("""Create a lexem category map for every input string""")
maps = []
for number, sentence in enumerate(examples):
    print number, sentence
    number_length = len(str(number))
    sentence_map = ''
    for position, symbol in enumerate(sentence):
        sentence_map = sentence_map + lexem_type(symbol)
    maps.append(sentence_map)
    print ' ' * number_length, sentence_map


#
# Print lexem category maps
#

#~ header("""Print lexem category maps""")
#~ for number, map in enumerate(maps):
    #~ print number, map


#
# Create a portion: a list of lists of tokens of every input sentence
#

portion = []

def no_space_conjunction(tag1, tag2):
    """If two tags represents one number and one letter."""
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
# Print all the tokens of the current input portion
#

for number, sentence in enumerate(portion):
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
count = 50

def get_value(dictionary, key):
    return dictionary[key]

def get_rate(key):
    return get_value(words, key)

header('*'*72, """Top""", count, """words""", '*'*72)
nominees = sorted(words.keys(), key=lambda v: words[v], reverse=True)[:count]
for place, word in enumerate(nominees):
    print place, word

show('Tokens index volume:', len(words.keys()))
