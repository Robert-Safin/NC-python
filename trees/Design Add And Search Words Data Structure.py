# Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Implement the WordDictionary class:

# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


from typing import Dict,List,Tuple

class TrieNode:
    def __init__(self) -> None:
        self.children:Dict[str, TrieNode] = {}
        self.word = False



class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.word = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)

    def dfs(self, node: TrieNode, word: str, index: int) -> bool:
        # base case for reach end of word
        if index == len(word):
            return node.word

        # current char
        char = word[index]

        # handle wildcard
        if char == '.':
            for child in node.children.values():
                # check if any child reaches base case
                if self.dfs(child, word, index + 1):
                    return True

        # handle normal char
        else:
            if char in node.children:
                return self.dfs(node.children[char], word, index + 1)

        # handle not found char
        return False
