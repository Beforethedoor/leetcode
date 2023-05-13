from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        min_depth = 1
        que = deque([node])

        while node:
            length = len(que)
            for _ in range(length):
                # we take first element in list!
                cur_node = que.popleft()
                if not cur_node.left and not cur_node.right:
                    return min_depth
                if cur_node.left:
                    # we append in end of list
                    que.append(cur_node.left)
                if cur_node.right:
                    # we append in end of list
                    que.append(cur_node.right)
            min_depth += 1
        return min_depth


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

sol = Solution()

print(sol.minDepth(tree))
