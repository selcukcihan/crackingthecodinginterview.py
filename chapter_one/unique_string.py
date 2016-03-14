#! /usr/bin/env python
"""
"""
def unique_chars(input_string):
    char_counts = set()
    for c in input_string:
        if c in char_counts:
            return False
        else:
            char_counts.add(c)
    return True

def unique_chars_no_ds(input_string):
    for i, source_char in enumerate(input_string):
        for j, target_char in enumerate(input_string[i + 1:]):
            if source_char == target_char:
                return False
    return True

def test_run():
    inputs = ["uniq chars", "no unique chars"]
    for s in inputs:
        u1 = unique_chars(s)
        u2 = unique_chars_no_ds(s)
        print "{0}: {1}, {2}".format(s, u1, u2)

