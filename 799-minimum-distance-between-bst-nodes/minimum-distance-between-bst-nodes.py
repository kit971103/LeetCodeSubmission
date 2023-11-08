# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        alist = []
        def dfs_Inorder(node):
            if node.left: dfs_Inorder(node.left)
            alist.append(node.val)
            if node.right: dfs_Inorder(node.right)
        dfs_Inorder(root)
        min_diff = alist[1] - alist[0]
        for a, b in itertools.pairwise(alist):
            if (b-a) < min_diff: min_diff = b-a
        return min_diff
