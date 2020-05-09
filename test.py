#迭代
class Solution:
    def __init__(self,):
        self.result = [1,2]  
    def g(self, n):
        lenth = len(self.result)
        if n > lenth:
            for i in range(n - lenth):
                self.result.append(self.result[-1]+self.result[-2])
        return self.result[n - 1]

#递归
# class Solution:
#     def __init__(self,):
#         self.result = [1,2]  
#     def g(self, n):
#         lenth = len(self.result)
#         if n <= lenth: return self.result[n - 1]
#         self.result.append(self.g(n - 1) + self.g(n - 2))
#         return self.result[n - 1]
        
s = Solution()
print(s.g(100))
print(s.result)