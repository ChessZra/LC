class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mp = {}
        N = len(nums)
        nu = len(set(nums))
        res = 0
        l = 0
        for r in range(N):

            mp[nums[r]] = 1 + mp.get(nums[r], 0)

            while len(mp) == nu:
                res += N - r
                mp[nums[l]] -= 1
                if mp[nums[l]] == 0:
                    del mp[nums[l]]
                l += 1
                
        return res

