# You are a product manager and currently leading a team to develop a new
# product. Unfortunately, the latest version of your product fails the
# quality check. Since each version is developed based on the previous
# version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out
# the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which returns whether
# version is bad. Implement a function to find the first bad version.
# You should minimize the number of calls to the API.


def firstBadVersion( n: int) -> int:
    # init pointer for first v and last v
    left = 1
    right = n

    while left < right:
        mid = (left + right) // 2
        if isBadVersion(mid):
            # cut right side including mid value
            right = mid
        else:
            # cut left side but keep mid value
            left = mid + 1
    # Since left == right, it points to the first bad version
    return left





def isBadVersion(v:int) -> bool:
    if v < 1:
        raise Exception("NEGATIVE VERSION")
    if v in range(1,4):
        return False
    else:
        return True


print(firstBadVersion(5))
