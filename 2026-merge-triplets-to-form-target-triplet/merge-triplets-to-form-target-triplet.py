class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = set(), set(), set()
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            a.add(x)
            b.add(y)
            c.add(z)
        return target[0] in a and target[1] in b and target[2] in c


