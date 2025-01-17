class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        nums[0] -= k

        for i in range(1, N):
            if nums[i - 1] >= nums[i]:
                nums[i] = min(nums[i] + k, nums[i - 1] + 1)
            else:
                nums[i] = max(nums[i] - k, nums[i - 1] + 1)
        #print(nums)
        return len(set(nums))