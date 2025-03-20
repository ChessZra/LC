class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        """
        gcd(a, b, c, d, e) = gcd(a, gcd(b, gcd(c, ...)))
        you learn new things everyday hehehehaw
        """

        num_ones = nums.count(1)
        N = len(nums)

        if num_ones > 0:
            return N - num_ones
        
        best = 10 ** 20
        for i in range(N):
            running_gcd = nums[i]
            for j in range(i + 1, N):
                running_gcd = gcd(running_gcd, nums[j])
                if running_gcd == 1:
                    best = min(best, j - i + 1)
                    break
        
        if best == 10 ** 20:
            return -1
        it_takes = best - 1
        return N - 1 + it_takes