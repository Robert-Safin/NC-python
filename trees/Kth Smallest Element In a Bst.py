
from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # List to keep track of the k smallest elements
    res:List[int] = []

    # Helper function to perform in-order traversal
    def helper(node):
        # Use nonlocal to modify the list defined in the enclosing scope
        if not node or len(res) >= k:
            return
        helper(node.left)
        if len(res) < k:
            res.append(node.val)
            helper(node.right)

    helper(root)
    return res[-1]  # The k-th smallest element
