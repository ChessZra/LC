class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = set(), set(), set()
        ab, ac, bc = set(), set(), set()
        abc = set()
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            a.add(x)
            b.add(y)
            c.add(z)
            ab.add((x, y))
            ac.add((x, z))
            bc.add((y, z))
            abc.add((x, y, z))
        # for x, y, z in abc:
        #     tx, ty, tz = target
        #     best = False
        #     if tx == x and ty == y and tz == z:
        #         best = True
        #     elif tx == x and ty == y and tz != z:
        #         best = tz in c
        #     elif tx == x and ty != y and tz == z:
        #         best = ty in b
        #     elif tx != x and ty == y and tz == z:
        #         best = tx in a
        #     elif tx != x and ty != y and tz == z:
        #         best = (tx, ty) in ab
        #     elif tx == x and ty != y and tz != z:
        #         best = (ty, tz) in bc
        #     elif tx != x and ty == y and tz != z:
        #         best = (tx, tz) in ac
        #     elif tx != x and ty != y and tz != z:
        #         best = (tx, ty, tz) in ab
        #     if best:
        #         return True
        return target[0] in a and target[1] in b and target[2] in c


