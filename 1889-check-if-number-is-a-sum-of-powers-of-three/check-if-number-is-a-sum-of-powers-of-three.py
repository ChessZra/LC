class Solution:
    def __init__(self):
        self.all_possible = self._precompute()
    
    def checkPowersOfThree(self, n: int) -> bool:
        return n in self.all_possible
    
    def _precompute(self):
        arr = []
        for i in range(0, 10000):
            y = 3 ** i
            if y > 10 ** 7:
                break
            arr.append(y)
        all_possible = []
        path = []
        N = len(arr)
        def dfs(index, total_sum):
            all_possible.append(total_sum)
            if index >= N:
                return 
            dfs(index + 1, total_sum)
            dfs(index + 1, total_sum + arr[index])
        dfs(0, 0)
        return set(all_possible)