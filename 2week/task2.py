"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution:

    def generateParenthesis(self, n: int) -> list[str]:
        ans = []
        def generateWays(path: str, v: int):
            if v < n:
                return
            if len(path) == n * 2:
                if v == n:
                    ans.append(path)
                return

            generateWays(path + "(", v + 1)
            generateWays(path + ")", v - 1)

        generateWays("", n)
        return ans