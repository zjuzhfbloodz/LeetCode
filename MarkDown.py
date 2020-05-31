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

    id = 309
    word = '卖掉了电脑，感觉有些nansou啊'
    idea = 'DP动态规划，今天进入股票问题，这个题目感觉自己想到死胡同里了，nansou'
    code = '''
> DP动态规划，labuladong写了个[股票问题解答](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/solution/yi-ge-fang-fa-tuan-mie-6-dao-gu-piao-wen-ti-by-lab/)可以看看，但是感觉这个直接从i-2拿有问题
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        dp = [[0, 0] for _ in range(n + 1)]
        prices.insert(0, 0)  # 下标1算第一天, 方便处理

        dp[1][1] = -prices[1]
        for i in range(2, n + 1):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])

        return dp[n][0]
```
> 这个解法跟自己的思想比较接近，分成三种情况来做即持有，卖了未持有，保持未持有三种状态。个人倾向这种解法
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 每天有持有，卖了未持有，保持未持有三种状态，计算出这三种状态下的最大值，就是最终结果
        # 如果今天持有，那么昨天有两种情况：
        #       1. 昨天持有，今天没有操作
        #       2. 昨天保持未持有，今天买了
        #       不存在昨天卖了未持有，今天买了的情况，因为是冷冻期
        # 在这两种情况下，取最大值，就是今天持有的最大值
        #
        # 如果今天卖了未持有，那么昨天一定是持有状态
        #
        # 如果今天保持未持有，那么昨天有两种情况
        #       1. 昨天卖了未持有，今天没操作
        #       2. 昨天本来未持有，今天没操作
        # 在这两种情况下，取最大值，就是今天未持有的最大值
        # 
        # 定义变量p1: 昨天持有的最大收益，p2: 昨天卖了未持有获取的最大收益
        # p3: 昨天保持未持有获得的最大收益
        # 今天持有的最大收益：p1 = max(p1, p3 - prices[i])
        # 今天卖了未持有的最大收益：p2 = p1 + prices[i]
        # 今天保持未持有的最大收益：p3 = max(p2, p3)
        # 
        n = len(prices)
        if n < 2:
            return 0

        p1, p2, p3 = -prices[0], 0, 0
        for i in range(1, n):
            p1, p2, p3 = max(p1, p3 - prices[i]), p1 + prices[i], max(p2, p3) #这三个状态同时计算

        return max(p1, p2, p3)
```
'''
    thoughts = '看来这个题目自己的想法没问题，就是实现上有些问题！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
