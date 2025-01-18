class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        N = len(parents)
        roots = [Node(x) for x in range(N)]

        # Create the tree from parents
        for child in range(1, N):
            parent = roots[parents[child]]
            if parent.left is None:
                parent.left = roots[child]
            else:
                parent.right = roots[child]
        
        @cache
        def get_size(node):
            if node is None:
                return 0
            return 1 + get_size(node.left) + get_size(node.right)

        f = collections.Counter() # score: frequency
        def dfs(node):
            if node is None:
                return
            
            l, r = get_size(node.left), get_size(node.right)
            p = N - r - l - 1
            f[max(1, l) * max(1, r) * max(1, p)] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(roots[0])

        return f[max(f.keys())]