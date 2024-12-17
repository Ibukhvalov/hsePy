"""
https://leetcode.com/problem-list/binary-tree/
url: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        Output = []
        Value = collections.deque([root])
        while Value:
            Inner = []
            for i in range(len(Value)):
                node = Value.popleft()
                Inner.append(node.val)
                if node.left:
                    Value.append(node.left)
                if node.right:
                    Value.append(node.right)
            Output.append(Inner)
        Final = []
        for i in range(len(Output)):
            if i % 2 != 0:
                Final.append(Output[i][::-1])
            else:
                Final.append(Output[i])
        return Final
