# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        layer = [root]
        res = []

        while layer:
            res.append(layer[-1].val)
            next_layer = []
            for node in layer:
                if node.left: next_layer.append(node.left)
                if node.right: next_layer.append(node.right)
            layer = next_layer.copy()
        return res
            
            

        