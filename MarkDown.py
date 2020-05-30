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

    id = 121
    word = '昨天和gsszzr一起去打了球，感觉不错；昨晚睡了8个小时，争取早睡！'
    idea = 'DP动态规划，今天进入股票问题，这个题目其实也可以用最大子序列和来做'
    code = '''
> 最大子序列和问题，只要当前子序列的和大于0,他就对最大子序列和有贡献故继续走；一旦小于0就放弃之前的重新开始；据说叫[Kadane算法](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/kadanesuan-fa-shi-jian-on-kong-jian-o1-by-chxj1992/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        prev = prices[0]
        max_profit = 0
        max_here = 0
        for t in prices[1:]:
            x = t - prev
            prev = t
            max_here = max_here + x if max_here > 0 else x
            max_profit = max(max_profit, max_here)
        return max_profit
```
> DP动态规划解法，dp[i]是前i天的最大利润，要有一个记录最小价格的minprice，dp[i] = max(dp[i-1],prices[i]-minprice)。[解析](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/solution/gu-piao-wen-ti-python3-c-by-z1m/)
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 0: return 0 # 边界条件
        dp = [0] * n
        minprice = prices[0] 

        for i in range(1, n):
            minprice = min(minprice, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - minprice)

        return dp[-1]
```
'''
    thoughts = '进军股票问题，感觉就是时间序列类问题，加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
