class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        def is_prime(x):
            if x == 1: return False
            for i in range(2, int(x ** 0.5) + 1):
                if (i * (x // i)) == x:
                    return False
            return True

        R, C = len(mat), len(mat[0])
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        f = collections.Counter()
        path = 0
        def dfs(r, c, d):
            nonlocal path
            if r < 0 or c < 0 or r >= R or c >= C:
                return

            path *= 10
            path += mat[r][c]

            if path > 10 and is_prime(path):
                f[path] += 1

            dfs(r + directions[d][0], c + directions[d][1], d)
        
        for r in range(R):
            for c in range(C):
                for d in range(len(directions)):
                    path = 0
                    dfs(r, c, d)
        
        #print(f)
        if len(f.values()) == 0:
            return -1

        max_freq = max(f.values())
        res = -1
        for k, v in f.items():
            if v == max_freq:
                res = max(res, k)
       
        return res