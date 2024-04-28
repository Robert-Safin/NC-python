# Koko loves to eat bananas. There are n piles of bananas, the ith pile
# has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, she eats all of them instead
# and will not eat any more bananas during this hour.

# Koko likes to eat slowly but still wants to finish eating all the
# bananas before the guards return.

# Return the minimum integer k such that she can eat all the bananas
# within h hours.

from typing import List
from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:

    # left logically can not be less than 1
    # max(piles) is the biggest k that will solve in h hours
    left = 1
    right = max(piles)

    while left <= right:
        mid_val = (left + right) // 2

        # calc hours(k) to get through piles
        hours_taken = 0
        for pile in piles:
            hours_taken += ceil(pile/mid_val)

        # calculated k is does eat all piles in less/equal to h
        # but need to investigate smaller k options
        # exclude right side and keep current k
        if hours_taken <= h:
            right = mid_val - 1
        # calculated k is too large (can not eat all piles in h hours)
        # exclude left side (smaller Ks) and keep current k
        else:
            left = mid_val + 1
    # when while left <= right loop exists last left value is best k
    return left





piles = [3,6,7,11]
h = 8
print(minEatingSpeed(piles,h))
