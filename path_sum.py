from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, node: Optional[TreeNode], target: int) -> bool:
        if not node:
            return False

        target -= node.val

        if not node.left and not node.right:
            return target == 0

        return (
            self.hasPathSum(node.left, target)
            or self.hasPathSum(node.right, target)
        )


# [1,2,3,4,null,null,5]
tree = TreeNode(1)
node1 = TreeNode(2)
tree.left = node1
node3 = TreeNode(3)
tree.right = node3
node4 = TreeNode(4)
tree.left.left = node4
node5 = TreeNode(5)
tree.right.right = node5

solution = Solution()
print(solution.hasPathSum(tree, 9))
