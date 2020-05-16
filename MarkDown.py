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

    id = 343
    word = '今天完成了毕业论文初稿，但是其实还有许多需要思考的地方，希望可以思考的全面一些吧！加油！'
    idea = 'DP动态规划，思考好状态转移方程，即f(n)=max(f(i)*(n-i))'
    code = '''
> 自己的想法，利用上述状态转移方程
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=1: return 0
        if n==2: return 1
        if n==3: return 2 #2和3的时候特殊，他们当时的max不能被后面的利用，因为他们的本身大于两数乘积的max，2>1且3>2
        maxmul = [2,3]
        for i in range(4,n+1):
            thismax = 0
            for j in range(2,i):  
                thismax = max(thismax,(i-j)*maxmul[j-2])
            maxmul.append(thismax)
        return maxmul[n - 2]
```
> 数学方法，值得思考，感觉是数论，比上述算法快，因为DP问题说白了还是穷举，见[这里](https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/)
```python
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
```
'''
    thoughts = '毕业论文初稿完成，但是思考不能停止！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
