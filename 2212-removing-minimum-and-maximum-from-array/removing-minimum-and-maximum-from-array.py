class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        N = len(nums)
        
        mx = max(nums)
        mn = min(nums)

        mxi = nums.index(mx)
        mni = nums.index(mn)

        l, r = min(mxi, mni), max(mxi, mni)

        return min(r + 1, N - l, l + 1 + N - r)