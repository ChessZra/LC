class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        total = collections.Counter()
        for num in nums:
            total[num] += 1
        
        running_heap = []
        f = collections.Counter()
        for i in range(N - 1):
            f[nums[i]] += 1
            heappush(running_heap, (-f[nums[i]], nums[i]))

            freq, num = heappop(running_heap)
            right = total[num] - f[num]
            # print(freq, num, f[num], right)
            if f[num] > ((i + 1) // 2) and right > ((N - i - 1) // 2):
                return i
        
        return -1