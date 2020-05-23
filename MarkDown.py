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

    id = 416
    word = '电脑不知道能卖多少钱，今天学了word embedding一开始一头雾水，后来似乎有些理解，继续加油！'
    idea = 'DP动态规划，思考好状态转移方程即可，今天进入0-1背包问题，这个题目没太懂，看了解答懂了一些，加油！'
    code = '''
> DP，见[解答](https://leetcode-cn.com/problems/longest-common-subsequence/solution/dong-tai-gui-hua-zhi-zui-chang-gong-gong-zi-xu-lie/)
```python
class Solution(object):
    def canPartition(self, nums):
        all_sum, N = sum(nums), len(nums)
        if all_sum % 2 == 1:
            return False
        half_sum = all_sum // 2
        # flag[i][j]: 表示nums数组前i个元素是否可以表示和为j的状态True or False
        flag = [[False]*(half_sum+1) for _ in range(N)]
        # 只要nums中的元素可以组合成和为half_sum即可。同时也规定了元素不可以扩充使用，
        # 这一点和0-1背包问题不同，所以第一层遍历就是遍历nums数组，避免重复
        for i in range(N):
            for j in range(nums[i], half_sum+1):
                # 此状态说明当前元素恰好为j，直接返回True
                if j == nums[i]:
                    flag[i][j] = True
                else:
                    flag[i][j] = flag[i-1][j] or flag[i-1][j-nums[i]]
        return flag[-1][-1]
```
'''
    thoughts = '明天记得数据结构考试！！！有空就做了吧'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
