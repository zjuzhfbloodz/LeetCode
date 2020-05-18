class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        result,n = [1],len(s)
        for i in range(1,n):
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1])>=10: 
                if s[i] != '0': result.append(result[i-2]+result[i-1])
                else: result.append(result[i-2])
            else: 
                if s[i] != '0': result.append(result[i-1])
                else: return 0
        print(result)
        return result[n-1]

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        l1,l2,n = 1,1,len(s)
        for i in range(1,n):
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1])>=10: 
                if s[i] != '0': new = l1+l2
                else: new = l1
            else: 
                if s[i] != '0': new = l2
                else: return 0
            l1,l2 = l2,new
        return l2

s = Solution()
print(s.numDecodings('226'))