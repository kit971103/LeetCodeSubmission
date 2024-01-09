# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def leafvaluesequence(node: TreeNode) -> list[int]:
            if not node: return []
            if not node.left and not node.right: return [node.val]
            return leafvaluesequence(node.left) + leafvaluesequence(node.right)
        return leafvaluesequence(root1)==leafvaluesequence(root2)