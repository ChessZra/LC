class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        res = '9' * (N + 1)

        used = []
        def dfs(index):
            if len(used) == N + 1:
                nonlocal res
                res = min(res, ''.join(used))
                return 
            
            for char in "123456789":
                if char in used:
                    continue

                if pattern[index] == 'I':
                    if used and char < used[-1]:
                        continue
                if pattern[index] == 'D':
                    if used and char > used[-1]:
                        continue

                used.append(char)
                dfs(index + 1)
                used.pop()
        
        for char in "123456789":
            used.clear()
            used = [char]
            dfs(0)
        return res