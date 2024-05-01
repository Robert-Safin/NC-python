# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        vals:List[List[int]] = []

        for row in matrix:
            sum = 0
            res:List[int] = []

            for val in row:
                sum += val
                res.append(sum)

            vals.append(res)

        self.matrix = vals

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0

        for row in self.matrix[row1:row2+1]:
            left_bound = 0
            if col1 > 0:
                left_bound = col1
            row_sum = row[col2] - row[left_bound-1]

            sum += row_sum

        return sum




mat = [[-1 ]]

nm = NumMatrix(mat)
#print(nm.matrix)


print(nm.sumRegion(0, 0, 0, 0)) # 8
