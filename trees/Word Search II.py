# Given an m x n board of characters and a list of strings words,
# return all words on the board.

# Each word must be constructed from letters of sequentially
# adjacent cells, where adjacent cells are horizontally or vertically
# neighboring. The same letter cell may not be used more than once in a word.

from typing import List,Dict,Set,Tuple


class TrieNode:
    def __init__(self) -> None:
        self.children:Dict[str,TrieNode] = {}
        self.word = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word:str) -> None:
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.word = True

    def starts_with(self, prefix:str) -> bool:
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def search(self, word:str) -> bool:
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.word

# optimal BigO but can have major runtime improvements via
# not searching for word once it was found already
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # init PrefixTree
        trie = Trie()
        for word in words:
            trie.insert(word)

        # the approach can lead to duplicate value, hence use set
        result:Set[str] = set()

        # dfs each cell
        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board,trie.root,result,row,col, '', set())

        # convert to list for output
        return list(result)

    def dfs(self, board: List[List[str]], node: TrieNode, result:Set[str], row:int, col:int, prefix:str, visited:Set[Tuple[int,int]]) -> None:

        # abort out of bounds / already visited / non resulting paths
        ROWS, COLS = len(board), len(board[0])
        if (row < 0 or col < 0 or
            row >= ROWS or col >= COLS
            or (row, col) in visited or
            board[row][col] not in node.children):
            return

        # update visited
        visited.add((row,col))

        # append new char to prefix
        prefix += board[row][col]
        # update node
        node = node.children[board[row][col]]
        # check if node end of word
        if node.word:
            result.add(prefix)

        # should continue searching even if word found, e.g. found 'app' but there is also 'apple'
        self.dfs(board,node,result,row+1,col,prefix,visited)
        self.dfs(board,node,result,row,col+1,prefix,visited)
        self.dfs(board,node,result,row-1,col,prefix,visited)
        self.dfs(board,node,result,row,col-1,prefix,visited)

        # unmark, as deeper call begin unwinding, shallow calls can explore the cell via diff path
        visited.remove((row,col))




board = [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

sol = Solution()
sol.findWords(board,words) #["eat","oath"]
