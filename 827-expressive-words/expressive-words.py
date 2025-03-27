class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:

        def get_arr(s):
            N = len(s)
            c = 1
            arr = []
            for i in range(1, N):
                if s[i] == s[i - 1]:
                    c += 1
                else:
                    arr.append((s[i - 1], c))
                    c = 1
            arr.append((s[-1], c))
            return arr

        orig = get_arr(s)
        def can(s):
            arr = get_arr(s)

            if len(arr) != len(orig):
                return False
            
            for i in range(len(arr)):
                c1, f1 = orig[i]
                c2, f2 = arr[i]

                if c1 != c2:
                    return False
                if f2 > f1:
                    return False
                if f2 < f1 and f1 == 2:
                    return False 

            return True

        res = 0
        for word in words:
            if can(word):
                res += 1
        return res