# Given an integer array arr, return the length of a maximum size turbulent
# subarray of arr.

# A subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.


from typing import List

def maxTurbulenceSize(arr: List[int]) -> int:

    max_len = 1
    current_len = 1
    prev_comparison = ''

    for i in range(1, len(arr)):

        # determine comparison vor current iteration
        current_comparison = ''
        if arr[i - 1] < arr[i]:
            current_comparison = '>'
        elif arr[i - 1] > arr[i]:
            current_comparison = '<'
        else:
            current_comparison = ''


        # left == right, reset current len
        if current_comparison == '':
            current_len = 1
        # turbulent pattern, bump current len and try to update max len
        elif current_comparison != prev_comparison:
            current_len += 1
            max_len = max(max_len, current_len)
        # non turbulent pattern, reset current len to 2, since there are 2 non
        # equal elements, and their comparison was already saved
        else:
            current_len = 2

        # update global comparison
        prev_comparison = current_comparison

    return max_len


arr = [9,4,2,10,7,8,8,1,9] # 5

print(maxTurbulenceSize(arr))


arr = [4,8,12,16]
print(maxTurbulenceSize(arr)) # 2
