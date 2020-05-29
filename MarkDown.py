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

    id = 377
    word = '手环记录昨晚只睡了不到7个小时，感觉不够呀，今晚要早睡！！不知道要不要买电脑，纠结！！'
    idea = '完全背包问题，这个题目加入了序列顺序，让自己有了新的思考，见下面的对比'
    code = '''
> DP动态规划，相比传统方法改变了forloop的顺序，使得构成目标和的序列有了顺序，即同时包含2+1+1=4、1+1+2=4和1+2+1=4
```python
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #完全背包问题
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for j in range(1,target+1):
            for num in nums:
                if j >= num:
                    dp[j] += dp[j-num]
        return dp[-1]

#传统方法，这种解法是无顺序的，例如1+1+2=4就只有这一种，因为按照nums的顺序先排1之后才会排2，故序列顺序固定
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        #完全背包问题
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for num in nums:
            for j in range(num,target+1):
                dp[j] += dp[j-num]
        return dp[-1]
```
'''
    thoughts = '这个题目有些有趣，需要进一步思考，和传统算法不同，加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
