# trigger
A simple text parser.

## How to use it

Just run the script "tokenizer.py" by using Python 2 interpreter:

    python2 tokenizer.py

If the current directory contains a file named "examples.txt",
the script will read it; then, if strings provided, they will be
tokenized and the output will be following:

+ All read strings with a 'lexem category map' for each of them.
+ Words rating (top 50 or less).
+ Size of tokens index.

If "examples.txt" is not found, the usage info will be printed.

You can also invoke the usage info by typing ```--help``` (note that
the script execution will be halted, even if any other keys provided):

    python2 tokenizer.py --help

## Developing and Contributing

Contributing is NOT welcome for this repo, because I plan to publish it
to Public Domain, using CC0. Sorry for that.

## Legal and Licensing

Please see the LICENSE file.
