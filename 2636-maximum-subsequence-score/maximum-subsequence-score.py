class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        N = len(nums1)
        nums = [(nums1[i], nums2[i]) for i in range(N)]
        nums = sorted(nums, key=lambda x:x[1])

        pq = [] # max heap
        for i in range(N):
            heappush(pq, (-nums[i][0], i))

        lookup = collections.Counter()
        current_sum = 0
        for i in range(k - 1):
            mx, index = heappop(pq)
            lookup[index] = 1
            current_sum += -mx

        res = 0
        #print(nums, current_sum)
        for i in range(N - k + 1):
            num1, num2 = nums[i]
        
            # print(num2, current_sum, num1)
            if lookup[i] > 0:
                mx, index = heappop(pq)
                while index < i:
                    mx, index = heappop(pq)
                lookup[index] = 1
                current_sum += -mx

                #print('c1:', num2, current_sum, lookup)
                res = max(res, num2 * current_sum)

                current_sum -= num1
                lookup[i] = 0
            else:
                #print('c2:', num2, current_sum,num1, lookup)
                res = max(res, num2 * (current_sum + num1))

        return res