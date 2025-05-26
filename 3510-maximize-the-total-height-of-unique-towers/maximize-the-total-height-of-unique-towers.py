class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort()
        res = 0
        last_used = 10 ** 20

        for i in range(len(maximumHeight) - 1, -1, -1):

            if maximumHeight[i] >= last_used:
                res += (last_used - 1)
                last_used -= 1
            else:
                res += maximumHeight[i]
                last_used = maximumHeight[i]

            if last_used <= 0:
                return -1
                
        return res