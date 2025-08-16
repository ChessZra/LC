class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        arr = [int(x) for x in num]
        INT_MAX = 2 ** 31 - 1
        N = len(arr)
        res = []
        def go(first, second, index, path):
            if index >= N:
                if len(path) >= 3:
                    nonlocal res
                    res = path.copy()
                    return True
                else:
                    return False
            current = 0
            best = False
            for i in range(index, N):
                current *= 10
                current += arr[i]
                if arr[index] == 0 and i != index:
                    break
                if current > INT_MAX or current > (first + second):
                    break
                if current == (first + second):
                    best |= go(second, current, i + 1, path + [current])
            return best
        first = 0
        for i in range(N):
            first *= 10
            first += arr[i]
            if arr[0] == 0 and i != 0:
                break
            if first > INT_MAX:
                break
            second = 0
            for j in range(i + 1, N):
                second *= 10
                second += arr[j]
                if arr[i + 1] == 0 and j != i + 1:
                    break
                if second > INT_MAX:
                    break
                if go(first, second, j + 1, [first, second]):
                    return res
        return []