class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        #421
        f = collections.Counter(word)
        arr = sorted(f.values(), reverse=True)

        N = len(arr)
        x = collections.Counter(arr)
        res = 10 ** 20
        deleted = 0
        mx = arr[0]
        while mx > 0:
            temp = 0
            for j in range(N):
                if arr[j] < mx and abs(arr[j] - mx) > k:
                    temp += arr[j]
            res = min(res, temp + deleted)
            deleted += x[mx]
            x[mx - 1] += x[mx]
            x[mx] = 0
            mx -= 1

        return res