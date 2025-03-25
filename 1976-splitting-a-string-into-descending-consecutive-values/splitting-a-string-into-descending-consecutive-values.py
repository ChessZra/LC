class Solution:
    def splitString(self, s: str) -> bool:
        N = len(s)
        int_s = int(s)
        def solve(index, prev):
            if index >= N:
                return prev != int_s
            
            cur = ""
            best = False
            for i in range(index, N):
                cur += s[i]
                int_cur = int(cur)
                if prev is None or (int_cur - prev == -1):
                    best |= solve(i + 1, int_cur)
            return best

        return solve(0, None)
