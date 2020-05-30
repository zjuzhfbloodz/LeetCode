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

    id = 122
    word = '昨天和gsszzr一起去打了球，感觉不错；昨晚睡了8个小时，争取早睡！'
    idea = 'DP动态规划，今天进入股票问题，这个题目和121类似，可以用最大子序列和来做'
    code = '''
> 最大子序列和问题，自己的想法。和题目121相似，天数之间做差，求最大子序列和。但是因为题目不像121那样限制一笔交易（就像最大子列和不要求子列连续一样，那肯定是加所有正数），故可以不要两天价差是负数的情况（一旦出现负数我肯定前一天就卖掉，然后今天再买入），也就是只加价差大于0的情况。其实更简单一些，详细[可见](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/best-time-to-buy-and-sell-stock-ii-zhuan-hua-fa-ji/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i in range(1,len(prices)):
            today = prices[i] - prices[i-1]
            if today > 0: output += today
        return output
```
> DP动态规划解法，dp[i][0 or 1]代表第i天有没有股票时的最大收益，最后返回dp[-1][0]即可，[详细见](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/gu-piao-jiao-yi-xi-lie-tan-xin-si-xiang-he-dong-2/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n): #今天没有可能是昨天也没有或昨天有但是今天卖了；今天有可能是昨天也有或者昨天没有今天买了，求max
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]    # 返回最后一天且手上没有股票时的获利情况
```
'''
    thoughts = '进军股票问题，时间序列类解法和DP动态规划都可以解答，时间序列方法就是需要动脑子思考，DP相对机械一些，加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
