#! /usr/bin/env python
"""
"""

def are_anagrams(first, second):
    character_counts = {}
    for c in first:
        if c in character_counts:
            character_counts[c] = character_counts[c] + 1
        else:
            character_counts[c] = 1
    for c in second:
        if c not in character_counts:
            return False
        else:
            character_counts[c] = character_counts[c] - 1
            if character_counts[c] == 0:
                character_counts.pop(c)
    return len(character_counts) == 0

def test_run():
    lst = [ {"anagram": "gramana"},
            {"baba": "bab"},
            {"": ""},
            { "baba": "aabba"},
            {"babba": "abbba"},
            {"ba": "abbba"},
            {"babab": "ab"},
            {"": "dede"},
            {"haydisene": ""}
        ]
    for item in lst:
        for first, second in item.iteritems():
            print first + " - " + second + ": " + str(are_anagrams(first, second))
                
