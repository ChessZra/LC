class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        INF = float('inf')
        fives = [5 ** i for i in range(10)]

        N = len(s)
        def dfs(index, bits):
            value = int(bits, 2)
            if value == 0:
                return INF

            # this doesnt ork because of python precision
            # cond = math.log(value, 5) == int(math.log(value, 5))
            cond = value in fives
            if index == N - 1:
                return 1 if cond else INF        

            best = INF
            if cond:
                best = min(best, 1 + dfs(index + 1, s[index + 1]))
            best = min(best, dfs(index + 1, bits + s[index + 1]))
            
            return best
        
        ans = dfs(0, s[0])
        if ans == INF:
            return -1
        return ans