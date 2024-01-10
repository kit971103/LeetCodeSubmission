# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def find_in(node):
            nonlocal target
            nonlocal path
            nonlocal found

            if not node or found:
                return
            
            if node.val == start:
                target = path.copy()
                found = True
                return
            
            path.append("L")
            find_in(node.left)
            path.pop()
            
            path.append("R")
            find_in(node.right)
            path.pop()

        path = ["T"]
        target = None
        found = False
        find_in(root)

        def dfs(node):

            if not node:
                return
            
            if not node.left and not node.right:
                nonlocal res
                i = 0
                for a,b in zip(target, path):
                    if a == b: 
                        i+=1
                    else:
                        break
                res = max(res, len(target) + len(path) - 2*i)
            
            path.append("L")
            dfs(node.left)
            path.pop()

            path.append("R")
            dfs(node.right)
            path.pop()
        
        path = ["T"]
        res=0
        dfs(root)

        return max(res, len(target)-1) #len(target)-1 repersent the depth of start node





