from typing import Optional,List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    out:List[int] = []

    if not root:
        return out

    inorderTraversal(root.left)
    out.append(root.val)
    inorderTraversal(root.right)

    return out
