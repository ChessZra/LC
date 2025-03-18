class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)

        def add(bit_array, number):
            for i in range(32):
                if (number & (1 << i)) > 0:
                    bit_array[i] += 1

        def subtract(bit_array, number):
            for i in range(32):
                if (number & (1 << i)) > 0:
                    bit_array[i] -= 1

        # if all elements in bit_array are <= 1, then 
        # all pairs are nice
        def good(bit_array):
            for freq in bit_array:
                if freq > 1:
                    return False
            return True 

        l = 0
        # 1_000_000_000 max, 32 bits -> 4_294_967_295
        bit = [0] * 32
        ans = 1
        for r in range(N):
            add(bit, nums[r])

            while not good(bit):
                subtract(bit, nums[l])
                l += 1
            
            ans = max(ans, r - l + 1)
        return ans