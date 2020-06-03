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

    id = 583
    word = '昨天买了U盘和耳机，今天努力继续做PPT！'
    idea = 'DP动态规划，思路承接1143的最长公共子序列问题，这个题就相当于个变体'
    code = '''
> 两个字符串长度为m和n，长度为l的最长公共子序列就是最后能留下的部分，那么删除步数就是m+n-2l，故只需要找到l的长度即可，转化为1143问题，dp[i][j]是字符串长度为i和j时的l，依次类推即可
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1),len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return n+m-2*dp[n][m]
```
'''
    thoughts = '做完100道题之后翻过来复习两个月，不然不踏实！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
