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

    id = 189
    word = '今天和朋哥畅聊了很久，受益匪浅，想着Data Scientist的目标进发！'
    idea = '今天是简单版强盗抢劫，感觉DP的思想还是不那么容易掌握，递归会写但是记录值不太会'
    code = '''
> 递归记录子问题的值，递推关系是当前这次抢不抢的max
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        N = len(nums)
        dp = [0] * (N+1)
        dp[0] = 0
        dp[1] = nums[0]
        for k in range(2, N+1):
            dp[k] = max(dp[k-1], nums[k-1] + dp[k-2])
        return dp[N]
```
> 从递推关系可以看出，只需要k-1和k-2两个的f，故优化空间
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        curr = 0  
        # 每次循环，计算“偷到当前房子为止的最大金额”
        for i in nums:
            # 循环开始时，curr 表示 dp[k-1]，prev 表示 dp[k-2]
            # dp[k] = max{ dp[k-1], dp[k-2] + i }
            prev, curr = curr, max(curr, prev + i)
            # 循环结束时，curr 表示 dp[k]，prev 表示 dp[k-1]
        return curr
```
'''
    thoughts = '这两天要加油做毕设啊！冲！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
