"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-pattern/description/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lettersIndexSet = {}
        curLen = 0
        maxLen = 0

        for i, letter in enumerate(s):
            
            if(letter in lettersIndexSet):
                for l in s[i-curLen : lettersIndexSet[letter]]:
                    del lettersIndexSet[l]
                curLen = i - lettersIndexSet[letter]
            else:
                curLen+=1
                maxLen = max(curLen, maxLen)

            lettersIndexSet[letter] = i

        return maxLen
        