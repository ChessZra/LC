class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        f = {x: []}
        N = len(nums)
        for i in range(N):
            if nums[i] == x:
                f[x].append(i)
        res = []
        for i in range(len(queries)):
            if (queries[i] - 1) < len(f[x]):
                res.append(f[x][queries[i] - 1])
            else:
                res.append(-1)
        return res