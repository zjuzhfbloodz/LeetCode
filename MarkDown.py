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

    id = 538
    word = '他们说新加坡不开学了改上网课，我心态爆炸'
    idea = 'BST采取右-根-左的中序遍历就是从大到小，然后用bigger累加比当前结点大的，加到当前结点即可'
    code = '''
> 按上述自己的想法
```python
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return
        #右-根-左的中序遍历
        stack,node,bigger = [],root,0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            node.val += bigger #每次加bigger
            bigger = node.val #更新bigger
            node = node.left
        return root
```
> 递归的方法，思路和上述一致，只是写起来简单但是复杂度高一些
```python
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.num = 0
        def depthfirstsearch(root):
            if root is None:
                return 
            else:
                depthfirstsearch(root.right)
                self.num = self.num + root.val
                root.val = self.num
                depthfirstsearch(root.left)
                return root
        return depthfirstsearch(root)
```
    '''
    thoughts = '中序遍历的确可以解决很多BST的问题！希望NUS按时开学啊！！！不要延后好不好，心态炸了！！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
