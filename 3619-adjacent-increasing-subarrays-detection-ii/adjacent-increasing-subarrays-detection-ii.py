class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        arr = []
        streak = 1
        N = len(nums)
        for i in range(1, N):
            if nums[i] > nums[i - 1]:
                streak += 1
            else:
                arr.append(streak)
                streak = 1
        arr.append(streak)
        best = 0
        for i in range(len(arr)):
            best = max(best, arr[i] // 2)
            if i > 0:
                best = max(best, min(arr[i], arr[i - 1]))
        return best

