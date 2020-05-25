import time
import os
import shutil
class Markdown:

    def __init__(self,id,word,idea,code,thoughts):
        self.time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.id = id
        self.pic = '![text](https://github.com/zjuzhfbloodz/LeetCode/blob/master/questions/{:0>4d}.png?raw=true)'.format(self.id)
        self.path = 'D:\Code\LeetCode\leetcode-algorithms'
        self.question = self.get_question()
        self.url = self.get_url()
        self.words = word
        self.idea = idea
        self.code = code
        self.thoughts = thoughts
        
    #获取题目链接
    def get_url(self,):
        if self.question[:4].isalnum():
            ques_name = self.question[6:]
        else: ques_name = self.question[5:]
        ques_name = ques_name.replace(" ", "-")
        return 'https://leetcode-cn.com/problems/'+ques_name
        
    #获取题目名称
    def get_question(self,):
        with open('folder_dict.txt','r') as f:
            dict = eval(f.read())
        return dict[self.id]

    #创建markdown文件
    def create_solution(self,):

        file_path = self.path + '\\' + self.question + '\\{:0>4d}.md'.format(self.id)
        
        with open(file_path, 'w') as f:
            f.write('## [{}]({})\n'.format(self.question,self.url))
            f.write('### 日期:\n' + '>{} {}\n'.format(self.time, self.words))
            f.write('### 题目:\n' + self.pic + '\n')
            f.write('### 思路:\n' + '>{}\n'.format(self.idea))
            f.write('### 代码:\n' + self.code + '\n')
            f.write('### 思考:\n' + '>{}\n'.format(self.thoughts) + '\n')
        
        shutil.copy(file_path,'D:\Markdown\LEETCODE')
            

if __name__ == "__main__":

    id = 474
    word = '这两天学DeepLearning有些焦虑，朋哥还没回复毕业论文的事情，希望可以沉下心来，加油！'
    idea = 'DP动态规划，思考好状态转移方程即可，进入0-1背包问题，这是一个两类0-1背包问题，套路差不多'
    code = '''
> DP，自己的想法，详细见代码注释dp[i][j][k]表示j个0和k个1能组成前i个字符的最大个数
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #排序是必须的
        strs,l = sorted(strs,key = lambda x:len(x)),len(strs)
        dp = [[[0 for i in range(m+1)] for j in range(n+1)] for k in range(l+1)]
        for i in range(l):
            l0,l1 = strs[i].count('0'),strs[i].count('1')
            for j in range(n+1):
                for k in range(m+1):
                    if j >= l1 and k >= l0:
                        dp[i+1][j][k] = max(dp[i][j][k],dp[i][j-l1][k-l0]+1)
                    else:
                        dp[i+1][j][k] = dp[i][j][k]
        return dp[-1][-1][-1]
```
> 上述方法可以降维，因为dp[i+1]只用到了dp[i]的值，故可以记录下来用两个二维数组来做，方法如下
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #排序是必须的
        strs,l = sorted(strs,key = lambda x:len(x)),len(strs)
        dp = [[0 for j in range(m+1)] for k in range(n+1)]
        last = [[0 for j in range(m+1)] for k in range(n+1)]
        for i in range(l):
            l0,l1 = strs[i].count('0'),strs[i].count('1')
            for j in range(n+1):
                for k in range(m+1):
                    if j >= l1 and k >= l0:
                        dp[j][k] = max(last[j][k],last[j-l1][k-l0]+1)
                    else:
                        dp[j][k] = last[j][k]
            #print(last,dp)
            last = [[j for j in i] for i in dp] #完全复制，直接赋值不行的
        return dp[-1][-1]
```
> dalao用逆序做的，目前不太懂，反正就是降维逆序就完事儿了，或者用上面的两个数组来记录
```python
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1): #逆序
                    dp[i][j] = max(dp[i][j], 1 + dp[i - zeros][j - ones])

        return dp[-1][-1]
```
'''
    thoughts = '背包问题有些掌握，但是模模糊糊总感觉不清楚，抽空看看背包九讲吧！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
