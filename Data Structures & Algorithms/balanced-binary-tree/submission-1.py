# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = 1

        def solve(root):
            if root == None:
                return 0 
            left = solve(root.left)
            if left == -1:
                return -1
            right = solve(root.right)
            if right == -1:
                return -1

            if (left - right) not in [-1, 0, 1]:
                return -1

            return 1 + max(left, right)
        
        result = solve(root)
        return False if result == -1 else True