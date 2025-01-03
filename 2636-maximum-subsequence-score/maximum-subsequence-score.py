class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)
        nums = [(nums1[i], nums2[i]) for i in range(N)]
        nums.sort(key=lambda x:-x[1])
        
        current_sum = 0

        pq = [] # min heap of size k - 1
        res = 0
        for i in range(N):
            num1, num2 = nums[i]
            
            if len(pq) == k - 1:
                res = max(res, num2 * (current_sum + num1))

            heappush(pq, num1)
            current_sum += num1

            if len(pq) == k:
                current_sum -= heappop(pq)
                
        return res