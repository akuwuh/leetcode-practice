# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node, l):
            if not node:
                return
            
            l.append(node.val)

            if node.left:
                dfs(node.left, l)
            if node.right:
                dfs(node.right, l)
            return l
        
        l = dfs(root, [])
        l.sort()

        ans = 100000

        for i in range(1,len(l)):
            ans = min(ans, l[i] - l[i-1])
        
        return ans

