class Solution:
    def maxProfit(self, prices, fee):
        if not prices: return 0
        n = len(prices)
        div = [prices[i]-prices[i-1] for i in range(1,n)]
        output,ts = 0,-1*fee
        for i in range(len(div)):
            if div[i] >= 0:
                ts += div[i]
            elif ts > 0:
                output += ts
                ts = -1 * fee
            else: ts = -1 * fee
        if ts > 0: output += ts
        print(div)
        return output

s = Solution()
print(s.maxProfit([4,5,2,4,3,3,1,2,5,4],1))