# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.



class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left-=1
                right+=1


            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left-=1
                right+=1

        return count


sol = Solution()


s = "abc"
print(sol.countSubstrings(s)) # 3


s = "aaa"
print(sol.countSubstrings(s)) # 6
