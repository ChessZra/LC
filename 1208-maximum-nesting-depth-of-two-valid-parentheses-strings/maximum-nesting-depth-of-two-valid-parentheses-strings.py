class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:

        stk = []
        N = len(seq)
        res = [None] * N
        for i in range(N):
            if seq[i] == '(':
                if stk:
                    stk.append((i, 1 - stk[-1][1]))
                else:
                    stk.append((i, 0))
            else:
                res[i] = stk[-1][1]
                res[stk[-1][0]] = stk[-1][1]

                stk.pop()
        return res