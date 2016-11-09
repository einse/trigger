# trigger
A simple text parser.

## Status

The last version of Trigger got some troublesome issues:

- [Fail on the '-t' key (#3)](https://github.com/einse/trigger/issues/3)
- [Unintended output files (#4)](https://github.com/einse/trigger/issues/4)

Please consider using older versions instead:

- [v1.1](https://github.com/einse/trigger/releases/tag/v1.1)
- [v1.0.2](https://github.com/einse/trigger/releases/tag/v1.0.2)

Also please don't clone the Trigger's repo until the program get fixed.

_They told me not to push untested changes to the 'master' branch... Let this be a lesson to me. - S. A._

## How to Use It

Just run the script "trigger.py" by using Python 2 interpreter:

    python2 trigger.py

If the current directory contains a file named "trgr_examples.txt",
the script will read it; then, if strings provided, they will be
tokenized.

If "trgr_examples.txt" is not found, the usage info will be printed.

You can also invoke the usage info by adding the ```--help``` flag
(note that the script execution will be halted, even if any other flags
provided):

    python2 trigger.py --help

## Developing and Contributing

Contributing is NOT welcome for this repo, because I plan to publish it
to Public Domain, using CC0. Sorry for that.

## Legal and Licensing

Please see the LICENSE file.

## Technical Details

Trigger hasn't yet been tested on memory usage, performance, or any
other parameters. Be careful about that. Though it was mentioned in the
LICENSE file, use the scripts at your own risk and please don't complain
if things go wrong.
