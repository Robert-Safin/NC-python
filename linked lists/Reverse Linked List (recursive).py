from typing import Optional

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


    # recursive function to reverse a linked list
def reverseList(head: ListNode) -> Optional[ListNode]:
        # base case: if head is None or head.next is None, return head
        if head == None or head.next == None:
            return head

        # recursively call the function to reverse the rest of the linked list
        reversed_list = reverseList(head.next)

        # reverse the current node
        head.next.next = head
        head.next = None

        return reversed_list

# node_5 = ListNode(5,None)
# node_4 = ListNode(4,node_5)
# node_3 = ListNode(3,node_4)
# node_2 = ListNode(2,node_3)
# node_1 = ListNode(1,node_2)

# new_head = reverseList(node_1)


# current = new_head
# while current != None:
#     print(current.val)
#     current = current.next
