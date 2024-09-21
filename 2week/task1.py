"""
leetcode.com/problem-list/string/
https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
"""


from string import ascii_lowercase


class WordDictionary:

    def __init__(self):
        self.words = set()

    def addWord(self, word: str) -> None:
        self.words.add(word)

    def search(self, word: str) -> bool:
        if ('.' in word):
            for c in ascii_lowercase:
                wordFixed = word.replace('.', c, 1)
                if ('.' in wordFixed):
                    for d in ascii_lowercase:
                        if (wordFixed.replace('.', d) in self.words):
                            return True
                else:
                    if wordFixed in self.words:
                        return True
        return word in self.words
