class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        N = len(nums)

        def good(index):
            if N == 1:
                return True

            if index == 0 and nums[0] != nums[1]:
                return True
            if index == N - 1 and nums[index] != nums[index - 1]:
                return True
            
            if nums[index] != nums[index - 1] and nums[index] != nums[index + 1]:
                return True
            
            return False

        l, r = 0, N - 1
        while l <= r:
            m = (l + r) // 2

            if good(m):
                return nums[m]

            if m < N - 1:
                if nums[m] != nums[m + 1]:
                    if (N - m - 1) % 2 == 1:
                        l = m + 1
                    else:
                        r = m - 1
                else:
                    if (N - m - 1) % 2 == 0:
                        l = m + 1
                    else:
                        r = m - 1

        return -1