# class Solution:
#     def maximumProfit(self, prices: List[int], k: int) -> int:
#         N = len(prices)
#         INF = 10 ** 20
#         @cache
#         def solve(index, k, state):
#             if index >= N:
#                 if state == -1:
#                     return 0
#                 return -INF # needs to finish all transaction
#             if k == 0:
#                 return 0
#             best = -INF
#             if state == -1: # not in a transaction
#                 best = max(best, solve(index + 1, k, 0) - prices[index])
#                 best = max(best, solve(index + 1, k, 1) + prices[index])
#                 best = max(best, solve(index + 1, k, -1))
#             elif state == 0:
#                 best = max(best, solve(index + 1, k - 1, -1) + prices[index])
#                 best = max(best, solve(index + 1, k, state))
#             else: # state == 1
#                 best = max(best, solve(index + 1, k - 1, -1) - prices[index])
#                 best = max(best, solve(index + 1, k, state))
#             return best
#         return solve(0, k, -1)    

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        N = len(prices)
        INF = 10 ** 20
        
        # map states: -1 -> 0, 0 -> 1, 1 -> 2
        dp = [[[-INF] * 3 for _ in range(k + 1)] for _ in range(N + 1)]
        
        # base cases
        for kk in range(k + 1):
            dp[N][kk][0] = 0  # state -1 allowed to end with 0 profit
            # dp[N][kk][1] and dp[N][kk][2] stay -INF (invalid unfinished transactions)
        
        for i in range(N - 1, -1, -1):
            for kk in range(k + 1):
                # state = -1
                if kk >= 0:
                    best = -INF
                    if kk >= 0:  # can always skip
                        best = max(best, dp[i + 1][kk][0])  # skip
                    if kk >= 0:
                        best = max(best, dp[i + 1][kk][1] - prices[i])  # buy -> state=0
                        best = max(best, dp[i + 1][kk][2] + prices[i])  # short -> state=1
                    dp[i][kk][0] = best
                
                # state = 0 (holding long)
                if kk >= 0:
                    best = dp[i + 1][kk][1]  # hold
                    if kk > 0:
                        best = max(best, dp[i + 1][kk - 1][0] + prices[i])  # sell -> finish transaction
                    dp[i][kk][1] = best
                
                # state = 1 (holding short)
                if kk >= 0:
                    best = dp[i + 1][kk][2]  # hold
                    if kk > 0:
                        best = max(best, dp[i + 1][kk - 1][0] - prices[i])  # cover -> finish transaction
                    dp[i][kk][2] = best
        
        return dp[0][k][0]
