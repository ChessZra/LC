class Solution:
    def minLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def good(x):
            f = collections.Counter()
            current_sum = 0
            l = 0
            for i in range(N):
                f[nums[i]] += 1
                if f[nums[i]] == 1:
                    current_sum += nums[i]
                if (i - l + 1) == x:
                    if current_sum >= k:
                        return True
                    if f[nums[l]] == 1:
                        current_sum -= nums[l]
                    f[nums[l]] -= 1
                    l += 1
            return False
        l, r = 0, N
        while l < r:
            m = (l + r) // 2
            if good(m):
                r = m
            else:
                l = m + 1
        return -1 if not good(l) else l