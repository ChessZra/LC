import random

class Solution:

    def __init__(self, m: int, n: int):
        self.R = m
        self.C = n
        self.last_index = m * n - 1
        self.mp = {}

    def flip(self) -> List[int]:
        index = random.randint(0, self.last_index)
        
        if index not in self.mp:
            self.mp[index] = self.mp.get(self.last_index, self.last_index)
            self.last_index -= 1
            return [index // self.C, index % self.C]
        else:
            old = index
            index = self.mp[index]
            self.mp[old] = self.mp.get(self.last_index, self.last_index)
            self.last_index -= 1
            return [index // self.C, index % self.C]

    def reset(self) -> None:
        self.last_index = self.R * self.C - 1
        self.mp = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()