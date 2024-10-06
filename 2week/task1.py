"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            j = 0
            while (
                i - j - 1 >= 0 and i + j + 1 < len(s) and s[i - j - 1] == s[i + j + 1]
            ):
                j += 1
            if 2 * j + 1 > len(ans):
                ans = s[i - j : i + j + 1]
            if i < len(s) - 1 and s[i] == s[i + 1]:
                j = 0
                while (
                    i - (j + 1) >= 0
                    and i + 2 + j < len(s)
                    and s[i - j - 1] == s[i + 2 + j]
                ):
                    j += 1
                if j * 2 + 2 > len(ans):
                    ans = s[i - j : i + 1 + j + 1]

        return ans
