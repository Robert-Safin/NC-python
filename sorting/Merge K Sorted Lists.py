# You are given an array of k linked-lists lists, each linked-list
# is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.
from typing import Optional, List
from collections import defaultdict
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# suboptimal solution. can be solved using map with value counts to also reconstruct

def mergeKLists(lists: List[Node]) -> Optional[Node]:
    arr:List[int] = []

    # collect all values of from all linked lists into array
    for ar in lists:
        curr = ar
        while curr != None:
            arr.append(curr.val)
            curr = curr.next

    # edge case
    if not arr:
        return None

    # classic merge sort
    sorted = mergeSort(arr)

    # init head
    head = Node(sorted[0])
    # loop and add pointer to next node
    current = head
    for i in range(1,len(sorted)):
        current.next = Node(sorted[i])
        current = current.next

    return head


def mergeSort(nums:List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    split = len(nums) // 2

    left = nums[:split]
    right = nums[split:]

    left_sorted = mergeSort(left)
    right_sorted = mergeSort(right)

    return merge(left_sorted,right_sorted)


def merge(left:List[int], right:List[int]) -> List[int]:
    result = []

    while (left and right):

        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    if left:
        result += left

    if right:
        result += right

    return result





# node1 = Node(5)
# node2 = Node(4,node1)
# node3 = Node(1,node2)

# node4 = Node(4)
# node5 = Node(3,node4)
# node6 = Node(1,node5)

# node7 = Node(6)
# node8 = Node(2,node7)

# arr = [node3, node6, node8]

# out = mergeKLists(arr)


# current = out
# while current != None:
#     print(current.val)
#     current = current.next
