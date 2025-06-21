class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        res = []
        target_size = 2 ** n
        path = [start]
        seen = set([start])
        def dfs():
            nonlocal res
            if res:
                return
            if len(path) == target_size:
                # check if cur[0] and cur[-1] at most one
                diffs = 0
                for i in range(n):
                    if (path[-1] & (1 << i)) != (path[0] & (1 << i)):
                        diffs += 1
                
                if diffs == 1:
                    res = path.copy()
                return

            for i in range(n):
                one_diff = path[-1] ^ (1 << i)
                if one_diff not in seen:
                    seen.add(one_diff)
                    path.append(one_diff)
                    dfs()
                    path.pop()  
                    seen.remove(one_diff)
        dfs()
        return res
                