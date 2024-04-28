# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by
# splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # dummy provides a starting point for the new list, handles case of inserting into empty list
    dummy = ListNode()
    # pointer we update
    pointer = dummy

    # ensure we always have 2 values to compare
    while list1 and list2:
        # update pointer with the smaller value and navigate the list deeper
        if list1.val < list2.val:
            pointer.next = list1
            list1 = list1.next
        # handles the opposite case, as well as values being equal
        else:
            pointer.next = list2
            list2 = list2.next
        # move the pointer for next iteration
        pointer = pointer.next
    # one of the lists can still contain value, so we simply append that list's
    # node as pointer's next
    if list1:
        pointer.next = list1
    if list2:
        pointer.next = list2

    # remember dummy is our fake head, opening it exposes the true new list head
    return dummy.next


node_1 = ListNode(6,None)
node_2 = ListNode(4,node_1)
node_3 = ListNode(3,node_2)


node_4 = ListNode(5,None)
node_5 = ListNode(2,node_4)
node_6 = ListNode(1,node_5)

new_head = mergeTwoLists(node_3, node_6)
current = new_head
while current != None:
    print(current.val)
    current = current.next
