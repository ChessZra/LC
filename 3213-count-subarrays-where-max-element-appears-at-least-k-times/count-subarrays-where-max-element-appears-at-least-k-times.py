class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        res = 0
        mx = max(nums)
        mp = {}
        counter = 0
        for i in range(N):
            if nums[i] == mx:
                counter += 1
                mp[counter] = i
            
            if counter - k >= 0:
                res += mp[counter - k + 1] + 1
        return res
            