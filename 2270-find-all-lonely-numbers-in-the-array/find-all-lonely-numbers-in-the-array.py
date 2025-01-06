class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        f = collections.Counter(nums)
        res = []
        for x, v in f.items():
            if f[x] == 1 and f[x - 1] == 0 and f[x + 1] == 0:
                res.append(x)
        return res