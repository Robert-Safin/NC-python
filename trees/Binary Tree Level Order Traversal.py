

from typing import Optional,List
from collections import deque
from typing import Deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def levelOrder(root: TreeNode) -> List[List[int]]:
    res = []
    q:Deque[TreeNode] = deque()
    if root:
        q.append(root)

    while q:
        val = []

        for i in range(len(q)):
            node = q.popleft()
            val.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(val)
    return res
