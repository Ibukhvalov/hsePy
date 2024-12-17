"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""


class Solution:
    def buildTreeRecursive(self, inorder, postorder):
        if not postorder or not inorder:
            return None
        val = postorder.pop()
        index = inorder.index(val)
        return TreeNode(
            val=val,
            right=self.buildTreeRecursive(inorder[index + 1 :], postorder),
            left=self.buildTreeRecursive(inorder[0:index], postorder),
        )

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None
        return self.buildTreeRecursive(inorder, postorder)
