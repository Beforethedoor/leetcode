from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node):
            nonlocal result

            if not node:
                return 0, 0

            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            s = node.val + left_sum + right_sum
            c = 1 + left_count + right_count

            if s // c == node.val:
                result += 1

            return s, c

        traverse(root)
        return result


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

print("""
    Tree:
    -----------------------
    |           1         |
    |        /    \       |
    |      2        3     |
    |    /   \     /  \   |
    |  4       5  6    7  |
    -----------------------
""")

solution = Solution()
print(solution.averageOfSubtree(tree))
