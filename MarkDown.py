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

    id = 322
    word = '这两天学DeepLearning有些焦虑，朋哥还没回复毕业论文的事情，希望可以沉下心来，加油！'
    idea = '这个题是完全背包问题，自己的思路想出来的解决方案，抽空看看labuladong的完全背包'
    code = '''
> DP，自己的想法，DP[i]代表可以凑成钱数是i的最少硬币数，递推公式是DP[i-coins]的min再+1；特殊情况是不能凑成，设置为inf，最后再一起判断
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0 for i in range(amount+1)]
        for i in range(1,amount+1):
            path = [dp[i-coins[j]] for j in range(len(coins)) if i-coins[j] >= 0]
            if path: dp[i] = min(path) + 1
            else: dp[i] = float('inf') #如果不能凑成那么path是空列表，设置为inf
        return -1 if dp[-1] == float('inf') else dp[-1]
```
> 最开始的递归想法，太慢，不能AC
```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def inner(coins,amount):
            if amount == 0: return 0
            if amount in coins: return 1
            if amount < min(coins): return float('inf')
            output = min([inner(coins,amount-coins[i]) for i in range(len(coins)) if amount-coins[i]>=0]) + 1
            return output
        output = inner(coins,amount)
        return -1 if output == float('inf') else output
```
'''
    thoughts = '看[HERE](https://leetcode-cn.com/problems/coin-change/solution/yong-bei-bao-wen-ti-si-xiang-lai-li-jie-ying-bi-zh/)，讲明白了为什么01背包问题降维要逆序；同时和这个题目做了比较'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
