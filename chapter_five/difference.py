#! /usr/bin/env python
"""
Write a function to determine the number of bits required to convert integer A to integer B.
Input: 31, 14
Output: 2
"""

"""
100000 - 1 = 11111
             01110
"""

def different_bit_count(n1, n2):
    xor = n1 ^ n2
    count = 0
    while xor > 0:
        if xor & 1:
            count += 1
        xor >>= 1
    return count

def bit_string(n):
    retval = ""
    while n > 0:
        retval = str(n & 1) + retval
        n >>= 1
    return retval.zfill(8)
    
def test_run():
    for pair in [(31, 14), (1, 2), (10, 20)]:
        first = bit_string(pair[0])
        second = bit_string(pair[1])
        diff = different_bit_count(pair[0], pair[1])
        print first
        print second
        print diff
        print "----------"

test_run()
