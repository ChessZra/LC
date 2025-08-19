class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        N = len(nums)
        res = 0
        last_greater = -1
        last_within = None
        for i in range(N):
            if nums[i] > right:
                last_greater = i
                last_within = None
                continue
            if left <= nums[i] <= right:
                res += i - last_greater
                last_within = i
            else: # nums[i] < left
                if last_within is not None:
                    res += 1 + (last_within - last_greater - 1)
        return res