#!/usr/bin/env python3
"""
Unit tests for moo.py
"""
import unittest
import moo
import re


class TestIt(unittest.TestCase):
    def sanity_check(self, word, out):
        self.assertEqual(len(word), len(out))

        # Check pattern
        if len(word) > 4:
            found = re.match("mooo[o]+", out, re.IGNORECASE)
            self.assertTrue(found)

        # Check caps
        for i in range(len(word)):
            self.assertEqual(word[i].isupper(), out[i].isupper())

    def test_1_letter_word(self):
        word = "I"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "M")

    def test_2_letter_word(self):
        word = "on"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "mo")

    def test_3_letter_word(self):
        word = "The"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Moo")

    def test_4_letter_word(self):
        word = "book"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "mooo")

    def test_capify_1(self):
        word = "moo"
        reference = "Pen"
        out = moo.capify(word, reference)
        self.assertEqual(out, "Moo")

    def test_capify_2(self):
        word = "moo"
        reference = "PEN"
        out = moo.capify(word, reference)
        self.assertEqual(out, "MOO")

    def test_capify_3(self):
        word = "moo"
        reference = "pen"
        out = moo.capify(word, reference)
        self.assertEqual(out, "moo")

    def test_capify_4(self):
        word = "moo"
        reference = "PeN"
        out = moo.capify(word, reference)
        self.assertEqual(out, "MoO")

    def test_upper_4_letter_word(self):
        word = "BOOK"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "MOOO")

    def test_capped_4_letter_word(self):
        word = "Book"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Mooo")

    def test_mixcapped_4_letter_word(self):
        word = "BooK"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "MooO")

    def test_5_letter_word(self):
        word = "clock"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "moooo")

    def test_6_letter_word(self):
        word = "whales"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "mooooo")

    def test_13_letter_word(self):
        word = "Extraordinary"
        out = moo.moo(word)
        self.sanity_check(word, out)
        self.assertEqual(out, "Moooooooooooo")

    def test_line(self):
        line = "On the bus"
        out = moo.moo_moo(line, moo.moo)
        self.assertEqual(out, "Mo moo moo")

    def test_is_word_1(self):
        thing = "word"
        out = moo.is_word(thing)
        self.assertTrue(out)

    def test_is_word_2(self):
        thing = ";"
        out = moo.is_word(thing)
        self.assertFalse(out)

    def test_line_punctuation(self):
        line = "On the bus? On the bus."
        out = moo.moo_moo(line, moo.moo)
        self.assertEqual(out, "Mo moo moo? Mo moo moo.")


if __name__ == "__main__":
    unittest.main()

# End of file
