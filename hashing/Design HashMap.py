# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap.
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped,
# or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.

from typing import List,Optional
class ListNode:
    def __init__(self, key:int, val:int, next=None):
        self.key = key
        self.val = val
        self.next = next


class MyHashMap:
    def __init__(self):
        self.capacity = 1000
        self.items = [None] * self.capacity

    def hash(self, key: int) -> int:
        return key % self.capacity

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if self.items[index] is None:
            self.items[index] = ListNode(key, value)
        else:
            current = self.items[index]
            while True:
                if current.key == key:
                    current.val = value  # Update existing key
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = ListNode(key, value)  # Append new element

    def get(self, key: int) -> int:
        index = self.hash(key)
        current = self.items[index]
        while current:
            if current.key == key:
                return current.val
            current = current.next
        return -1

    def remove(self, key: int) -> None:
        index = self.hash(key)
        current = self.items[index]
        prev = None
        while current:
            if current.key == key:
                if prev is None:
                    self.items[index] = current.next  # Remove first node
                else:
                    prev.next = current.next  # Remove middle or last node
                return
            prev = current
            current = current.next
