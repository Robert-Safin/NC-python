# You are given an integer array height of length n. There are n
# vertical lines drawn such that the two endpoints of the ith line are
# (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container,
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

from typing import List

def maxArea(height: List[int]) -> int:

    largest_volume = 0

    LEFT = 0
    RIGHT = len(height) - 1

    while LEFT < RIGHT:

        # calc volume shortest wall * length of container
        current_volume = min(height[LEFT], height[RIGHT]) * (RIGHT - LEFT)

        # try to update container
        largest_volume = max(largest_volume, current_volume)

        # bump the shorter wall
        if height[LEFT] < height[RIGHT]:
            LEFT += 1
        else:
            RIGHT -= 1

    return largest_volume



height = [1,8,6,2,5,4,8,3,7]
maxArea(height) #49


height = [1,1]
maxArea(height) #1
