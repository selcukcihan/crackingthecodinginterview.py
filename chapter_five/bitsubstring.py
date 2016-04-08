#! /usr/bin/env python
"""
You are given two 32-bit numbers, N and M, and two bit positions, i and j. Write a
method to set all bits between i and j in N equal to M (e.g., M becomes a substring of
N located at i and starting at j).
EXAMPLE:
Input: N = 10000000000, M = 10101, i = 2, j = 6
Output: N = 10001010100
"""

import string

digs = string.digits + string.letters

def int2base(x, base):
    if x < 0: sign = -1
    elif x == 0: return digs[0]
    else: sign = 1
    x *= sign
    digits = []
    while x:
        digits.append(digs[x % base])
        x /= base
    if sign < 0:
        digits.append('-')
    digits.reverse()
    return ''.join(digits)

def set_bits(n, m, i, j):
    """
    N: 10000000000
    M: 10101
    R: 10001010100
    NN = N AND 11110000011: zero out bits from i to j
    MM = M << i: 00001010100
    R = NN | MM
    """
    mask = 0xFFFFFFFF & (~(((~(0xFFFFFFFF << (j + 1 - i))) & 0xFFFFFFFF) << i))
    print int2base(n, 2)
    print int2base(m, 2)
    print int2base(mask, 2)
    nn = n & mask
    print int2base(nn, 2)
    mm = m << i
    print int2base(mm, 2)
    return nn | mm

def test_run():
    n = 0b10000000000
    m = 0b10101
    i = 2
    j = 6
    modified = set_bits(n, m, i, j)
    print int2base(modified, 2)
    
