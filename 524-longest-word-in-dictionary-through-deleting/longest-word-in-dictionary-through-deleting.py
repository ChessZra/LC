class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best = ""
        N = len(s)
        for word in dictionary:
            j = 0
            for i in range(N):
                if s[i] == word[j]:
                    j += 1
                if j >= len(word):
                    if len(word) > len(best):
                        best = word
                    elif len(word) == len(best):
                        best = min(best, word)
                    break
        return best