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

    id = 235
    word = '面试了观远数据，感觉公司很不错，但是自己似乎说错话了，心态爆炸'
    idea = '自己的做法是对的，层序遍历但是没搞懂为啥，很迷啊，看看大家的思路吧！明白了！两结点必定位于*最近公共祖先的左右子树*上！这点很关键，那么层次遍历第一次满足的结点就是最近公共结点了！因为如果放弃了这一结点，之后的结点都无法满足这个条件了！'
    code = '''
> 按上述自己的想法
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #层序遍历可以做
        if not root: return root
        if p.val > q.val: p,q = q,p
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            if node.val<=q.val and node.val>=p.val:
                return node
```
> 递归的方法，思路更简单，从根结点开始，当前结点位于两结点中，则直接输出；否则，若当前结点小，说明两个结点在右子树上，大同理
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #迭代
        if not root: return root
        if p.val > q.val: p,q = q,p
        if root.val>=p.val and root.val<=q.val: return root
        if root.val>q.val: return self.lowestCommonAncestor(root.left,p,q)
        if root.val<p.val: return self.lowestCommonAncestor(root.right,p,q)
```
    '''
    thoughts = '希望接下来的面试顺利吧！！！二叉搜索树还要多思考！！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
