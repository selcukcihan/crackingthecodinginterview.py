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

11100
10011

1 1100

11100


01110
10110


001000 1100
001001 1000

0010010100

0010010001

"""

def print_base_2(value):
    valstr = ""
    while value > 0:
        valstr = str(value % 2) + valstr
        value = value // 2

    print valstr

def next_large(n):
    _n = n
    position_begin = 1
    position_end = 1
    position = 1
    while _n > 0:
        if _n & 0x1: # this is the first one bit
            position_begin = position
            position_end = position
            while _n > 0 and _n & 0x1:
                position_end += 1
                _n = _n >> 1
            break
        position += 1
        _n = _n >> 1
    if position_end > 0:
        m = n | (0x1 << (position_end - 1))
        m = m & (0xFFFFFFFF << (position_end - 1)) 
        m = m | ((1 << (position_end - position_begin - 1)) - 1)
        return m
    return n

"""
01100 shift last one to right
01010

01111
no solution

1000
0100

1011, 1010, 1001, 1000, 0111
0111

101011
100111

en sagdan bitlere bak, ilk biri saga kaydir. saga kayamiyorsa devam et o grup birleri gec yine dene
buldugun pozisyonu sifirla, bir kucuk pozisyonu birle

"""

def next_small(n):
    zero_detected = False
    _n = n
    position = -1
    current_position = 1
    while _n > 0:
        if _n & 0x1 > 0: # the bit is one
            if zero_detected:
                # do stuff
                position = current_position
                break

            zero_detected = False
        else: # the bit is zero
            zero_detected = True

        current_position += 1
        _n = _n >> 1

    if position == -1:
        raise Exception("No next smallest for the given integer")

    zeroing_mask = (~(1 << (position - 1))) & 0xFFFFFFFF
    one_mask = 1 << (position - 2)
    return (n & zeroing_mask) | one_mask

def test_run():
    #print_base_2(next_large(0b0111))
    #print_base_2(next_large(0b01110))
    #print_base_2(next_large(0b01010))
    print_base_2(next_small(0b01010))
    print_base_2(next_small(0b01100))
    print_base_2(next_small(0b01000))
    print_base_2(next_small(0b1011))
    print_base_2(next_small(0b101011))

