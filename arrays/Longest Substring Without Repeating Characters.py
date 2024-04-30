# Given a string s, find the length of the longest substring without
# repeating characters.

from typing import Set

def lengthOfLongestSubstring(s: str) -> int:

    charSet:Set[str] = set()
    LEFT = 0
    max_substring = 0

    for RIGHT in range(len(s)):

        # before trying to add RIGHT digit, check if it is already in set
        # if it is pop LEFT char until RIGHT digit doesn't exist in set
        while s[RIGHT] in charSet:
            charSet.remove(s[LEFT])
            LEFT += 1

        # add RIGHT digit
        charSet.add(s[RIGHT])

        # try to update max
        max_substring = max(max_substring, RIGHT - LEFT + 1)

    return max_substring



s = "pwwkew"
print(lengthOfLongestSubstring(s))
