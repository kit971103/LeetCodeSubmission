# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, path):
            # nonlocal targetSum
            # nonlocal target
            nonlocal count
            path = path + [node.val] # implictly created a new copy
            # path.append(node.val) # cant work, need a new copy of path for each path
            # print(f"{node.val=}, {path=}")
            pathsum = 0
            n= len(path)
            for i in range(n):
                pathsum += path[n-1-i]
                if pathsum == targetSum: count+=1
            if node.left: dfs(node.left, path)
            if node.right: dfs(node.right, path)



        # target = targetSum
        count = 0
        if root: dfs(root, [])
        return count