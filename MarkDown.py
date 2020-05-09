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

    id = 70
    word = '今天回校！看到同学们都很棒，自己也要加油！'
    idea = '今天进入动态规划问题，斐波那契数列是一个开始！今天这个爬楼梯就是一个斐波那契，DP就是用空间换时间，避免子问题重复运算，看了labuladong感觉蛮有收获'
    code = '''
> 自己的想法，给定n阶楼梯f(n)可分为两种情况，先爬2阶然后有f(n-2)或者先爬1阶然后f(n-1)，然后迭代去做；可以优化，就是每次只记录前两次的步数，因为计算n时只需要n-1和n-2
```python
class Solution:
    def __init__(self,):
        self.result = [1,2]  
    def g(self, n):
        lenth = len(self.result)
        if n > lenth:
            for i in range(n - lenth):
                self.result.append(self.result[-1]+self.result[-2])
        return self.result[n - 1]
```
> 递归也可以做，同理
```python
class Solution:
    def __init__(self,):
        self.result = [1,2] 
    def climbStairs(self, n: int) -> int:
        lenth = len(self.result)
        if n <= lenth: return self.result[n - 1]
        self.result.append(self.climbStairs(n - 1) + self.climbStairs(n - 2))
        return self.result[n - 1]
```
    '''
    thoughts = '和zmt打了球，宝子技术还不行，打着玩吧！DP问题很需要动脑子思考，加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
