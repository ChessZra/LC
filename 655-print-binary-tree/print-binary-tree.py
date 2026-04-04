# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def get_height(root):
            if not root:
                return 0
            return 1 + max(get_height(root.left), get_height(root.right))
        H = get_height(root)
        R, C = H, 2 ** H - 1
        res = [[""] * C for _ in range(R)]
        def traverse(root, r, c):
            if not root:
                return
            res[r][c] = str(root.val)
            traverse(root.left, r + 1, c - 2**(H - r - 2))
            traverse(root.right, r + 1, c + 2**(H - r - 2))
        traverse(root, 0, C // 2)
        return res