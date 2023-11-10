# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, path_sum):
            
            path_sum += node.val
            path.append(node.val)
            
            if not node.left and not node.right:
                if path_sum == targetSum: res.append(path.copy())
            else:
                if node.left: dfs(node.left, path_sum)
                if node.right: dfs(node.right, path_sum)

            path_sum -= node.val
            path.pop()

        path = []
        res = []
        if root: dfs(root, 0)
        return res
        