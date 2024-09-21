"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/decode-ways/description/
"""

def canDecode(x: str) -> bool:
    if 0 < int(x) <= 26 and x[0] != '0':
        return True
    return False

class Solution(object):
    def numDecodings(self, s: str) -> int:
        numsOfWays = [0 for _ in range(len(s))]

        if canDecode(s[0]):
            numsOfWays[0] = 1

        for i in range(1, len(s)):
            if i>0 and canDecode(s[i-1]+s[i]):
                numsOfWays[i] += numsOfWays[i-2]
                if i-2 < 0:
                    numsOfWays[i] += 1
            if i>0 and canDecode(s[i]):
                numsOfWays[i] += numsOfWays[i-1]

        return numsOfWays[len(s)-1]



solution = Solution()
print(solution.numDecodings(input()))