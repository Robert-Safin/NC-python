
from typing import Dict

def characterReplacement(s: str, k: int) -> int:
    left = 0
    max_length = 0
    max_count = 0

    counts:Dict[str,int] = {}

    for right in range(len(s)):
        counts[s[right]] = counts.get(s[right], 0) + 1
        max_count = max(max_count, counts[s[right]])

        # Check if we need to shrink the window
        if (right - left + 1) - max_count > k:
            counts[s[left]] -= 1
            left += 1

        # Calculate the max length of the substring
        max_length = max(max_length, right - left + 1)

    return max_length
