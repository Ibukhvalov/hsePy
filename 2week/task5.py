"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 1
        while i < len(path):
            j = 0
            slashFirstIndex = -1
            while i + j < len(path) and not (
                path[i + j] == "/"
                and (i + j + 1 >= len(path) or path[i + j + 1] != "/")
            ):
                if path[i + j] == "/" and slashFirstIndex == -1:
                    slashFirstIndex = i + j
                j += 1
            if slashFirstIndex == -1:
                slashFirstIndex = i + j

            current = path[i:slashFirstIndex]
            i = i + j + 1

            if current == ".":
                continue
            if current == "..":
                if len(stack) > 0:
                    stack.pop()
                continue
            if current != "":
                stack.append(current)

        if len(stack) == 0:
            return "/"

        answer = ""
        for file in stack:
            answer += "/" + file

        return answer
