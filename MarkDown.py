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

    id = 236
    word = '今天大学习才知道中国是世界唯一拥有全工业部门的国家，厉害！坦然面对面试结果！总是有收获的！'
    idea = '**最近公共祖先**一个很重要的思路是：两结点必定位于该祖先的左右子树，这是一个结论性的东西。'
    code = '''
> 自己的想法，有些愚蠢，层序遍历记录所有结点到根结点的path，然后找到p和q的从根结点开始对比，直到最后一个相同即为结果
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return root
        queue,pp,pq = [(root,[root])],[],[]
        while queue:
            node,path = queue.pop(0)
            if node.left: queue.append((node.left,path+[node.left]))
            if node.right: queue.append((node.right,path+[node.right]))
            if node == p: pp = path
            if node == q: pq = path
            if pp and pq: break
        minlen = min(len(pp),len(pq))
        for i in range(minlen):
            if pp[i].val != pq[i].val:
                return pp[i-1]
        else: return pp[i]
```
> 更巧妙的方法，只记录每个结点的父结点，然后当成链表一样逐层回溯，题目转化为160相交链表的操作，将两个链表合并（此时长度相同，如果后端有相同必然在最后一致）找到第一个相同点即可
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dic,queue = {root:None},[root]
        while queue:
            node = queue.pop(0)
            if node.left:
                dic[node.left] = node
                queue.append(node.left)
            if node.right:
                dic[node.right] = node
                queue.append(node.right)
        l1,l2 = p,q
        while l1 != l2:
            l1 = dic.get(l1,q) #参考160相交链表
            l2 = dic.get(l2,p)
        return l1
```
> 递归，如果当前结点是p或q，返回当前结点就是结果；否则去左右子树找，利用**两结点必定位于最近祖先的左右**的特点，如果在左右子树找到则返回根结点，否则返回找到的left或right
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```
    '''
    thoughts = '这个题目第一次看到没什么思路，面试应该问的比较多，理解并牢记！但行善事，莫问前程！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
