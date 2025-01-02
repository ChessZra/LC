class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        INF = float('inf')
        res = INF

        def go(nums1, nums2):
            ans = 0
            #print(nums1, nums2)
            for i in range(N - 1):
                if nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]:
                    continue
                
                if nums1[i] > nums1[-1]: 
                    ans += 1
                    nums1[i], nums2[i] = nums2[i], nums1[i] # swap it
                
                if nums2[i] > nums2[-1]:
                    ans += 1
                    nums1[i], nums2[i] = nums2[i], nums1[i] # swap it

                if not (nums1[i] <= nums1[-1] and nums2[i] <= nums2[-1]):
                    return INF

            return ans

        orig1 = nums1.copy()
        orig2 = nums2.copy()
        go1 = go(orig1, orig2)

        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        go2 = go(nums1, nums2)

        if go1 == INF and go2 == INF:
            return -1

        return min(go1, go2 + 1)