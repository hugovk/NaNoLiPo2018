#!/usr/bin/env python3
"""
Replace all words with moos, preserving punctuation.

For NaNoGenMo and NaNoLiPo 2018.
https://github.com/NaNoGenMo/2018
https://github.com/ojahnn/NaNoLiPo2018
"""
import re
import sys
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def moo_moo(line, converter_fun):
    """Mooify a line"""
    mooed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            mooed.append(converter_fun(thing))
        else:
            mooed.append(thing)
    return "".join(mooed)


def moo(word):
    """Mooify a word"""
    length = len(word)

    return capify("m" + "o" * (length - 1), word)


def capify(word, reference):
    """Make sure word has the same capitalisation as reference"""
    new_word = ""

    # First check whole word before char-by-char
    if reference.islower():
        return word.lower()
    elif reference.isupper():
        return word.upper()

    # Char-by-char checks
    for i, c in enumerate(reference):
        if c.isupper():
            new_word += word[i].upper()
        else:
            new_word += word[i]
    return new_word


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Replace all words with moos, preserving punctuation."
    )
    parser.add_argument(
        "infile",
        nargs="?",
        type=argparse.FileType("r"),
        default=sys.stdin,
        help="Input text",
    )
    parser.add_argument(
        "-t",
        "--translation",
        action="store_true",
        help="Output a line-by-line translation",
    )
    args = parser.parse_args()

    for line in args.infile:
        line = line.rstrip()
        if args.translation:
            print()
            print(line)
        print(moo_moo(line, moo))

# End of file
