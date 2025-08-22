class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        pq = []
        N = len(nums)
        res = []
        f = collections.Counter()
        for i in range(N):
            f[nums[i]] += freq[i]
            heappush(pq, (-f[nums[i]], nums[i]))
            while pq and f[pq[0][1]] != -pq[0][0]:
                heappop(pq)
            if pq:
                res.append(-pq[0][0])
            else:
                res.append(0)
        return res