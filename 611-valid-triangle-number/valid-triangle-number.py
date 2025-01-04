class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """
        2, 3, 4, 4
        """
        res = 0
        nums.sort()
        N = len(nums)

        # a + b > c
        for i in range(2, N):
            c = nums[i]
            for j in range(i):
                b = nums[j]

                l, r = 0, j - 1
                while l < r:
                    m = (l + r) // 2
                    a = nums[m]

                    if a + b > c:
                        r = m
                    else:
                        l = m + 1
                if 0 <= r < N - 1 and nums[r] + b > c:
                    res += j - r

        return res