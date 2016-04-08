#! /usr/bin/env python
"""
Given an integer, print the next smallest and next largest number that have the same
number of 1 bits in their binary representation.

increment/decrement by 1, count bit number

0111 => 1000, 1001, 1010, 1011
0011 => 0100, 0101
0101 => 0110
1110010 => 1110011, 1110100
1110100

01000 => 01001, 01010, 01011, 01100, 01101, 01110, 01111, 10000



01110 => 01111, 10000, 10001, 10010, 10011

1 1100

11100


01110
10110


001000 1100
001001 1000

0010010100

0010010001

"""

def print_next_large(n):
    _n = n
    one_detected = False
    zero_after_ones_position = -1
    position_begin = 0
    position_end = 0
    position = 0
    # 01011 (decimal 11)
    while _n > 0:
        if _n & 0x1: # this is the first one bit
            position_begin = position
            position_end = position
            # position_begin = 0
            # position_end = 2
            while _n > 0 and _n & 0x1: # 00101 (position = 1), 00010 (position = 2)
                position_end += 1
                _n = _n >> 1
            break
        position += 1
        _n = _n >> 1
        
    if _n > 0:
        m = n | (0x1 << position_end) # m: 01111
        m = m & ((~(0x1 << position_begin)) & 0xFFFFFFFF)
        # m = 01110
        
        _m = m
        while _m > 0:
            
