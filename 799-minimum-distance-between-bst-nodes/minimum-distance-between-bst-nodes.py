# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        alist = []
        queue = [root]
        while queue:
            node = queue.pop()
            alist.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        alist.sort()
        min_diff = alist[1] - alist[0]
        for a, b in itertools.pairwise(alist):
            if (diff:=b-a) < min_diff: min_diff = diff
        return min_diff
