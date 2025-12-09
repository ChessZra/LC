class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7
        N = len(nums)
        res = [1] * N
        left = collections.Counter()
        right = collections.Counter()
        left[nums[0]] += 1
        right[nums[N-1]] += 1
        for i in range(1, N - 1):
            res[i] *= left[nums[i] * 2]    
            left[nums[i]] += 1
        for i in range(N - 2, 0, -1):
            res[i] *= right[nums[i] * 2]
            right[nums[i]] += 1 
        return sum(res[1:N-1]) % MOD