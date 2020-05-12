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

    id = 64
    word = '今天写完了毕设第二章的一部分，将对算法的理解用代码实现了，效果不错！明天继续写论文，后天和朋哥交流一下！加油！'
    idea = 'DP动态规划，思考好状态转移方程即可'
    code = '''
> 自己的想法，从矩阵左上角走到矩阵任意元素$(p,q)$的距离为$f(p,q) = min(f(p-1,q),f(p,q-1))+grid(p,q)$，上述即转移方程，但是需要注意第一行和列是特殊的要单独计算
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid[0]),len(grid) #m为列，n为行
        path = [[0 for i in range(m)] for j in range(n)]
        for i in range(m): path[0][i] = sum(grid[0][:i+1])
        for j in range(1,n): path[j][0] =  sum([grid[x][0] for x in range(j+1)])
        for p in range(1,n):
            for q in range(1,m):
                path[p][q] = min(path[p-1][q],path[p][q-1]) + grid[p][q]
        return path[n-1][m-1]
```
> 改进后的算法，不需要额外的矩阵空间，直接在grid上操作就行
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid[0]),len(grid) #m为列，n为行
        for i in range(1,m): grid[0][i] += grid[0][i-1]
        for j in range(1,n): grid[j][0] += grid[j-1][0]
        for p in range(1,n):
            for q in range(1,m):
                grid[p][q] = min(grid[p-1][q],grid[p][q-1]) + grid[p][q]
        return grid[n-1][m-1]
```
'''
    thoughts = '继续完成毕业论文！加油！DP问题想法也更多了！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
