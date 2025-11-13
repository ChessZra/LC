class Solution:
    def minOperations(self, n: int, m: int) -> int:
        """ 
        Sieve template created by Ezra
        n > 1, all primes strictly below n in sqrt(n) :)
        """
        N = 10_000
        possible = [True] * N
        possible[0] = False
        possible[1] = False
        for i in range(2, int(N**0.5) + 1):
            if possible[i] == True:
                start = i**2
                while start < N:
                    possible[start] = False
                    start += i  
        # Algorithm start
        pq = [(n, n)]
        visited = set()
        while pq:
            cost, x = heappop(pq)
            if x in visited or possible[x]:
                continue
            if x == m:
                return cost
            visited.add(x)
            str_x = str(x)
            for i in range(len(str_x)):
                digit = int(str_x[i])
                if digit < 9:
                    new = int(str_x[:i] + str(digit + 1) + str_x[i+1:])
                    heappush(pq, (cost + new, new))
                if digit > 0:
                    new = int(str_x[:i] + str(digit - 1) + str_x[i+1:])
                    heappush(pq, (cost + new, new))
        return -1
