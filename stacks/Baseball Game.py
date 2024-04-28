# You are given a list of strings operations, where operations[i] is
# the ith operation you must apply to the record and is one of the following:
# where
# int => push to stack
# + => sum last 2 ints in stack and push the sum to stack
# D => double last stack value and push the product to stack
# C => pop last stack value
from typing import List
def calPoints(operations: List[str]) -> int:

    stack:List[int] = []

    for op in operations:
        match op:
            case '+':
                last_val = stack[-1]
                second_last_val = stack[-2]
                current_sum = last_val + second_last_val
                stack.append(current_sum)
            case 'D':
                last_val = stack[-1]
                double = last_val * 2
                stack.append(double)
            case 'C':
                stack.pop()
            case _:
                stack.append(int(op))

    return sum(stack)

print(calPoints(["5","2","C","D","+"]))
