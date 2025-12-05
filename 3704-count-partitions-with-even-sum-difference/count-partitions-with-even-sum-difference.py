class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        tot = sum(nums)
        run = 0
        res = 0
        for i in range(len(nums) - 1):
            run += nums[i]
            if (run - (tot - run)) % 2 == 0:
                res += 1
        return res