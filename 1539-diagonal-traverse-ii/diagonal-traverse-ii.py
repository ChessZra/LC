class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """ 
        (0, 0) -> (0, 0)
        (0, 1) -> (0, 1) (1, 0)
        (0, 2) -> (0, 2) (1, 1) (2, 0)
        """
        R = len(nums)
        def find_root(r, c):
            dist_to_left = c
            dist_to_down = R - r - 1
            if dist_to_left < dist_to_down:
                return (r + dist_to_left, 0) 
            else:
                return (R - 1, c - dist_to_down)

        f = collections.defaultdict(list)
        for r in range(R):
            for c in range(len(nums[r])):
                f[find_root(r, c)].append(nums[r][c])

        res = []
        for r in range(len(nums)):
            res.extend(f[(r, 0)][::-1])
        
        mx = max([len(x) for x in nums])
        for c in range(1, mx):
            if len(f[(R - 1, c)]) > 0: 
                res.extend(f[(R - 1, c)][::-1])

        return res