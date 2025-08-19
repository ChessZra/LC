class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        f = collections.Counter()
        for num in nums:
            f[num] += 1
        for num in set(nums):
            need = k - num
            if f[need] == 0 or f[num] == 0:
                continue
            if need == num:
                get = f[need] // 2
                if f[need] >= 2:
                    res += get
                f[need] -= get
                continue
            get = min(f[need], f[num])
            f[need] -= get
            f[num] -= get
            res += get
        return res