class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=1: return 0
        if n==2: return 1
        if n==3: return 2
        maxmul = [2,3]
        for i in range(4,n+1):
            thismax = 0
            for j in range(2,i):
                thismax = max(thismax,(i-j)*maxmul[j-2])
            maxmul.append(thismax)
        return maxmul[n - 2]
        
s = Solution()
print(s.integerBreak(10))