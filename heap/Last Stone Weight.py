# You are given an array of integers stones where stones[i] is the weight of
# the ith stone.

# We are playing a game with the stones. On each turn, we choose the
# heaviest two stones and smash them together. Suppose the heaviest
# two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of
# weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left,
# return 0.



from typing import List
import heapq

def lastStoneWeight(stones: List[int]) -> int:
    # Simulate max-heap by inverting the signs of the integers
    max_heap = [-stone for stone in stones]
    heapq.heapify(max_heap)  # Create a heap from the list of negated stones (min-heap simulating max-heap)



    while len(max_heap) > 1:
        # Pop the two largest elements, remembering they are negative
        first = -heapq.heappop(max_heap)
        second = -heapq.heappop(max_heap)

        print(f'first:{first}, second: {second}')

        if first != second:
            # Push the difference back into the heap, negated to maintain max-heap property
            heapq.heappush(max_heap, -(first - second))


    # Check if there is any stone left
    if max_heap:
        return -max_heap[0]  # Return the last stone weight, revert the negation
    else:
        return 0


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))
