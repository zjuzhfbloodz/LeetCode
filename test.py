class Solution:
    def numSquares(self, n: int) -> int:
        result = [0,1,2]
        for i in range(3,n+1):
            square_root, minss = int(i ** 0.5), n
            for j in range(1, square_root + 1):
                #print(j,i)
                minss = min(1+result[i-j**2],minss)
            result.append(minss)
        return result[n]

s = Solution()
print(s.numSquares(4586))