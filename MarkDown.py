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
        
        shutil.copy(file_path,'D:\Data\Markdown\LEETCODE')
            

if __name__ == "__main__":

    id = 135
    word = '5203的作业完成得不错，老师发来邮件，但是不知道回复的是否恰当，人生总是纠结'
    idea = '仍然是贪心算法，但是今天这个题思维难度不小，需要同时满足左条件和右条件，可以两次遍历完成'
    code = '''
> 对于每一个孩子，需要同时满足和左右两位孩子的关系即满足题目要求，故先从左到右遍历一边满足左关系，再从右到左遍历一遍使其在不影响左关系的前提下满足右关系，[详见](https://leetcode-cn.com/problems/candy/solution/candy-cong-zuo-zhi-you-cong-you-zhi-zuo-qu-zui-da-/)
```python
class Solution:
    def candy(self, ratings):
        n = len(ratings)
        ns = [1 for i in range(n)]
        for i in range(1,n):
            if ratings[i] > ratings[i-1]: ns[i] = ns[i-1] + 1
        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]: ns[j] = max(ns[j],ns[j+1]+1)
        return sum(ns)
```
'''
    thoughts = '其实我还有另外一种想法，是官方解法的方法四，但是没有实现，之后可以尝试'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
