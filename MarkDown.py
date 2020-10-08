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

    id = 673
    word = '昨天果然说错话了，覆水难收，吸取教训之后改正吧！5102x的成绩也不错，继续加油啊！人生应该积极向上，无论躺着还是站着！'
    idea = '本来以为做的是la说的第一题，结果没想到做的是复杂版本，还要求最长序列个数，不过还好想出来了'
    code = '''
> 我的思路是找到以nums[i]结尾的最长递增子序列，同时追踪这个最长子序列可以由多少个之前的序列构成（即最长子序列个数），最后只需要根据maxdp叠加所有的个数即可
```python
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        #我的思路是找到以nums[i]结尾的最长递增子序列
        n,maxdp = len(nums),0
        if n == 0 or n == 1: return n
        dp = [(1,1)] * n #第一维度是长度，后面是这个长度可以由之前的几个序列得到比如12547，最后的7最长是4，可以由1257和1247构成，就是（4，2）
        for i in range(1,n):
            maxlen,count = 0,1
            for j in range(i):
                if nums[j] < nums[i]:
                    if  maxlen < dp[j][0]:
                        maxlen = dp[j][0]
                        count = dp[j][1]
                    elif maxlen == dp[j][0]: count += dp[j][1]
            maxdp = max(maxdp,maxlen + 1)
            dp[i] = (maxlen + 1,count)
        #针对maxdp的所有序列数求和
        output = sum([p[1] for p in dp if p[0] == maxdp])

        return output
```
'''
    thoughts = '人总会说错话，不要拘泥于此，但是要学会成长，希望多和爸妈聊天！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
