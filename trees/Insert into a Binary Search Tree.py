# You are given the root node of a binary search tree (BST) and a value
# to insert into the tree. Return the root node of the BST after
# the insertion. It is guaranteed that the new value does not exist
# in the original BST.

# Notice that there may exist multiple valid ways for the insertion,
# as long as the tree remains a BST after insertion. You can return
# any of them.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    elif val < root.val:
        root.left = insertIntoBST(root.left, val)
    return root
