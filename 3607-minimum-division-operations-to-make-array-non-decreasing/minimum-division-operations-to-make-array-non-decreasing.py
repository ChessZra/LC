N = 1_000_001
possible = [True] * N
possible[0] = False
possible[1] = False
for i in range(2, int(N**0.5) + 1):
    if possible[i] == True:
        start = i**2
        while start < N:
            possible[start] = False
            start += i  
primes = []
for i in range(len(possible)):
    if possible[i]:
        primes.append(i)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        for i in range(N - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                if possible[nums[i]]:
                    return -1
                for j in range(len(primes)):
                    if nums[i] % primes[j] == 0:
                        best = max(primes[j], nums[i] // primes[j])
                        nums[i] //= best
                        res += 1
                        break
                # print(nums)
                if nums[i] > nums[i + 1]:
                    return -1
        return res