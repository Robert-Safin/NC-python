# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

from typing import Tuple, List

# Can be solved with using 2 stack ([node_value] + [smallest_value])
class MinStack:
    def __init__(self):
        # (node_value, smallest_value_in_stack)
        self.values:List[Tuple[int,int]] = []

    def push(self, val: int) -> None:
        # handle pushing to empty stack
        if len(self.values) == 0:
            self.values.append((val,val))
        else:
            last_min = self.values[-1][-1]
            # set new lowest node
            if val < last_min:
                self.values.append((val,val))
            # keep old smallest node
            else:
                self.values.append((val,last_min))

    def pop(self) -> None:
        self.values.pop()


    def top(self) -> int:
        return self.values[-1][0]


    def getMin(self) -> int:
        return self.values[-1][1]
