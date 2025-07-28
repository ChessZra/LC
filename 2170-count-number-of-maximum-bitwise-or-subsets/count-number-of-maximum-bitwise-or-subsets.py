class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for num in nums:
            mx |= num
        N = len(nums)
        res = 0
        def dfs(index, cur):
            if index >= N:
                nonlocal res
                res += int(cur == mx)
                return

            dfs(index + 1, cur | nums[index])
            dfs(index + 1, cur)
        dfs(0, 0)
        return res