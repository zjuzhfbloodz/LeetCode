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

    id = 376
    word = '今天熟悉了CNN，吃了夜宵小龙虾，明天学习RNN！加油！'
    idea = 'DP动态规划，思考好状态转移方程即可，依然是最长子序列问题，今天这个题目自己想出来啦！就是复杂了一些...'
    code = '''
> 动态规划，maxls记录以i元素结尾的最长子序列长度，sign记录i和i-1是升序还是降序，用来加入新值时的判断，然后一步步进行，sign满足就+1看看是不是max，要注意diff=0的情况
```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        maxls,sign = [1],[0]
        for i in range(1,n):
            maxl,s = 0,0
            for j in range(0,i):
                diff = nums[i] - nums[j]
                if diff == 0: #相等了，一般来说就continue就行，但是需要考虑极端情况[1,1,1,1]这样的
                    if maxl < 1:
                        maxl,s = 1,0
                elif diff * sign[j] <= 0 and maxl < maxls[j] + 1: #满足条件且maxl小于当前值+1就更新
                    maxl = maxls[j] + 1
                    s = 1 if diff > 0 else -1
            maxls.append(maxl)
            sign.append(s)
        return max(maxls)
```
> 贪心算法，思路清奇，心态爆炸，很快
```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: # 当出现升序时, 和**有效**的降序数量上加1
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down, up)

```
'''
    thoughts = '最长子序列问题有些眉目了，今天感悟：递归 < DP < 贪心，同样需要思考的东西也更多，加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
