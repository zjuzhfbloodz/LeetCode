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

    id = 650
    word = '终于出去玩了一天，感觉不错！要继续努力了！'
    idea = 'DP动态规划，这个题目还可以用质因数分解的方法来做，动态规划的方法类似但是相对比较复杂'
    code = '''
> 如果n是素数，那么只能使用复制1的方式达到n；如果n是合数，要想生成n，必须通过n的质因子来合成，因为其他的都无法生成n，例如n=p*q，p和q都是质数，那么只需要p步生成p然后copy+(q-1)paste生成q个p即n，即输出为p+q。故输出就是n的质因子的和
class Solution(object):
    def minSteps(self, n):
        #这个题目就是求n的所有素因子之和
        ans = 0
        d = 2
        while n > 1:
            while n % d == 0:
                ans += d
                n /= d
            d += 1
        return ans
```
'''
    thoughts = '这个题目看似复杂，实则是数学问题，想清楚了就没问题！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
