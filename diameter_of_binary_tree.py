from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0  # variable to store the maximum diameter found so far

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # update ans if new diameter is found
            self.ans = max(self.ans, left + right)
            # return the maximum height of the node
            return max(left, right) + 1

        dfs(root)
        return self.ans


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
print(solution.diameterOfBinaryTree(tree))
