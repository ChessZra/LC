class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        f = collections.Counter()
        for num in nums:
            f[num] += 1
        
        dominant = None
        for key, value in f.items():
            if value > (N // 2):
                dominant = key
                break
        
        if dominant is None:
            return -1

        freq = 0
        for i in range(N):
            if nums[i] == dominant:
                freq += 1
            
            right = f[dominant] - freq

            if freq > ((i + 1) // 2) and right > ((N - i - 1) // 2):
                return i
                
        return -1