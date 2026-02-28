class Solution:
    def countPairs(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        def good(x, y):
            xl = list(str(x))
            xn = len(xl)
            for i in range(xn):
                for j in range(i + 1, xn):
                    xl[i], xl[j] = xl[j], xl[i]
                    if y == int(''.join(xl)):
                        return True
                    xl[i], xl[j] = xl[j], xl[i]
            return False
        for i in range(N):
            for j in range(i + 1, N):
                x, y = nums[i], nums[j]
                if x == y or good(x, y) or good(y, x):
                    res += 1
        return res