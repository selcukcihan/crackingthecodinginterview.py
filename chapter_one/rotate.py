#! /usr/bin/env python

def rotate(matrix):
    n = len(matrix)
    for r in range(n / 2): # loop over rings
        end = n - r - 1 # rth ring begins from index (r,r) ends at (end, end)
        for i in range(end - r):
            tmp = matrix[r][r + i]
            matrix[r][r + i] = matrix[end - i][r]
            matrix[end - i][r] = matrix[end][end - i]
            matrix[end][end - i] = matrix[r + i][end]
            matrix[r + i][end] = tmp


def print_matrix(matrix):
    for row in matrix:
        print " ".join(row)

def test_run(n):
    matrix = [[chr(97 + n*x + y) for y in range(n)] for x in range(n)]
    print_matrix(matrix)
    rotate(matrix)
    print "\nrotated:\n"
    print_matrix(matrix)
