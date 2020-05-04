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

    id = 240
    word = '下雨了很凉快，即将返校！'
    idea = '这个题目想做很简单，高效的方法不好想，要学会利用这个矩阵升序的特点'
    code = '''
> 自己的想法，递归，先找到第0列中第一个比target大的元素outi，因为第0列是行中最小元素，所以outi之后的所有行都比target大，剪枝；之后找outi-1行（最后一个比target小的行）第一个比target大的元素列outj，由于outj是最右下角元素为子矩阵最大，故(outi，outj)内的元素都比target小，剪枝；递归的继续做即可
```python
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False
        #先找第一列，找到最合适的行，删去大于它的行
        outi = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                outi = i - 1
                break  
        if outi == -1: return False 
        #再找outi行第一个大的元素outj
        for j in range(len(matrix[outi])):
            if matrix[outi][j] >= target:
                outj = j
                break
        else: return False
        if matrix[outi][outj] == target: return True
        #递归
        return self.searchMatrix([x[outj:] for x in matrix[:outi+1]],target)
```
> 官方题解，思路很简洁，但是只能找左下角和右上角，因为左上角和右下角是min和max，无法移动
```python
class Solution:
    def searchMatrix(self, matrix, target):
        #找左下角和右上角，左上角和右下角不行，是min和max
        if not matrix: return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n-1
        while i < m and j >= 0:
            if target > matrix[i][j]: i += 1
            elif target < matrix[i][j]: j -= 1
            else: return True
        return False
```
    '''
    thoughts = '但行善事！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
