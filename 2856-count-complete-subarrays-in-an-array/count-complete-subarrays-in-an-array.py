class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        nu = len(set(nums))
        res = 0
        for i in range(N):
            st = set()
            for j in range(i, N):
                st.add(nums[j])

                if len(st) == nu:
                    res += N - j
                    break
        return res