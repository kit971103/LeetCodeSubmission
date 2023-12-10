# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            pass
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left =  self.deleteNode(root.left, key)
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ_parent, succ = root, root.right
            
            while succ.left is not None:
                succ_parent = succ
                succ = succ.left
            
            if succ_parent!= root:
                succ_parent.left = succ.right
            else:
                succ_parent.right = succ.right
            
            root.val = succ.val

            del succ
        return root


            
        