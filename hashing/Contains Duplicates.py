
from typing import List,Dict

def containsDuplicate(nums: List[int]) -> bool:
    hash:Dict[int,int] = {}

    for v in nums:
        if v in hash:
            return True
        else:
            hash[v] = 1

    return False



nums = [4,2,3,1]
print(containsDuplicate(nums))
