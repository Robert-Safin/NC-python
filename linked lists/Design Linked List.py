# Design your implementation of the linked list. You can choose to use a singly
# or doubly linked list. A node in a singly linked list should have two attributes:
# val and next. val is the value of the current node, and next is a pointer/reference
# to the next node. If you want to use the doubly linked list, you will need
# one more attribute prev to indicate the previous node in the linked list.
# Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

from typing import Optional,cast
# SINGLE LINKED IMPL

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self) -> None:
        # aka tail & head. Init with 'dummy' nodes which handle edge cases.
        self.left = ListNode(0)
        self.right = ListNode(0)
        #link tail and head to each other
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        # track current nodes and index
        i = 0
        current_node = self.left.next
        # edge case
        if index < 0:
            return -1

        # try to reach node at index, handle out of bounds with None check
        while i != index and current_node != None:
            # update counters
            current_node = current_node.next
            i += 1

        # avoid reading None, avoid returning 'dummy' node
        if current_node != None and current_node != self.right:
            return current_node.val
        else:
            return -1


    def addAtHead(self, val: int) -> None:
        # init new node
        new_head = ListNode(val)
        # set new node's pointers
        new_head.prev = self.left
        new_head.next = self.left.next
        # update surrounding nodes
        self.left.next.prev = new_head
        self.left.next = new_head


    def addAtTail(self, val: int) -> None:
        # init new node
        new_tail = ListNode(val)
        # set new node's pointers
        new_tail.prev = self.right.prev
        new_tail.next = self.right
        # update surrounding nodes
        self.right.prev.next = new_tail
        self.right.prev = new_tail



    def addAtIndex(self, index: int, val: int) -> None:
        # track current nodes and index
        current_node = self.left.next
        i = 0
        # edge case
        if index < 0:
            return

        # try to reach node at index, handle out of bounds with None check
        while i != index and current_node != None:
            # update counters
            current_node = current_node.next
            i += 1

        # avoid reading None
        if current_node != None:
            # init new node
            new_node = ListNode(val)
            # set new node's pointers
            new_node.next = current_node
            new_node.prev = current_node.prev
            # update surrounding nodes
            current_node.prev.next = new_node
            current_node.prev = new_node
        else:
            return


    def deleteAtIndex(self, index: int) -> None:
        # track current nodes and index
        current_node = self.left.next
        i = 0
        # edge case
        if index < 0:
            return

        # try to reach node at index, handle out of bounds with None check
        while i != index and current_node != None:
            # update counter
            current_node = current_node.next
            i += 1

        # avoid reading None, avoid deleting 'dummy' node
        if current_node != None and current_node != self.right:
            # set temp values of surrounding nodes
            temp_prev = current_node.prev
            temp_next = current_node.next
            # update surrounding nodes
            current_node.prev.next = temp_next
            current_node.next.prev = temp_prev
        else:
            return



list = MyLinkedList()
list.addAtHead(7)
list.addAtHead(2)
list.addAtHead(1)
list.addAtIndex(3, 0)




current = list.left
while current != None:
    print('from head',current.val)
    current = current.next

print('-----------------')

current = list.right
while current != None:
    print('from tail',current.val)
    current = current.prev
