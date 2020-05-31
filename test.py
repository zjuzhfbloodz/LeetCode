class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        dp = [[0 for i in range(2)]for j in range(n)]
        dp[0][1] = -prices[0]
        flag = True
        for p in range(1,n):
            dp[p][1] = dp[p-1][0] - prices[p]
            if dp[p-1][0] >= dp[p-1][1] + prices[p]: 
                dp[p][0] = dp[p-1][0]
                if not flag: 
                    dp[p][1] = dp[p-1][1]   
                    flag = True                
            else: 
                dp[p][0] = dp[p-1][1] + prices[p]
                dp[p][1] = dp[p-1][1]
                flag = False
            print(flag)
        print(dp)
        return dp[-1][0]

s = Solution()
print(s.maxProfit([1,2,3,0,2]))