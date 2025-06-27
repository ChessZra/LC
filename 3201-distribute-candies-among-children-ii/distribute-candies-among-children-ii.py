class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        
        """
        n candies among two children
        0:
        target = 5
        limit = (3, 2), (4, 1), (5, 0) 
    
        """
        res = 0
        for x in range(limit + 1):
            target = n - x
            # distribute target candies to two children with limit
            lm = max(0, target - limit)
           # print('target is', target)
            if lm > limit or target < 0:
                continue
            ans = min(limit, target) - lm + 1
            #print(f'({x}, {lm}-{min(limit, target)})', ans)
            res += ans
        return res