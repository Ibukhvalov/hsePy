"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/
"""


def round(x: int) -> int:
    if x < -(2**31):
        return -(2**31)
    if x > 2**31 - 1:
        return 2**31 - 1
    return x


class Solution:
    def myAtoi(self, s: str) -> int:
        i = -1
        while i + 1 < len(s) and s[i + 1] == " ":
            i += 1

        sign = 1
        if i + 1 < len(s) and s[i + 1] in "-+":
            if s[i + 1] == "-":
                sign = -1
            i += 1
        result = 0
        while i + 1 < len(s) and s[i + 1].isdigit():
            i += 1
            result = result * 10 + int(s[i])

        return round(result * sign)
