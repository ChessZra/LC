class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1_zero = nums1.count(0)
        nums2_zero = nums2.count(0)

        n1 = sum(nums1) + nums1_zero
        n2 = sum(nums2) + nums2_zero

        if n1 == n2:
            return n1

        if nums1_zero == 0 and nums2_zero == 0:
            return 0 if n1 == n2 else -1
        elif nums1_zero == 0 and nums2_zero != 0:
            return n1 if n1 > n2 else -1
        elif nums1_zero != 0 and nums2_zero == 0:
            return n2 if n2 > n1 else -1
        else:
            return max(n2, n1)