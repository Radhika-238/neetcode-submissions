# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, root1, root2):
        if root1 and not root2:
            return False
        if root2 and not root1:
            return False
        
        if root1 and root2:
            if root1.val != root2.val:
                return False
        else:
            return True
        
        result = self.isSameTree(root1.left, root2.left)
        if result == False:
            return False
        result = self.isSameTree(root1.right, root2.right)
        if result == False:
            return False
        
        return True


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot and not root:
            return False
        if not subRoot and root:
            return True
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)