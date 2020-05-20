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

    id = 646
    word = '今天初步入门了Pytorch，继续加油！'
    idea = 'DP动态规划，思考好状态转移方程即可，这个题目没想出转移方程，和昨天的300很像啊，很难受；这个题提前排序很重要！'
    code = '''
> 动态规划，f(n)是以当前区间为结尾的最长长度，状态转移方程是如果满足添加条件，则+1，遍历找max；记得先排序啊！
```python
class Solution(object): #Time Limit Exceeded
    def findLongestChain(self, pairs):
        pairs.sort() #先排序
        dp = [1] * len(pairs)

        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)
```
> 贪心算法，按区间的第二个数排序，这样如果某区间的第一个数比链条的末尾区间第二个值大，那么他一定能并入，res+=1然后改变最大值即可，这个思路很清奇！理解了！
```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x:x[1])
        res=1
        cur=pairs[0][1]
        for i in range(1,len(pairs)):
            if pairs[i][0]>cur:
                res+=1
                cur=pairs[i][1]
        return res

```
'''
    thoughts = '这个题目有些难度，和300类似，两个题目都没想出来了！要加油啊！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
