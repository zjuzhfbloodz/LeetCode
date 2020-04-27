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

    id = 653
    word = '屁股总是疼，昨天回忆了申请的过程，很受用，加油！'
    idea = '自己想的方法没用到BST的特点，第二种方法用到了，但是感觉似乎复杂度差不多？'
    code = '''
> BFS层次遍历，累次记录下当前结点前的所有结点值，遍历到当前结点时只需看k-node.val在不在集合中即可，复杂度O(N)，一次遍历完事儿
```python
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        queue,vals = [root],[]
        while queue:
            node = queue.pop(0)
            #看看当前集合中有没有能和当前结点和为k的，有就终止，没有继续
            if k-node.val in vals: return True
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            #将当前结点值加入集合
            vals.append(node.val)
        return False   
```
> BST中序遍历有序，初始两个点为头结点l和末端结点r，比k大则r-1（因为l一开始是最小不能再减小了，而l变大只有在l+r大于k时，所以此后l都不可能减小了），比k小则l+1，直到l+r==k为止，否则输出False
```python
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root: return False
        nodelist = self.inorder(root)
        l,r = 0,len(nodelist)-1
        while l < r:
            if nodelist[l] + nodelist[r] > k: r -= 1
            elif nodelist[l] + nodelist[r] < k: l += 1
            else: return True
        return False
    #BFS中序遍历
    def inorder(self,root):
        l = []
        stack,node = [],root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            l.append(node.val)
            node = node.right
        return l
```
    '''
    thoughts = '题目不难，几种方法的复杂度也都大同小异，当然是利用了BST特点的比较巧妙！加油！但行善事！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
