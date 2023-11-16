# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node) -> tuple:
            
            if not node: return (False, False)
            
            p_in_this = q_in_this = False
            p_in_L_subtree, q_in_L_subtree = dfs(node.left)
            p_in_R_subtree, q_in_R_subtree = dfs(node.right)

            if node == p or p_in_L_subtree or p_in_R_subtree: 
                p_in_this = True
            if node == q or q_in_L_subtree or q_in_R_subtree: 
                q_in_this = True
            
            nonlocal CommonAncestor
            if p_in_this and q_in_this and CommonAncestor is None: 
                CommonAncestor = node
            
            return (p_in_this, q_in_this)




            

            
        CommonAncestor = None
        dfs(root)
        
        return CommonAncestor

