# The median is the middle value in an ordered integer list. If the size of the
# list is even, there is no middle value, and the median is the mean of the two middle values.

# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within
# 10-5 of the actual answer will be accepted.


from typing import List
from heapq import heappush,heappop


class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heappush(self.large, num)
        else:
            heappush(self.small, -1 * num)

        if len(self.small) > len(self.large) + 1:
            val = -1 * heappop(self.small)
            heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = -1 * heappop(self.large)
            heappush(self.small, val)

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return -1 * self.small[0]

        elif len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2




mf = MedianFinder()
mf.addNum(5)
mf.addNum(4)
mf.addNum(3)
mf.addNum(7)


print(mf.small,mf.large)
