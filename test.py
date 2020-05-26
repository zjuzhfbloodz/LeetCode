class Solution:
    def coinChange(self, coins, amount):
        # def inner(coins,amount):
        #     if amount == 0: return 0
        #     if amount in coins: return 1
        #     if amount < min(coins): return float('inf')
        #     output = min([inner(coins,amount-coins[i]) for i in range(len(coins)) if amount-coins[i]>=0]) + 1
        #     return output
        # output = inner(coins,amount)
        # return -1 if output == float('inf') else output
        dp = [0 for i in range(amount+1)]
        for i in range(1,amount+1):
            path = [dp[i-coins[j]] for j in range(len(coins)) if i-coins[j] >= 0]
            if path: dp[i] = min(path) + 1
            else: dp[i] = float('inf')
        return -1 if dp[-1] == float('inf') else dp[-1]

s = Solution()
print(s.coinChange([2],1))
