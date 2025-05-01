class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:

        def solve(nums, target):
            f = collections.Counter()
            N = len(target)
            res = 0
            for s in nums:
                
                if len(s) <= len(target):
                    lookfor = target[:N - len(s)]
                    if lookfor + s == target:
                        res += f[lookfor]
                    #print(lookfor, nums, target)
                f[s] += 1
            return res
        return solve(nums, target) + solve(nums[::-1], target)