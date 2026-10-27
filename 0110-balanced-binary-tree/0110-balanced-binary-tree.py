# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
            
        def treeHeight(root: TreeNode | None) -> int:
            if root is None:
                return 0
            return max(treeHeight(root.left), treeHeight(root.right)) + 1
        
        if abs(treeHeight(root.left) - treeHeight(root.right)) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
