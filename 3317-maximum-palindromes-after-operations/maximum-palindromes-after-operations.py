class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        N = len(words)
        new_words = sorted(words, key=lambda x:len(x))
        f = collections.Counter()
        for word in words:
            for char in word:
                f[char] += 1
        res = 0
        for index, word in enumerate(new_words):
            length = len(word) # we need to make a palindrome of length length

            pairs_needed = length // 2
            remainder = length % 2

            # match the evens
            for k, v in f.items():
                if pairs_needed == 0:
                    break
                have_pairs = v // 2
                removing = min(have_pairs, pairs_needed)

                f[k] -= (removing * 2)
                pairs_needed -= removing
            if pairs_needed > 0:
                break # can't do it anymore

            # match the remainder
            # take away from an odd first
            for k, v in f.items():                
                if remainder == 0:
                    break
                if v > 0 and v % 2 == 1:
                    f[k] -= 1
                    remainder -= 1
                    break

            for k, v in f.items():                
                if remainder == 0:
                    break
                if v > 0 and v % 2 == 0:
                    f[k] -= 1
                    remainder -= 1
                    break

            if remainder != 0:
                break
            res += 1
        
           

        return res