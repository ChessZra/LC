import random

class Solution:

    def __init__(self, m: int, n: int):
        self.R = m
        self.C = n
        self.last_index = m * n - 1
        self.mp = {}

    def flip(self) -> List[int]:
        # get a random index
        index = random.randint(0, self.last_index)
        # get the unused index
        want = self.mp.get(index, index)
        # change the random index to the last index
        self.mp[index] = self.mp.get(self.last_index, self.last_index)
        # decrement last index
        self.last_index -= 1
        # return 
        return [want // self.C, want % self.C]

    def reset(self) -> None:
        self.last_index = self.R * self.C - 1
        self.mp = {}

# Your Solution object will be instantiated and called as such:
# obj = Solution(m, n)
# param_1 = obj.flip()
# obj.reset()