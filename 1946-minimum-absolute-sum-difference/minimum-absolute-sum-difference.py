class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        """
        [1, 5, 7]

        [1, 7, 5]
        [2, 3, 5]
        """
        N = len(nums1)
        sorted_nums = sorted(nums1)
        min_diff = sum([abs(nums1[i] - nums2[i]) for i in range(N)])
        MOD = 10 ** 9 + 7

        # we dont change it
        res = min_diff
        for index in range(N):
            # we change
            want = nums2[index]

            l, r = 0, N - 1
            while l < r:
                m = (l + r) // 2
                if sorted_nums[m] >= want:
                    r = m
                else:
                    l = m + 1

            closest = l
            if l > 0 and abs(sorted_nums[l - 1] - want) < abs(sorted_nums[l] - want):
                closest -= 1

            temp = min_diff - abs(nums1[index] - nums2[index])
            temp += abs(want - sorted_nums[closest])
            res = min(res, temp)

        return res % MOD