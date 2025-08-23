class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        N = len(rewardValues)
        rewardValues.sort()
        dp = [[0] * (rewardValues[-1] + 1) for _ in range(N + 1)] 
        for index in range(len(dp) - 1, -1, -1):
            for cur_sum in range(len(dp[0]) -1, -1, -1):
                if index >= N:
                    dp[index][cur_sum] = cur_sum
                    continue
                best = 0
                if rewardValues[index] > cur_sum:
                    next_sum = cur_sum + rewardValues[index]
                    if rewardValues[-1] <= next_sum:
                        best = max(best, next_sum)
                    else: 
                        best = max(best, dp[index + 1][next_sum])
                best = max(best, dp[index + 1][cur_sum])
                dp[index][cur_sum] = best
        # print(dp)
        return dp[0][0]
        # @cache
        # def solve(index, cur_sum):
        #     if index >= N:
        #         return cur_sum
        #     best = 0
        #     if rewardValues[index] > cur_sum:
        #         next_sum = cur_sum + rewardValues[index]
        #         if rewardValues[-1] <= next_sum:
        #             best = max(best, next_sum)
        #         else: 
        #             best = max(best, solve(index + 1, next_sum))
        #     best = max(best, solve(index + 1, cur_sum))
        #     return best
        # return solve(0, 0)

