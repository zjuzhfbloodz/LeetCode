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

    id = 501
    word = '昨天学习了线性SVM（软），感觉不错；今天研究研究潜变量构造！加油！'
    idea = '利用二叉搜索树中序遍历有序的特点，在遍历的过程中比较不断更新count的max；这个题目不难，但是要**不使用额外空间**还是要我想的这种比较巧妙'
    code = '''
> 上述想法，如果与max的count相同就append，否则就更新max_count和输出out
```python
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        #DFS中序遍历
        if not root: return []
        stack,node,out,outcount,this,thiscount = [],root,[],0,0,0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.val != this: #和当前值不同就更新，意味着走完了上一个数
                this = node.val
                thiscount = 0
            if node.val == this: thiscount += 1 #相同就count++
            if thiscount == outcount: out.append(this) #和max_count相同就out加上新元素
            if thiscount > outcount: out,outcount = [this],thiscount #否则舍弃之前的所有out，更新
            node = node.right
        return out
```
    '''
    thoughts = '昨天练了羽毛球感觉还是有很多不足，多练习吧！！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
