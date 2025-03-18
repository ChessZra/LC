class Solution:
    def smallestValue(self, n: int) -> int:
        # use sieve to find all numbers below n
        # loop until n becomes prime
        """ 
        Sieve template created by Ezra
        n > 1, all primes strictly below n in sqrt(n) :)
        """
        n += 1
        possible = [True] * (n)
        possible[0] = False
        possible[1] = False

        for i in range(2, int(n**0.5) + 1):
            if possible[i] == True:
                start = i**2
                while start < n:
                    possible[start] = False
                    start += i  
        
        primes = []
        for x in range(len(possible)):
            if possible[x]:
                primes.append(x)
        
        n -= 1

        # main algorithm
        def divide(x):
            if possible[x]:
                return x
            
            for p in primes:
                if x % p == 0:
                    return divide(x // p) + divide(p)

        while True:
            new_n = divide(n)
            if possible[n] or n == new_n:
                return n
            n = new_n
        return -1