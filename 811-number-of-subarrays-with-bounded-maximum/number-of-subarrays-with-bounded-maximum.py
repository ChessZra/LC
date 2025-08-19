class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        N = len(nums)
        arr = []
        for i in range(N):
            if left <= nums[i] <= right:
                arr.append(1)
            elif nums[i] > right:
                arr.append(-1)
            else:
                arr.append(0)
        res = 0
        last_negative_one = -1
        last_one = None
        for i in range(N):
            if arr[i] == -1:
                last_negative_one = i
                last_one = None
                continue
            if arr[i] == 1:
                res += i - last_negative_one
                last_one = i
            else: # arr[i] == 0
                if last_one is not None:
                    res += 1 + (last_one - last_negative_one - 1)
        return res