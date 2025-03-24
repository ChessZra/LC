class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        N = len(nums)

        # "want" can only have three different possibilities heehehaw
        @cache
        def dfs(left, right, want):
            if right <= left:
                return 0
            
            best = 0
            if nums[left] + nums[left + 1] == want:
                best = max(best, 1 + dfs(left + 2, right, want))
            
            if nums[right] + nums[right - 1] == want:
                best = max(best, 1 + dfs(left, right - 2, want))
            
            if nums[left] + nums[right] == want:
                best = max(best, 1 + dfs(left + 1, right - 1, want))
            return best
        
        return 1 + max(dfs(2, N - 1, nums[0] + nums[1]), dfs(0, N - 3, nums[-1] + nums[-2]), dfs(1, N - 2, nums[0] + nums[-1]))