class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        f = defaultdict(list)
        N = len(nums)
        for i in range(N):
            f[nums[i]].append(i)
        res = []
        for q in queries:
            arr = f[nums[q]]
            if len(arr) == 1:
                res.append(-1)
                continue
            l, r = 0, len(arr) - 1
            while l < r:
                m = (l + r) // 2
                if arr[m] >= q:
                    r = m
                else:
                    l = m + 1
            left_index, right_index = (l - 1) % len(arr), (l + 1) % len(arr)
            left, right = abs(q - arr[left_index]), abs(q - arr[right_index])
            if l + 1 == len(arr):
                right = min(right, N - right)
            if l - 1 == -1:
                left = min(left, N - left)
            res.append(min(right, left))
        return res