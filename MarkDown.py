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

    id = 57
    word = '今天理发购物和妈妈打球！明天回校！'
    idea = '纯粹是对题目的思考，和排序算法没啥关系，以后这种题先跳过吧，还是优先学习算法'
    code = '''
> 自己的想法，直接把区间insert进去，然后利用56的合并区间做
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i in range(len(intervals)):
            if intervals[i][0] >= newInterval[0]:
                intervals.insert(i,newInterval)
                break
        else: intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for inter in intervals:
            if len(res) == 0 or res[-1][1] < inter[0]:  # 如果结果集最后一个元素的右边界比新加入区间的左边界小，直接加入结果集
                res.append(inter)
            else:  # 否则，说明新加入的和结果集最后一个区间有重合，更新区间右边界即可
                res[-1][1] = max(res[-1][1], inter[1])
        return res
```
> 找到右区间第一个比左区间大的，找到左区间最后一个比右区间小的，这是新区间的重合区间，然后合并，之前的不管，之后的也不管，注意三种特殊情况即可
```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #三种特殊情况
        if not intervals: return [newInterval]
        if newInterval[1] < intervals[0][0]: return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]: return intervals + [newInterval]
        i,n = 0,len(intervals)
        #找左端第一个融合的
        while i < n and newInterval[0] > intervals[i][1]: i += 1
        #记录下左边最小和左边的坐标
        left,tmp = min(intervals[i][0], newInterval[0]),i
        #如果没有重合区间，直接insert然后输出
        if intervals[i][0] > newInterval[1]: return intervals[:tmp] + [newInterval] + intervals[tmp:]
        #找右端第一个融合的
        while i < n and newInterval[1] >= intervals[i][0]: i += 1
        #记录下右边最小
        right = max(newInterval[1], intervals[i-1][1])
        return intervals[:tmp] + [[left, right]] + intervals[i:]
```
    '''
    thoughts = '这种题目锻炼思维，对算法模型的构建意义不大，继续加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
