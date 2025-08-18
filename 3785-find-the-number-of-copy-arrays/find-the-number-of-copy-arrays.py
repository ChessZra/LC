class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        previous_interval = bounds[0]
        N = len(original)
        for i in range(1, N):
            delta = original[i] - original[i - 1]
            l, r = previous_interval
            l += delta
            r += delta
            previous_interval = [max(l, bounds[i][0]), min(r, bounds[i][1])]
        return max(0, previous_interval[1] - previous_interval[0] + 1)