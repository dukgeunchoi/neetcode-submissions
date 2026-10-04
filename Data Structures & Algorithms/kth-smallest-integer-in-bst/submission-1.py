# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        def dfs(node, k):
            if not node: return

            dfs(node.left, k)
            self.nodes.append(node.val)
            dfs(node.right, k)
            return
        
        dfs(root, k)
        print(self.nodes)
        return self.nodes[k-1]