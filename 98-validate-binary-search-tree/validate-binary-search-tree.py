# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        INF = float('inf')
        good = True

        @cache
        def dfs(root):
            if not root:
                return (INF, -INF)

            mn_left, mx_left = dfs(root.left)
            mn_right, mx_right = dfs(root.right)

            if mx_left >= root.val or mn_right <= root.val:
                nonlocal good
                good = False

            return (min([mn_left, mn_right, root.val]), max(mx_left, mx_right, root.val))

        dfs(root)
        return good