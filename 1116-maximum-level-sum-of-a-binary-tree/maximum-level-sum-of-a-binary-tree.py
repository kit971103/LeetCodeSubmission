# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = [root]
        max_level_idx = level_idx = 1
        max_level_sum = root.val

        while level:
            
            next_level =[]
            level_sum = 0
            
            for node in level:
                level_sum += node.val
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            if level_sum > max_level_sum: 
                max_level_sum = level_sum
                max_level_idx = level_idx
            level_idx+=1

            level = next_level.copy()
        
        return max_level_idx

        