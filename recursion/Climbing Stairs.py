# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?


def climbStairs(n: int) -> int:

    # edge cases
    if n == 1:
        return 1
    elif n == 2:
        return 2

    # Initialize pointers with base case values, ie. with n=1 => 1 and with n=2 => 2
    # the pointers will summed and shifted right.
    left = 1
    right = 2

    # calculate range for number of steps excluding base cases
    for i in range(3, n + 1):
        # sum pointers
        current = right + left
        # shift left
        left = right
        # shift right
        right = current
    # rightmost value
    return right



# Dynamic with extra mem allocation O(N)
# def climbStairs(n: int) -> int:
#     mem = [0 for i in range(0, n + 1) ]
#     mem[-1] = 1
#     mem[-2] = 1


#     for i in range(3, n + 2):
#         mem[-i] = mem[-i + 1] + mem[-i + 2]


#     return mem[0]





# BRUTE FORCE O(^n)
# def climbStairs(n: int) -> int:

#     if n < 0:
#         return 0

#     if n == 0:
#         return 1

#     return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(5)) # 5 => 8 out
