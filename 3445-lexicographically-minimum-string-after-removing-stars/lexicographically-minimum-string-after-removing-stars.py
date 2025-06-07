class Solution(object):
    def clearStars(self, s):
        popping_off = []
        pq = []

        for index, char in enumerate(s):
            if char == '*':
                popping_off.append(heappop(pq))
            else:
                heappush(pq, (char, -index))

        lookup = set()
        for c, i in popping_off:
            lookup.add(-i)

        res = ""
        for i in range(len(s)):
            if i not in lookup and s[i] != '*':
                res += s[i]

        return res