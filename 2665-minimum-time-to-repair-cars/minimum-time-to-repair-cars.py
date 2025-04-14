class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def can(time):
            """
            how many cars can we fix with given time
            time = r * n^2
            n = sqrt(time / r)
            """
            skibidi = 0
            for i in range(len(ranks)):
                skibidi += int((time / ranks[i]) ** 0.5)
            return skibidi >= cars

        l, r = 0, 10 ** 20
        while l < r:
            m = (l + r) // 2
            if can(m):
                r = m
            else:
                l = m + 1
        return l