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

    id = 69
    word = '不要熬夜了！今天睡了一天就因为晚上睡得晚！'
    idea = '进入二分查找部分，求平方根也可以用牛顿迭代'
    code = '''
> 简单的二分查找，复杂度O(log(N))，注意求中点时候的方法是l+(r-l)//2，这样防止l+r溢出内存空间
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2: return x
        l,r = 1,x
        while l <= r:
            mid = l+(r-l)//2
            if mid*mid > x:
                r = mid-1
            elif mid*mid < x:
                l = mid+1
            else: return mid
        return r
```
> 牛顿迭代求根，写过很多遍，这个题目没有精度要求，故简单一些
class Solution:
    def mySqrt(self, x: int) -> int:
        #y = 2*x0(x-x0) + x0^2 - c
        #y == 0 -> x = 0.5*(c-x0^2)/x0 + x0
        x0 = x
        while x0**2 > x: x0 = int(0.5*(x-x0**2)/x0 + x0)
        return x0
```
'''
    thoughts = '进入二分查找问题！做完之后复习一遍！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
