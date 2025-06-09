class Solution:
    def fillCups(self, amount: List[int]) -> int:
        res = 0

        while True:
            amount.sort()
            if amount[-1] == 0:
                break
            
            if amount[-2] > 0:
                res += 1
                amount[-1] -= 1
                amount[-2] -= 1
            else:
                res += 1
                amount[-1] -= 1 
        return res