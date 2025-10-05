# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            current = (current << 1) | node.val  # build binary number
            if not node.left and not node.right:  # leaf
                return current
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)

        