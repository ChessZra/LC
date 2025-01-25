class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        
        sorted_nums = sorted([(x, i) for i, x in enumerate(nums)])
        N = len(nums)

        if N == 1:
            return nums
        
        components = []
        prev = sorted_nums[0][0]
        comp = [sorted_nums[0][1]]
        for i in range(1, N):
            if sorted_nums[i][0] - prev <= limit:
                comp.append(sorted_nums[i][1])
            else:
                components.append(comp)
                comp = [sorted_nums[i][1]]
            prev = sorted_nums[i][0]
        components.append(comp)

        res = [None] * N
        for comp in components:
            i = 0
            for index in sorted(comp):
                res[index] = nums[comp[i]]
                i += 1
        return res