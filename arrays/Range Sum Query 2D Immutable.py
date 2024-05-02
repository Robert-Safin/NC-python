# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # make matrix with same dimensions+1, place 0 in all cells
        self.values = [ [ 0 for y in range(COLS+1) ] for x in range(ROWS+1) ]

        # calc 2d prefix sum, by adding left + above values
        for row in range(ROWS):
            prefix_sum = 0
            for col in range(COLS):
                prefix_sum += matrix[row][col]
                # there is padding in new matrix but none in original,
                # hence we increment col but leave row
                # getting the value directly above
                above = self.values[row][col+1]
                # offset by one due to padding
                self.values[row+1][col+1] = prefix_sum + above


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # account padding
        r1 = row1+1
        r2 = row2+1
        c1 = col1+1
        c2 = col2+1

        # 2D sum form top-left to the query bottom-right
        bottom_right = self.values[r2][c2]
        # area above query
        above = self.values[r1-1][c2]
        # area left of query
        left = self.values[r2][c1-1]
        # area that is contained in both above and left, which needs to be re added
        top_left = self.values[r1-1][c1-1]

        return bottom_right - above - left + top_left



mat = [ [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5] ]

nm = NumMatrix(mat)





print(nm.sumRegion(2, 1, 4, 3)) # 8
