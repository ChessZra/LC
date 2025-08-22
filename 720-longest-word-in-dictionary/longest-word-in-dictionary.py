class Solution:
    def longestWord(self, words: List[str]) -> str:
        lookup = set(words)
        N = len(words)
        best = ''
        for word in words:
            s = ''
            valid = True
            for char in word:
                s += char
                if s not in lookup:
                    valid = False
                    break
            if valid:
                if len(word) > len(best):
                    best = word
                elif len(word) == len(best):
                    best = min(best, word)
        return best