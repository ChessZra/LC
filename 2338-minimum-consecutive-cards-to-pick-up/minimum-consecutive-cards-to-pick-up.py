class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mp = {}
        best = 10 ** 20
        N = len(cards)
        for i in range(N):
            if cards[i] not in mp:
                mp[cards[i]] = i
            else:
                best = min(best, i - mp[cards[i]] + 1)
                mp[cards[i]] = i
        if best == 10 ** 20:
            return -1
        return best