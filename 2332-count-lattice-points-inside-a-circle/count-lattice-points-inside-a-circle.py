class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = 0 
        for x in range(201):
            for y in range(201):
                
                for cx, cy, r in circles:
                    # (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2
                    if (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2:
                        #print(x, y)
                        res += 1
                        break
        return res