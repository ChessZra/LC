class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        stk = [(-1, -1)]
        prefix = [None] * N
        for i in range(N):
            while stk[-1][0] >= nums[i]:
                stk.pop()
            prefix[i] = stk[-1][1]
            stk.append((nums[i], i))
        
        suffix = [None] * N
        stk = [(-1, N)]
        for i in range(N - 1, -1, -1):
            while stk[-1][0] >= nums[i]:
                stk.pop()
            suffix[i] = stk[-1][1]
            stk.append((nums[i], i))

        f = collections.defaultdict(set)
        for i in range(N):
            f[nums[i]].add((prefix[i], suffix[i]))

        res = 0
        for k, v in f.items():
            if k == 0: continue
            res += len(v)
        return res