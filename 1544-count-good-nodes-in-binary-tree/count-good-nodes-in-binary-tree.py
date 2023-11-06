# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, path_max):
            nonlocal count
            if node.val >= path_max: count += 1
            if node.val >= path_max: path_max = node.val
            if node.left: dfs(node.left, path_max)
            if node.right: dfs(node.right, path_max)
            
        count = 0
        dfs(root, root.val)
        return count