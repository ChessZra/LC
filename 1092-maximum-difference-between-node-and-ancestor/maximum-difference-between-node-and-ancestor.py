# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        INF = 10 ** 20
        
        best = 0
        def solve(node):
            if not node:
                return (INF, -INF)


            left_mn, left_mx = solve(node.left)
            right_mn, right_mx = solve(node.right)

            mn, mx = min(left_mn, right_mn, node.val), max(left_mx, right_mx, node.val)

            nonlocal best
            best = max(best, abs(node.val - mn), abs(node.val - mx))

            return (mn, mx)

        solve(root)
        return best