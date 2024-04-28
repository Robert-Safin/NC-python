# You are given an m x n integer matrix matrix with the
# following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer
# of the previous row.
# Given an integer target, return true if target is in matrix
# or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.



from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    # edge case
    if not matrix or not matrix[0]:
        return False

    top = 0
    bottom = len(matrix) - 1
    row = None

    # Step 1: find the correct row where the target may exist
    while top <= bottom:
        mid = (top + bottom) // 2
        # Check if the target is in the bounds of the current row
        if matrix[mid][0] <= target <= matrix[mid][-1]:
            row = matrix[mid]  # Update row here within the loop
            break
        elif target < matrix[mid][0]:
            bottom = mid - 1
        else:
            top = mid + 1
    else:
        # If no row is found, return False
        return False

    # Step 2: perform binary search on the selected row
    # Check if row is not None (even though we know it should not be due to the break statement)
    if row is not None:
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

    return False





matrix = [  [1, 3, 5, 7],
            [10,11,16,20],
            [23,30,34,60]   ]
target = 3

print(searchMatrix(matrix,target))
