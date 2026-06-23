# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def postOrder(self, node: Optional[TreeNode]):
        if node is None: return
        temp = node.left
        node.left = node.right
        node.right = temp
        self.postOrder(node.left)
        self.postOrder(node.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.postOrder(root)
        return root
