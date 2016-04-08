#! /usr/bin/env python
"""
5.2 Given a (decimal - e.g. 3.72) number that is passed in as a string, print the binary representation.
If the number can not be represented accurately in binary, print "ERROR"
"""

"""

0.17 = (1 / 10) + (7 / 100)
0.0101 = 0 / 2 + 1 / 4 + 0 / 8 + 1 / 16 = 5 / 16 

    x * 5^n            Y * 2^3n
--------------  =    -----------
  2^4n * 5^n           2^n * 5^n
  
"""
    
def to_binary(value):
    bits = ""
    while value > 0:
        bits = str(value % 2) + bits
        value = value // 2
    return bits
    
def print_binary_new(nstring):
    numbers = [int(s) for s in nstring.split(".")]
    numbers_string = [s for s in nstring.split(".")]
    bits = to_binary(numbers[0])
    if len(numbers) > 1:
        digits = len(numbers_string[1])
        divider = pow(5, digits)
        print "divider"
        print divider
        if numbers[1] % divider > 0:
            raise Exception("Not expressable in base 2")
        base2 = numbers[1] * pow(2, 3 * digits) / divider
        print "base2"
        print base2
        base2str = to_binary(base2)
        print "base2str"
        print base2str
        for i in range(4 * digits - len(base2str)):
            base2str = "0" + base2str
        print bits + "." + base2str
    else:
        print bits

def test_run():
    print_binary_new("20")
    print_binary_new("3.75")
    print_binary_new("32.0675")
    
        
