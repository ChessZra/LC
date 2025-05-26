class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        # Bruteforce DP
        N = len(strength)
        target = 2 ** N - 1

        @cache
        def solve(bitmask, x):
            if bitmask == target:
                return 0
            
            best = 10 ** 20
            for i in range(N):
                if bitmask & (1 << i) == 0:
                    t = math.ceil(strength[i] / x) 
                    best = min(best, t + solve(bitmask | (1 << i), x + k))
            return best
        
        return solve(0, 1)
        """
        Greedy attempt - 758/763 cases passed
        energy = 0
        x = 1
        time = 0

        while len(strength) > 0:
            time_needed_to_wait = math.ceil((min(strength) - energy) / x)
            # print(strength, x)
            time += time_needed_to_wait
            energy += time_needed_to_wait * x

            best = 10 ** 20
            idx = 0
            for i in range(len(strength)):
                if energy >= strength[i] and (energy - strength[i]) < best: 
                    best = energy - strength[i]
                    idx = i

            energy = 0
            strength.pop(idx)
            x += k

        return time

        """