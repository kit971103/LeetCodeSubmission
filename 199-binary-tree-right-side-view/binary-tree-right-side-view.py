# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        layer = deque([root])
        res = []

        while layer:
            res.append(layer[-1].val)
            level_length = len(layer)
            for _ in range(level_length):
                node = layer.popleft()
                if node.left: layer.append(node.left)
                if node.right: layer.append(node.right)
        return res
            
            

        