class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = [] # number of plates
        N = len(s)
        count = 0
        for char in s:
            if char == '*':
                count += 1
            prefix.append(count)
        
        right = [None] * N # right most candle at index
        right_most_candle = None
        for i in range(N - 1, -1, -1):
            if s[i] == '|':
                right_most_candle = i
            right[i] = right_most_candle
        
        left = []
        left_most_candle = None
        for i in range(N):
            if s[i] == '|':
                left_most_candle = i
            left.append(left_most_candle)

        res = []
        for l, r in queries:
            if right[l] is None or left[r] is None:
                res.append(0)
            else:
                
                right_index = left[r]
                left_index = right[l]

                if left_index >= right_index:
                    res.append(0)
                else:
                    res.append(prefix[right_index] - prefix[left_index])
        return res