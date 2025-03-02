class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts.append(h)
        verticalCuts.append(w)

        mxx = 0
        temp = 0
        for x in verticalCuts:
            mxx = max(mxx, x - temp)
            temp = x
        
        mxy = 0
        temp = 0
        for y in horizontalCuts:
            mxy = max(mxy, y - temp)
            temp = y
        
        return (mxx * mxy) % (10 ** 9 + 7)