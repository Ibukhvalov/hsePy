"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/group-anagrams/description/
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagramSet = set()
        anagramDict = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagramSet:
                anagramDict[sorted_word] = list()

            anagramSet.add(sorted_word)
            anagramDict[sorted_word].append(word)
        return [anagramDict[key] for key in anagramSet]
