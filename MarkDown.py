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

    id = 62
    word = '论文只剩实验部分，明天和朋哥交流一下，加油！就要有结果了！'
    idea = 'DP动态规划，思考好状态转移方程即可，和64题类似，比其简单'
    code = '''
> 自己的想法，从矩阵左上角走到矩阵任意元素$(p,q)$的路径为$f(p,q) = f(p-1,q),f(p,q-1)$，上述即转移方程，但是需要注意第一行和列都是1
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m列n行
        pathnum = [[1 for i in range(m)] for j in range(n)] #第一行和第一列都是1，那就都初始化为1，改剩下的
        for i in range(1,n):
            for j in range(1,m):
                pathnum[i][j] = pathnum[i-1][j] + pathnum[i][j-1]
        return pathnum[n-1][m-1]
```
> 优化操作，在一维数组也就是上述矩阵的列上操作，每次更新；感觉这个想法有一些反人类，目前还不知道为啥，但是明白是可以的
```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """优化空间复杂度为O(n)"""
        # 对二维矩阵进行压缩成一位数组,将最新生成的值覆盖掉旧的值,逐行求解当前位置的最新路径条数！
        # 实质：在于动态计算并替换当前位置下的路径数最新值
        # 状态转移公式变成：f[i] = f[i-1]+f[i]
        # 初始值： f = [1]*m,取横轴
        # f[-1]表示可能路径的总数
        # 空间复杂度：O(n),时间复杂度:O(m*n)

        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
```
'''
    thoughts = '继续完成毕业论文！加油！DP问题想法也更多了！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
