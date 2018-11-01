#!/usr/bin/env python3
"""
Replace all words with woofs, preserving punctuation.

For NaNoGenMo and NaNoLiPo 2018.
https://github.com/NaNoGenMo/2018
https://github.com/ojahnn/NaNoLiPo2018
"""
from __future__ import print_function, unicode_literals

import re
import sys
import argparse


def is_word(thing):
    found = re.match(r"\w+", thing, re.UNICODE)
    return found


def woof_woof(line, converter_fun):
    """Woofify a line"""
    woofed = []
    # Break line into words and non-words (e.g. punctuation and space)
    things = re.findall(r"\w+|[^\w]", line, re.UNICODE)
    for thing in things:
        if is_word(thing):
            woofed.append(converter_fun(thing))
        else:
            woofed.append(thing)
    return "".join(woofed)


def woof(word):
    """Woofify a word"""
    woofed = ""
    length = len(word)

    if length == 1:
        return capify("w", word)
    elif length == 2:
        return capify("wf", word)
    elif length == 3:
        return capify("wof", word)
    elif length == 4:
        return capify("woof", word)

    # Words longer than four will have:
    #  * first letter W
    #  * last letter F
    #  * middle with a random number of Os, then some Os

    # Number of Os:
    ohs = length - len("w") - len("f")

    woofed = "w" + ("o" * ohs) + "f"
    return capify(woofed, word)


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
        description="Replace all words with woofs, preserving punctuation."
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
        print(woof_woof(line, woof))

# End of file
