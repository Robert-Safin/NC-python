# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in
# the HashSet, do nothing.





class MyHashSet:

    def __init__(self):
        self.capacity = 2
        self.items = [[], []]
        self.count = 0

    def hash(self, key: int) -> int:
        return key % self.capacity

    def resize(self) -> None:
        self.capacity *= 2
        old_items = self.items
        self.items = [[] for _ in range(self.capacity)]
        self.count = 0

        for item_array in old_items:
            for item in item_array:
                self.add(item)

    def add(self, key: int) -> None:
        index = self.hash(key)
        if key not in self.items[index]:
            self.items[index].append(key)
            self.count += 1

            if self.count > self.capacity * 10:
                self.resize()

    def remove(self, key: int) -> None:
        index = self.hash(key)
        if key in self.items[index]:
            self.items[index].remove(key)
            self.count -= 1

    def contains(self, key: int) -> bool:
        index = self.hash(key)
        return key in self.items[index]
