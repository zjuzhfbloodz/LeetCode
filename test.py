class Solution:
    def findTargetSumWays(self, nums,S):
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P, num - 1, -1): dp[j] += dp[j - num]
        print(dp)
        return dp[P]

s = Solution()
print(s.findTargetSumWays([9,7,0,3,9,8,6,5,7,6],2))