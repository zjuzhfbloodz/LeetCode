class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n<=1: return 0
        dp = [[[None, None] for _ in range(3)] for _ in range(n)]  # (n, k+1, 2)
        
        # 边界状态需要考虑：1.j=0时对i穷举; 2.i=0时对有效的j穷举(j=1,2)
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = -float('inf')
        for j in range(1, 3):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        
        # 状态转移
        for i in range(1, n):
            for j in range(1, 3):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
        print(dp)
        return dp[-1][-1][0]

s = Solution()
print(s.maxProfit([1,2,3,4,5]))