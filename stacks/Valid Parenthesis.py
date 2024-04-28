# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
from typing import List

def isValid(s: str) -> bool:
    stack:List[str] = []

    # Will be used to compare closing bracket to opening bracket
    map = {
            ")":"(",
            "}":"{",
            "]":"[",
                    }


    for c in list(s):
        # We push only opening brackets to the stack
        if c not in map:
            stack.append(c)
        # if stack is empty this means we have an orphan closing bracket.
        elif len(stack) == 0:
            return False
        # invalid pairing.
        elif map[c] != stack[-1]:
            return False
        # we found a valid closing bracket for stack's opening bracket, we pop it.
        else:
            stack.pop()

    # if something is left, we have have orphan opening brackets.
    if len(stack) == 0 :
        return True
    else:
        return False



print(isValid('){'))
