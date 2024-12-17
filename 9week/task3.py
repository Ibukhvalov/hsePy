"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build_bt_helper(
            preorder,
            inorder,
            left_inorder_index,
            right_inorder_index,
            preorder_index,
            mapping,
        ):
            if left_inorder_index > right_inorder_index:
                return
            curr_val = preorder[preorder_index[0]]
            preorder_index[0] += 1
            root = TreeNode(curr_val)
            if left_inorder_index == right_inorder_index:
                return root
            curr_val_index = mapping[curr_val]
            root.left = build_bt_helper(
                preorder,
                inorder,
                left_inorder_index,
                curr_val_index - 1,
                preorder_index,
                mapping,
            )
            root.right = build_bt_helper(
                preorder,
                inorder,
                curr_val_index + 1,
                right_inorder_index,
                preorder_index,
                mapping,
            )
            return root

        def build_bt(preorder, inorder):
            preorder_index = [0]
            mapping = {}
            for i in range(0, len(inorder)):
                mapping[inorder[i]] = i
            return build_bt_helper(
                preorder, inorder, 0, len(inorder) - 1, preorder_index, mapping
            )

        return build_bt(preorder, inorder)
