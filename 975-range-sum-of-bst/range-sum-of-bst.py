# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        res = 0
        while stack:
            if stack[-1] is None:
                stack.pop()
                continue
            node = stack.pop()
            if low <= node.val <= high:
                res += node.val
                stack.append(node.left)
                stack.append(node.right)
            elif node.val < low:
                stack.append(node.right)
            else:
                stack.append(node.left)
        return res

        