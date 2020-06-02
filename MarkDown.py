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

    id = 188
    word = '今天开始构思毕业答辩的PPT！'
    idea = 'DP动态规划，股票问题k次交易是最hard的问题，见[解答](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/solution/gu-piao-jiao-yi-xi-lie-cong-tan-xin-dao-dong-tai-g/)'
    code = '''
> DP动态规划，还是labuladong的方法，如果k>=n//2就相当于是不限制交易次数，其他就和123的k==2一样。见[股票问题解答](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/gu-piao-jiao-yi-xi-lie-tan-xin-si-xiang-he-dong-2/)
```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0

        if k >= n//2:   # 退化为不限制交易次数，找正值即可
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        else:           # 限制交易次数为k
            dp = [[[None, None] for _ in range(k+1)] for _ in range(n)]  # (n, k+1, 2)
            for i in range(n):
                dp[i][0][0] = 0
                dp[i][0][1] = -float('inf')
            for j in range(1, k+1): #这里第一天的时候可以交易k次（同价买卖）是为了取交易1-k次的max，这样最后的max是交易最多k次的max
                dp[0][j][0] = 0
                dp[0][j][1] = -prices[0]
            for i in range(1, n):
                for j in range(1, k+1):
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
            return dp[-1][-1][0]
```
'''
    thoughts = '个人觉得需要思考的地方还是初始化部分，要理解！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
