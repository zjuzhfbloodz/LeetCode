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

    id = 494
    word = '毕业论文查重似乎有很多bug，今天搞了搞google的colab，还用了用mistgpu，感觉都不错，云可以搞起来！'
    idea = 'DP动态规划，思考好状态转移方程即可，进入0-1背包问题，这个题目是自己想的，就是初始选值=0的情况比较特殊，需要分析'
    code = '''
> DP，自己的想法，详细见代码注释
```python
class Solution:
    def findTargetSumWays(self, nums,S):
        #转换成任意k个元素相加为(sum-S)/2
        sn,count,n = sum(nums),0,len(nums)
        if sn >= S and (sn - S) % 2 == 0: target = (sn - S) // 2
        else: return 0
        dp = [[0 for i in range(target + 1)] for j in range(n + 1)]
        for j in range(0,n+1):                #特殊，第一列的值不是0：如果不存在0，那么全为正号就相当于找到了0，故有1种，如果有0，就是2的0个数次方种
            if j-1 >= 0 and nums[j-1] == 0:
                count += 1
            dp[j][0] = 2 ** count
        if target == 0: return 1 * 2 ** count #如果S和Sn相等就没必要进入循环了，直接输出
        for i in range(1,n+1):
            for j in range(1,target+1):       #剩下的就是背包问题，思路一样，只不过max改为求和
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        return dp[-1][-1]
```
> DP，dalao的想法，快且少,[思路](https://leetcode-cn.com/problems/target-sum/solution/python-dfs-xiang-jie-by-jimmy00745/)，但是DP[0]的数值存疑(思考了一下似乎没问题，因为只是初始化为1，之后有0还会再做2的次方)
```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if sum(nums) < S or (sum(nums) + S) % 2 == 1: return 0
        P = (sum(nums) + S) // 2
        dp = [1] + [0 for _ in range(P)]
        for num in nums:
            for j in range(P,num-1,-1):dp[j] += dp[j - num]
        return dp[P]
```
'''
    thoughts = '背包问题有些眉目，大家推荐看背包九讲，感觉很复杂！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
