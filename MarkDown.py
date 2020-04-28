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

    id = 783
    word = '毕业论文初稿5.17交，做起来！交上去压力就给老师了！昨天学了SVM第一节，感觉不错！继续加油！'
    idea = '利用二叉搜索树中序遍历有序的特点，差的绝对值最小只有可能在中序遍历**相邻两元素间**产生'
    code = '''
> 上述想法，中序遍历的过程中两两做差和min比较即可，最后输出最小值
```python
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        stack,out,node,last = [],float('inf'),root,-float('inf')
        while stack or node: #中序遍历
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val - last < out: #last表示上一个node的值，用当前node-last为相邻两结点差，和out比较即可
                out = node.val - last
            node,last = node.right,node.val
        return out  
```
    '''
    thoughts = '能想到BST的中序遍历有序这个题目就不难，但行善事！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
