class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        def solve(x):
            ans = []
            for i in range(1, math.ceil(x ** 0.5) + 1):
                num1 = i
                num2 = x // i
                if num1 * num2 == x:
                    ans = [num1, num2]
            return ans
        a, b = solve(num + 1), solve(num + 2)
        if abs(a[1] - a[0]) < abs(b[1] - b[0]):
            return a
        return b