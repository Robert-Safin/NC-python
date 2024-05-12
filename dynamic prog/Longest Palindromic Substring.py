
class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0
        length = 0


        for i in range(len(s)):


            left = i
            right = i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                inner_length = right-left + 1

                if inner_length > length:
                    length = inner_length
                    start = left
                    end = right

                left -= 1
                right += 1



            left = i
            right = i+1

            while left >= 0 and right < len(s) and s[left] == s[right]:
                inner_length = right-left + 1

                if inner_length > length:
                    length = inner_length
                    start = left
                    end = right

                left -= 1
                right += 1

        return s[start:end+1]





sol = Solution()


s = "babad"
print(sol.longestPalindrome(s)) # "bab"

# s = "cbbd"
# print(sol.longestPalindrome(s)) # "bb"
