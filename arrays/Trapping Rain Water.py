# Given n non-negative integers representing an elevation map
# where the width of each bar is 1, compute how much water
# it can trap after raining.


from typing import List

def trap(height: List[int]) -> int:

    trapped = 0

    # for each point we want to obtain its highest left/right border
    left_highs:List[int] = []
    right_highs:List[int] = []

    # obtain left highs
    for i in height:
        if len(left_highs) == 0:
            left_highs.append(0)
        else:
            left_highs.append(max(left_highs[-1], i))

    # obtain right highs
    for i in reversed(height):
        if len(right_highs) == 0:
            right_highs.append(0)
        else:
            right_highs.append(max(right_highs[-1], i))
    # reverse back right high
    right_highs = list(reversed(right_highs))

    # pick the smaller of side highs and decrement the element val, ignoring negative vals
    for i in range(len(height)):
        trapped += max(0, min(left_highs[i], right_highs[i]) - height[i])


    return trapped

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height)) # 6


# height = [4,2,0,3,2,5]
# trap(height) # 9
