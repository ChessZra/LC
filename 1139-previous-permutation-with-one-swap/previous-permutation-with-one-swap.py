class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        # we can brute force intead of doing binary search
        # given that arr[i] is small enough
        # that is not the hard part of the problem
        N = len(arr)
        sl = SortedList()
        idx = {}
        for i in range(N - 1, -1, -1):
            sl.add(arr[i])
            idx[arr[i]] = i 
            l, r = 0, len(sl) - 1
            while l < r:
                m = (l + r) // 2
                if sl[m] >= arr[i]:
                    r = m
                else:
                    l = m + 1
            if l > 0:
                j = idx[sl[l - 1]]
                arr[i], arr[j] = arr[j], arr[i]
                break
        return arr

