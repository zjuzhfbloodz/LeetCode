class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #找到两个字符串的公共子串
        def findMaxSame(w1,w2):
            n,m = len(w1),len(w2)
            dp = [[0 for i in range(m+1)] for j in range(n+1)]
            lengths = [[[] for i in range(m+1)] for j in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,m+1):
                    if w1[i-1] == w2[j-1]:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                        temp = lengths[i - 1][j - 1]
                        temp.append((i,j))
                        lengths[i][j] = temp
                    else:
                        if dp[i-1][j]>=dp[i][j-1]:
                            dp[i][j] = dp[i - 1][j]
                            lengths[i][j] = lengths[i - 1][j]
                        else:
                            dp[i][j] = dp[i][j-1]
                            lengths[i][j] = lengths[i][j - 1]
            print(dp[-1][-1])
            return lengths[-1][-1],n,m,0
        ls, n, m, output = findMaxSame(word1, word2)
        print(ls)
        ls.insert(0, (0, 0))
        ls.append((n+1, m+1))
        for i in range(len(ls) - 1):
            output += max(ls[i+1][0]-ls[i][0],ls[i+1][1]-ls[i][1]) - 1
        print(ls)
        return output

s = Solution()
print(s.minDistance("mart","karma"))