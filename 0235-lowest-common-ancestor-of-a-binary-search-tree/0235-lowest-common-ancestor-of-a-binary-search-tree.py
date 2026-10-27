# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def searchRoot(current_root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if (current_root.val > p.val) and (current_root.val > q.val):
                return searchRoot(current_root.left, p, q)
            elif (current_root.val < p.val) and (current_root.val < q.val):
                return searchRoot(current_root.right, p, q)
            else:
                return current_root

        return searchRoot(root, p, q)