from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root


tree = TreeNode(1)
node1 = TreeNode(2)
tree.left = node1
node3 = TreeNode(3)
tree.right = node3
node4 = TreeNode(4)
tree.left.left = node4
node4 = TreeNode(5)
tree.left.right = node4
node5 = TreeNode(6)
tree.right.left = node5
node5 = TreeNode(7)
tree.right.right = node5

solution = Solution()
print(solution.invertTree(tree))
