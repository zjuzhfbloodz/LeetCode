class Solution:
    def findLongestChain(self, pairs):
        if not pairs: return 0
        pairs = sorted(pairs,key=lambda x:x[0])
        maxleng,maxnum = [1],[pairs[0][1]]
        for i in range(1,len(pairs)):
            thismax,newnum = 0,pairs[i][1]
            for j in range(i):
                if maxnum[j] < pairs[i][0]: 
                    newleng = maxleng[j] + 1
                    if newleng > thismax:
                        thismax = newleng
                        newnum = pairs[i][1]
                    elif newleng == thismax:
                        newnum = min(newnum,pairs[i][1])
                else: 
                    newleng = maxleng[j]
                    if newleng > thismax:
                        thismax = newleng
                        newnum = maxnum[j]
                    elif newleng == thismax:
                        newnum = min(newnum,maxnum[j])
            maxleng.append(thismax)
            maxnum.append(newnum)
        print(pairs)
        print(maxleng)
        print(maxnum)
        return maxleng[-1]

s = Solution()
print(s.findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))