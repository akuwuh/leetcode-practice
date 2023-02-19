# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        q = deque()
        q.append((root, 0))
        is_reverse = False
        
        while q:
            level_nodes = []
            level_size = len(q)
            
            for i in range(level_size):
                node, level = q.popleft()
                level_nodes.append(node.val)
                
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            
            if is_reverse:
                level_nodes.reverse()
            
            ans.append(level_nodes)
            is_reverse = not is_reverse
        
        return ans
            
            