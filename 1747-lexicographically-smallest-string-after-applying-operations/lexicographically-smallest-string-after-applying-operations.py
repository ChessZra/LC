class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        N = len(s)

        best = None
        def go(x, y):
            nonlocal best
            arr = [int(x) for x in s]

            for i in range(N):
                if i % 2 == 0:
                    arr[i] += x * a
                else:
                    arr[i] += y * a
                arr[i] %= 10
            
            visited = set()
            offset = 0 

            while offset not in visited:
                new_arr = arr[offset:] + arr[:offset]
                if best is None:
                    best = new_arr
                else:
                    if new_arr < best:
                        best = new_arr

                visited.add(offset)
                offset += b
                offset %= N

        for i in range(11):
            # case of even/odd a (you can only change odds)
            go(0, i)

            if b % 2 == 1:
                # case of odd a (you can change all evens)
                for j in range(1, 11):
                    go(j, i)

        return ''.join(str(x) for x in best)