# You are given the root of a binary search tree (BST) and an integer val.

# Find the node in the BST that the node's value equals val and return
# the subtree rooted with that node. If such a node does not exist,
# return null.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

    # base case
    if not root:
        return None

    # search the corresponding side
    if val > root.val:
        return searchBST(root.right, val)
    elif val < root.val:
        return searchBST(root.left, val)
    # else root.val == val
    else:
        return root
