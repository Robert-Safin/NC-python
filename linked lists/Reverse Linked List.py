# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional, Literal

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> Optional[ListNode]:
    cur, prev = head, None

    while cur != None:
        # store next pointer as it will be severed
        temp = cur.next
        # reverse node pointer
        cur.next = prev
        # update prev iterator pointer
        prev = cur
        # update cur iterator pointer
        cur = temp

        # one liner:
        # cur.next, prev, cur = prev, cur, cur.next


    return prev



node_5 = ListNode(5,None)
node_4 = ListNode(4,node_5)
node_3 = ListNode(3,node_4)
node_2 = ListNode(2,node_3)
node_1 = ListNode(1,node_2)

reverseList(node_1)


current = node_5
while current != None:
    print(current.val)
    current = current.next
