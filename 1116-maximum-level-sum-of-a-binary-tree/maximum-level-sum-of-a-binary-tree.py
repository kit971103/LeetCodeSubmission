# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        level = deque([root])
        max_level_idx = level_idx = 1
        max_level_sum = root.val

        while level:
            
            length = len(level)
            level_sum = 0
            
            for _ in range(length):
                node = level.popleft()
                level_sum += node.val
                if node.left: level.append(node.left)
                if node.right: level.append(node.right)
            
            if level_sum > max_level_sum: 
                max_level_sum = level_sum
                max_level_idx = level_idx
            level_idx+=1
        
        return max_level_idx

        