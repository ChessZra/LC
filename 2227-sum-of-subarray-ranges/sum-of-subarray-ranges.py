class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        stk = []
        for i in range(N):

            while stk and stk[-1][0] <= nums[i]:
                stk.pop()
            prev = -1 if not stk else stk[-1][1]
            prev_sum = 0 if not stk else stk[-1][2]
            cur_sum = nums[i] * (i - prev) + prev_sum
            res += cur_sum
            stk.append((nums[i], i, cur_sum))
        
        stk = []
        for i in range(N):

            while stk and stk[-1][0] >= nums[i]:
                stk.pop()
            prev = -1 if not stk else stk[-1][1]
            prev_sum = 0 if not stk else stk[-1][2]
            cur_sum = nums[i] * (i - prev) + prev_sum
            res -= cur_sum
            stk.append((nums[i], i, cur_sum))

        return res
