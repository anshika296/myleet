# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count=0
        ''' 1. Search left
          2. If answer found → return it
          3. Otherwise count current node
          4. If current node is kth → return it
          5. Search right'''
          #inorder traversal
        def dfs(root):
            nonlocal count
            if root is None:
                return None
            left=dfs(root.left)
            if left is not None:
                return left
            count+=1
            if count==k:
                return root.val
            return dfs(root.right)
        return dfs(root)