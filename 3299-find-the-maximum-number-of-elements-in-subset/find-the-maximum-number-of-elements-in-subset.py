class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        f = collections.Counter(nums)

        """
        O(N * 2) times two because for each number in nums, 
        you find the square root, it stops asap if none
        """
        @cache
        def solve(x):
            if f[x] < 2:
                return 0
            if x == 1:
                return f[x] // 2
            return 2 + solve(sqrt(x))

        best = 1
        for num in nums:
            if num == 1: # annoying
                best = max(best, (f[num] if f[num] % 2 == 1 else f[num] - 1))
                continue
            best = max(best, 1 + solve(sqrt(num)))
        return best