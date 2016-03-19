from copy import copy, deepcopy

def zero_row_and_column(matrix):
    unchanged = deepcopy(matrix)
    for i, row in enumerate(unchanged):
        for j, val in enumerate(row):
            if val == 0:
                for k in range(len(matrix)):
                    matrix[k][j] = 0
                for k in range(len(matrix)):
                    matrix[i][k] = 0

def test_run():
    matrix = [[1, 2, 3, 0], [1, 1, 1, 1], [1, 1, 1, 1]]
    for row in matrix:
        print row
    zero_row_and_column(matrix)
    print "\n"
    for row in matrix:
        print row

