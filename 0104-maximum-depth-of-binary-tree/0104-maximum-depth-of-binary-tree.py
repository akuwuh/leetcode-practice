# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, height):
            return max(dfs(node.left,height + 1),dfs(node.right, height+1)) if node else height
        return dfs(root, 0)