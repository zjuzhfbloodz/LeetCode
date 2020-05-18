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

    id = 91
    word = '今天简单了解了一下提升方法boosting，继续学习！'
    idea = 'DP动态规划，思考好状态转移方程即可，这个题目自己的想法和标答一样，感觉不错'
    code = '''
> 自己的想法，DP动态规划，状态转移方程：首先新加入字符s[i]自己肯定可以看成一种划分，故f(n)+=f(n-1)；再看s[i]是否能和s[i-1]组成10-26之间的数，可以的话就把这两个数字当成一个，f(n)+=f(n-2)；要注意0是特殊情况
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        result,n = [1],len(s)
        for i in range(1,n):
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1])>=10:  #判断能否组成两位数，如果可以判断是否为0
                if s[i] != '0': result.append(result[i-2]+result[i-1])
                else: result.append(result[i-2])
            else:  #否则若是0则违反规则输出0
                if s[i] != '0': result.append(result[i-1])
                else: return 0
        return result[n-1]
```
> 经过上述转移方程可以看出只需要f(n-1)和f(n-2)的值，故减少空间利用如下
```python
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        l1,l2,n = 1,1,len(s)
        for i in range(1,n):
            if int(s[i-1:i+1]) <= 26 and int(s[i-1:i+1])>=10: 
                if s[i] != '0': new = l1+l2
                else: new = l1
            else: 
                if s[i] != '0': new = l2
                else: return 0
            l1,l2 = l2,new
        return l2
```
'''
    thoughts = '动态规划问题只要思考好转移方程剩下的就比较好解决，继续加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
