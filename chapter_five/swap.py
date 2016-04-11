#! /usr/bin/env python
"""
Write a program to swap odd and even bits in an integer with as few instructions as
possible (e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, etc).
"""


"""

n:       012345
left:    12345-: 101010
right:   -01234: 010101
103254

0100 => 1000
1000 => 

1011 => 0111
0111

0101 => 1010
1010

0110 => 1001
"""
def swap(n):
    rmask = 0x55555555
    lmask = rmask << 1
    left = n << 1
    right = n >> 1
    return (left & lmask) | (right & rmask)

def print_bits(n):
    retval = ""
    while n > 0:
        retval = str(n & 1) + retval
        n >>= 1
    print retval.zfill(8)
    
def test_run():
    for i in range(16):
        s = swap(i)
        print_bits(i)
        print_bits(s)
        print "-----------"

test_run()
