class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        f = collections.Counter(s)
        
        odds = 0
        for char, freq in f.items():
            odds += int(freq % 2 == 1)
        
        if odds > 0:
            odds -= 1 # middle element for mn
        
        amt_pal = 1 + odds
        #print(amt_pal, mn, odds)

        return amt_pal <= k <= len(s)