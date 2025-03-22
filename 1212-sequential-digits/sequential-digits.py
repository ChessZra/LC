class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        # construct it - bruteforce if tle then just cache it lmao
        
        # 1,000,000,000 => 9 digits at most

        tuff = []
        for i in range(1, 10):
            damn = str(i)
            tuff.append(int(damn))
            for j in range(i + 1, 10):
                damn += str(j)
                tuff.append(int(damn))
        
        tuff.sort()
        res = []
        start = False
        for t in tuff:
            if t >= low:
                start = True
            if t > high:
                break

            if start:
                res.append(t)

        return res