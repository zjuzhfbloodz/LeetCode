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

    id = 413
    word = '今天重新对数据操作进行了思考，最后的结果还不错，明天写完总结就gaisu！'
    idea = 'DP动态规划，思考好状态转移方程；这个题目可以用数学方法去做，见下面我自己的想法'
    code = '''
> 自己的想法，利用数学思想，找到3个数的等差数列后就往后延长直到不再是等差数列，之后从该等差数列后的第一个数继续开始；如果当前3个数不是等差数列就往后走一个数。其中leng=序列长度-2，和等差数列个数的关系是count = leng*(leng+1)/2
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        a1,count = 0,0
        while a1 < len(A)-2:
            leng = 0
            if 2 * A[a1+1] == A[a1] + A[a1+2]: #如果找到，开始往后延长
                leng,d = leng+1,A[a1+1]-A[a1]
                a1 += 3
                while a1 < len(A):
                    if A[a1] - A[a1-1] == d:
                        leng += 1
                        a1 += 1
                    else: break
            else: a1 += 1 #如果没找到，下标加1，继续循环
            count += int(leng*(leng+1)/2) #count和序列长度的关系
        return count
```
> 双指针的方法，思路和自己的想法一样，但是是直接加count的，没用leng这一说
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        else:
            first = 0
            last = 2
            res = 0
            while last < len(A):
                if A[last] - A[last-1] == A[first+1] - A[first]:
                    res += last - first -1 
                    last += 1
                else:
                    first = last -1
                    last = first +2
        return res
```
> 动态规划的方法，思路见[这里](https://leetcode-cn.com/problems/arithmetic-slices/solution/chang-yong-tao-lu-jie-jue-dong-tai-gui-hua-by-lu-c/)
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3: return 0
        dif = [0]*(len(A)-1)
        dif[0] = A[1] - A[0]
        dp = [0]*len(A)
        for i in range(2, len(A)):
            dif[i-1] = A[i] - A[i-1]
            if dif[i-1] == dif[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

```
'''
    thoughts = '明天继续完成毕业论文！加油！但行善事！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
