# Given a root node reference of a BST and a key, delete the node with
# the given key in the BST. Return the root node reference
# (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minValue(root:TreeNode) -> TreeNode:
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root:
        return None

    if key > root.val:
        root.right = deleteNode(root.right, key)

    elif key < root.val:
        root.left = deleteNode(root.left, key)


    else:

        if not root.left:
            return root.right
        elif not root.right:
            return root.left


        else:

            minNode = minValue(root.right)

            root.val = minNode.val

            root.right = deleteNode(root.right, minNode.val)
    return root
