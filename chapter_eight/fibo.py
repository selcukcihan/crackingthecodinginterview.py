#! /usr/bin/env python
"""
Write a method to generate the nth Fibonacci number
"""

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

def test_run():
    for i in range(10):
        print str(i) + "th fibo: " + str(fibo(i))

test_run()
