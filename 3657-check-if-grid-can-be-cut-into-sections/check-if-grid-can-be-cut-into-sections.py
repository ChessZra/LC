class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        N = len(rectangles)
        xint = [(x[0], x[2]) for x in rectangles]
        yint = [(y[1], y[3]) for y in rectangles]

        xint.sort()
        yint.sort()

        count = 0
        mx_reach = 0
        for i in range(1, N):
            mx_reach = max(mx_reach, xint[i - 1][1])
            if xint[i][0] < mx_reach:
                continue
            count += 1

        # print(xint, count)
        if count >= 2:
            return True

        mx_reach = 0
        count = 0
        for i in range(1, N):
            mx_reach = max(mx_reach, yint[i - 1][1])
            if yint[i][0] < mx_reach:
                continue
            count += 1

        # print(yint, count)
        return count >= 2