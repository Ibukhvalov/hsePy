"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/description/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = 0
        k = 0
        start = 0
        for i, c in enumerate(s):
            if c == "(":
                k += 1
            else:
                k -= 1

            if k < 0:
                k = 0
                start = i + 1
            elif k == 0:
                ans = max(ans, i - start + 1)
        start = 0
        k = 0
        for i, c in enumerate(s[::-1]):
            if c == "(":
                k -= 1
            else:
                k += 1
            if k < 0:
                k = 0
                start = i + 1
            elif k == 0:
                ans = max(ans, i - start + 1)

        return ans
