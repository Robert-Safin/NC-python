# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

# Do not modify the linked list.

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    # third pointer will be launched if cycle detected
    # note: it is possible to not use 3rd pointer, by resetting existing pointers
    slow2 = head

    # detect cycle
    while fast and fast.next:
        slow = slow.next # type: ignore
        fast = fast.next.next

        # cycle found
        if slow == fast:
            # move both slow pointers once until they equal
            while slow2 != slow:
                slow = slow.next # type: ignore
                slow2 = slow2.next # type: ignore
            # equal node is cycle start
            return slow

    # no cycle found
    return None
