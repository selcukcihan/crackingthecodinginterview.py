#! /usr/bin/env python
"""
An array A[1...n] contains all the integers from 0 to n except for one number which is
missing. In this problem, we cannot access an entire integer in A with a single operation.
The elements of A are represented in binary, and the only operation we can use
to access them is fetch the jth bit of A[i], which takes constant time. Write code to
find the missing integer. Can you do it in O(n) time?
"""


"""
0: 000
0: 001
0: 010
0: 011
------100
1: 101
0: 110
1: 111

"""
0


class WeirdArray:
    def __init__(self, missing_value):
        self.missing_value = missing_value
        self.values = range(0, 0xFFFF + 1)
        self.values.remove(self.missing_value)
        print "Array: " + str(self.missing_value)
    def fetch(self, i, j):
        if j < 1 or j > 32:
            raise Exception("bit index out of range")
        val = self.values[i] & ((0xFFFF + 1) >> j) > 0
        return 1 if val > 0 else 0

def find_missing_value(A):
    retval = 0
    for j in range(1, 33):
        bit = 0
        for i in range(0, len(A.values)):
            bit ^= A.fetch(i, j)
        if bit:
            retval = retval | ((0xFFFF + 1) >> j)
    return retval

def test_run():
    print find_missing_value(WeirdArray(34567))
    print find_missing_value(WeirdArray(0))
    print find_missing_value(WeirdArray(0xFFFF))
    print find_missing_value(WeirdArray(3 << 5))

test_run()

