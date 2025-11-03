class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        N = len(nums)
        res = []
        for i in range(N - k + 1):
            subarray = nums[i:i+k]
            f = collections.Counter(subarray)
            arr = sorted([(k, v) for k, v in f.items()], key=lambda x:(x[1], x[0]), reverse=True)
            c = 0
            for i in range(min(x, len(arr))):
                c += arr[i][1] * arr[i][0]
            res.append(c)
        return res