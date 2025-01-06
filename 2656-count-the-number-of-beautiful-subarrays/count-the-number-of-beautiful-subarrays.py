class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:

        f = collections.Counter()
        f[0] = 1
        rs = 0
        res = 0
        for num in nums:
            rs ^= num
            res += f[rs]
            f[rs] += 1

        return res