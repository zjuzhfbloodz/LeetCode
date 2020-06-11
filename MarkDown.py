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

    id = 153
    word = '电脑明天到！学校也不知道开不开学，难受！'
    idea = '进入二分查找部分，这个题目需要转化一下，其实target就是nums[-1]'
    code = '''
> target就是nums[-1]，如果比他大说明是翻转的后半部分l=mid+1，如果小则是前半部分由于mid可能就是最小故r=mid，直到最后只剩一个元素
```python
#自己的想法，复杂一些，思想是一样的
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        if r == 0 or nums[0] < nums[-1]: return nums[0]
        while True:
            mid = l + (r-l)//2
            if nums[mid] > nums[-1]: l = mid + 1
            else:
                if nums[mid-1] > nums[mid]: return nums[mid]
                else: r = mid - 1
#改进后的算法
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r: 最后l=r输出
            mid = l + (r-l)//2
            if nums[mid] > nums[-1]: l = mid + 1
            else: r = mid
        return nums[l]
```
'''
    thoughts = '毕业论文交完和学校的联系可能就更少了吧！之后的人生路也要努力！！！努力终有结果，加油！！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
