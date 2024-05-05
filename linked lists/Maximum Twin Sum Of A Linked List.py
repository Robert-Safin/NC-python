# In a linked list of size n, where n is even, the ith node (0-indexed) of the
# linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the
# twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum
# twin sum of the linked list.

from typing import Optional,List,Dict

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head: Optional[ListNode]) -> int:
    # init two pointers
    slow = head
    fast = head

    # used for reversing list
    # will become head of the 2nd list
    prev = None

    while fast and fast.next:
        fast = fast.next.next

        # store copy of slow's next
        tmp = slow.next # type: ignore
        # redirect slow
        slow.next = prev # type: ignore
        # update prev
        prev = slow
        # update slow
        slow = tmp

    # there are now 2 linked list,
    # one where the slow pointer stopped (right half of the original list)
    # second is prev (reversed left half or original list)
    res = 0
    while slow:
        res = max(res, prev.val + slow.val) # type: ignore
        prev = prev.next # type: ignore
        slow = slow.next
    return res



node_1 = ListNode(1,None)
node_2 = ListNode(2,node_1)
node_3 = ListNode(4,node_2)
node_4 = ListNode(5,node_3)


# current = node_4
# while current:
#     print(current.val)
#     current = current.next

print(pairSum(node_4))
