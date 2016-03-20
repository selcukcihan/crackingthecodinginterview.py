#! /usr/bin/env python

"""
"""


#Assume you have a method isSubstring which checks if one word is a substring of another.
#Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring (i e , "waterbottle" is a rotation of "erbottlewat")

def is_rotation(str1, str2):
    candidate = -1
    idx1 = 0
    if len(str1) == 0:
        return False
    for idx2, c2 in enumerate(str2):
        if candidate > -1:
            if c2 == str1[idx1]:
                idx1 = idx1 + 1
            else:
                candidate = -1
        elif c2 == str1[0]:
            candidate = idx2
            idx1 = 1
    if candidate > -1:
        return str1[idx1:] in str2 # isSubstring
    else:
        return False

def test_run():
    print is_rotation("waterbottle", "erbottlewat")
    print is_rotation("elemeler", "elerelem")
    print is_rotation("elfmeler", "elerelem")
    print is_rotation("", "elerelem")
