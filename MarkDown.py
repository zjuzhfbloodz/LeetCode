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

    id = 518
    word = '学多了有时总会不知所措，不知道能不能开学，要不要找工作，总之加油吧！给自己打劲儿！'
    idea = '这个题是完全背包问题，自己的思路想出来的解决方案，昨天看了看labuladong的完全背包，有收获；看[这个](https://leetcode-cn.com/problems/coin-change/solution/yong-bei-bao-wen-ti-si-xiang-lai-li-jie-ying-bi-zh/)，讲得很清楚'
    code = '''
> DP，自己的想法，DP[i]代表可以凑成钱数是i的所有方法，递推公式是对于每个coin加上DP[i-coin]；特殊情况是不能凑成，结果输出0
```python
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #完全背包问题
        dp = [0 for i in range(amount+1)]
        dp[0] = 1
        for coin in coins:
            for j in range(coin,len(dp)):
                dp[j] += dp[j-coin]
        return dp[-1]
```
'''
    thoughts = '背包问题有些理解，前两天复习了二叉树的四种遍历方法，不看就要忘了，加油吧！学习总没错的！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
