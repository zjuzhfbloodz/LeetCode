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

    id = 744
    word = '早睡，早睡，早睡！重要的事情说三遍，明天去医院体检查查身体！'
    idea = '进入二分查找部分，这个题目就是单纯搜索问题，用二分最简单'
    code = '''
> 简单的二分查找，复杂度O(log(N))，因为这次是求大于的最小值，故等于的时候l依然要往mid的右边挪一位；另外，由于字符是循环的(a>z)，故一开始判断特殊情况。
```python
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]: return letters[0]
        l,r = 0,len(letters)-1
        while l <= r:
            mid = l + (r-l)//2
            if target < letters[mid]:
                r = mid-1
            elif target >= letters[mid]: #等于l也要+1
                l = mid+1
        return letters[l]
```

'''
    thoughts = '进入二分查找问题！做完之后复习一遍！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
