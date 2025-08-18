# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def encode_parent_dfs(root, prev):
            if not root:
                return            
            root.parent = prev
            encode_parent_dfs(root.left, root)
            encode_parent_dfs(root.right, root)
        encode_parent_dfs(root, None)
        def get_all_leaves(root, arr):
            if not root:
                return
            if root.val == target and not root.left and not root.right:
                arr.append(root)
                return
            get_all_leaves(root.left, arr)
            get_all_leaves(root.right, arr)
        leaves = []
        get_all_leaves(root, leaves)
        empty_flag = False
        def delete_traversal(leaf):
            if leaf.left or leaf.right or leaf.val != target:
                return # not a leaf
            if leaf.parent is None: # remove the root
                nonlocal empty_flag
                empty_flag = True
                return
            if leaf.parent.left == leaf:
                leaf.parent.left = None
            elif leaf.parent.right == leaf:
                leaf.parent.right = None
            delete_traversal(leaf.parent)
        for leaf in leaves:
            delete_traversal(leaf)
        return root if not empty_flag else None