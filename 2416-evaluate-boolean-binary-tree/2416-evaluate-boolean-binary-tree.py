# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root):
        if not root:
            return False
        
        # Leaf node
        if not root.left and not root.right:
            return bool(root.val)
        
        # Evaluate left and right subtrees
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        # Apply OR or AND
        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val

        