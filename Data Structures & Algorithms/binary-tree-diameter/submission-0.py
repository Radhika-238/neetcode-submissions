# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def solve (root):
            nonlocal diameter
            if root == None:
                return 0
            left_height = solve(root.left)
            right_height = solve(root.right)
            diameter = max(diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        solve(root)
        return diameter