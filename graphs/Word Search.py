# Given an m x n grid of characters board and a string word, return true
# if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.


from typing import List,Tuple

def exist(board: List[List[str]], word: str) -> bool:
    ROWS = len(board)
    COLS = len(board[0])

    # find cells where char is equal to first char in word
    # and dfs it
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == word[0]:
                if dfs(board, row, col, word, 0):
                    return True

    return False

def dfs(board: List[List[str]], row: int, col: int, word: str, index: int) -> bool:
    ROWS = len(board)
    COLS = len(board[0])

    # base case, entire word has been found
    if index == len(word):
        return True

    # discard out of bounds and wrong chars
    if (row < 0 or col < 0 or row >= ROWS or col >= COLS or
            board[row][col] != word[index]):
        return False

    # Mark the cell as visited
    temp = board[row][col]
    board[row][col] = '#'

    found = (dfs(board, row + 1, col, word, index + 1) or
             dfs(board, row - 1, col, word, index + 1) or
             dfs(board, row, col + 1, word, index + 1) or
             dfs(board, row, col - 1, word, index + 1))

    # Restore the cell's original value
    # this is needed since the 'outer loop' in fn exist needs untouched grid for each entry point
    board[row][col] = temp
    return found






board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"

print(exist(board,word))
