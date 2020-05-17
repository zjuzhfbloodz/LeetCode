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

    id = 279
    word = '终于提交了初稿，明天开始学习！加油！'
    idea = 'DP动态规划，思考好状态转移方程，但是这个题单独用动态规划速度很慢'
    code = '''
> 自己的想法，DP动态规划，简化成了3行，原理是找1-（n-1）所有的最小数量组合，然后n就是减i平方+1的最小值
```python
class Solution:
    def numSquares(self, n: int) -> int:
        result = [0,1]
        for i in range(2,n+1): result.append(min([1+result[i-j**2] for j in range(1, int(i ** 0.5) + 1)]))
        return result[n]
```
> 数学方法，拉格朗日提出来的，比上述算法快太多，降维打击，因为DP问题说白了还是穷举，见[这里]最后一种方法(https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode/）
```python
class Solution:
    def isSquare(self, n: int) -> bool:
        sq = int(math.sqrt(n))
        return sq*sq == n

    def numSquares(self, n: int) -> int:
        # four-square and three-square theorems
        while (n & 3) == 0:
            n >>= 2      # reducing the 4^k factor from number
        if (n & 7) == 7: # mod 8
            return 4

        if self.isSquare(n):
            return 1
        # check if the number can be decomposed into sum of two squares
        for i in range(1, int(n**(0.5)) + 1):
            if self.isSquare(n - i*i):
                return 2
        # bottom case from the three-square theorem
        return 3
```
'''
    thoughts = '这个题目还可以通过贪心算法求解，还需学习！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
