"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""


class Solution(object):
    def levelOrderBottom(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            curr_level = []
            next_level = []
            for node in queue:
                curr_level.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            result.insert(0, curr_level)
            queue = next_level

        return result
