# You are given a string s and an integer k. You can choose any character
# of the string and change it to any other uppercase English character.
# You can perform this operation at most k times.

# Return the length of the longest substring containing the same
# letter you can get after performing the above operations.


from typing import Dict

def characterReplacement(s: str, k: int) -> int:

    counts:Dict[str,int] = {}
    max_substring = 0

    # pointer used for 'popping' values from the 'tail'
    LEFT = 0

    for RIGHT in range(len(s)):
        current_char = s[RIGHT]

        # each iteration will update frequency of encountered char
        if current_char in counts:
            counts[current_char] += 1
        else:
            counts[current_char] = 1


        window_len = RIGHT - LEFT + 1
        max_occurrence = max(list(counts.values()))

        # check if window is valid,
        # ie can we make enough replacements to make it valid
        # if valid try update max
        if window_len - max_occurrence <= k:
            max_substring = max(max_substring, window_len)
        # if we dont have enough replacements to make window valid
        # 'pop' tail value
        else:
            counts[s[LEFT]] -= 1
            LEFT += 1



    return max_substring

s = "AABABBA"
k = 1
print(characterReplacement(s,k)) # 4


s = "ABAB"
k = 2
print(characterReplacement(s,k)) # 4

s = "ABBB"
k = 2
print(characterReplacement(s,k)) # 4


s = "ABAA"
k = 0
print(characterReplacement(s,k)) # 2
