# Given an array of integers arr and two integers k and threshold,
# return the number of sub-arrays of size k and average greater than
# or equal to threshold.
from typing import List,Deque
from collections import deque

def numOfSubarrays(arr: List[int], k: int, threshold: int) -> int:

    count = 0
    running_sum = 0

    for i in range(0,len(arr)):
        # add the current element to the running sum
        running_sum += arr[i]


        # check if we have k elements in the window
        if i >= k-1:
            # check if more than k elements in the window,
            # then remove the first element from the window
            if i >= k:
                running_sum -= arr[i-k]
            # if the average is greater than or equal to threshold
            if running_sum / k >= threshold:
                count += 1

    return count




arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

numOfSubarrays(arr,k,threshold) # 3


arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

numOfSubarrays(arr,k,threshold) # 6
