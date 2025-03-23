class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        def solve(mid):
            res = 0 
            for i in range(mid):
                if nums[i] > k:
                    res += abs(k - nums[i])    
            res += abs(k - nums[mid])
            for i in range(mid + 1, N):
                if nums[i] < k:
                    res += abs(k - nums[i])
            return res
        # print(nums)
        if N % 2 == 1:
            return solve(N // 2)
        # print(solve(N // 2 - 1), solve(N // 2))

        if nums[N // 2] >= k:
            return solve(N // 2)
        
        return min(solve(N // 2), solve(N // 2 - 1))
        