class Solution:
    def wordBreak(self, s, wordDict):
        i,wordDict = 0,sorted(wordDict,key = lambda x:len(x))
        while i < len(wordDict):
            if wordDict[i] in s:
                s = s.replace(wordDict[i],'')
            i += 1
        if not s: return True
        else: return False
s = Solution()
print(s.wordBreak("cars",["car","ca","rs"]))