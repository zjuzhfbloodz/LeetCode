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

    id = 303
    word = '和朋哥交流过感觉发文章好难，需要做的事情很多，今天论文写的很消极；还是要努力向前！做到问心无愧！'
    idea = 'DP动态规划，思考好状态转移方程即可，这个题目不难'
    code = '''
> 自己的想法，计算所有从起点到i和j的点的和，i和j之间的就是两者差；这个计算需要用到动态转移方程就是f(n) = f(n-1) + nums[n]；另外，像这样有顺序的可以用数组去承接，不一定要用字典，字典会慢很多
```python
class NumArray:

    def __init__(self, nums: List[int]):
        if not nums: return
        self.nums = nums
        self.sumdict = [nums[0]]

    def sumRange(self, i: int, j: int) -> int:
        k = len(self.sumdict)
        for x in range(k,j+1): self.sumdict.append(self.sumdict[-1] + self.nums[x]) #动态转移方程
        if i == 0: return self.sumdict[j]
        return self.sumdict[j]-self.sumdict[i-1]
```
'''
    thoughts = '相信自己，切勿妄自菲薄，做到问心无愧！明天继续完成毕业论文！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
