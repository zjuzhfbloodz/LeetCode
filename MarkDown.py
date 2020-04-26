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

    id = 109
    word = '不能吃太多，保持身材！另外继续实习祈福！'
    idea = '和108的思路差不多，不断找到中点然后递归去做，链表找中点就用快慢结点'
    code = '''
> 每次找中点作为根节点，这样可以保证左右子树的结点数相同，到只有两个叶结点的子树就必定满足**平衡**，以此类推均满足
```python
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return head
        if not head.next: return TreeNode(head.val)
        mid,beforemid = self.getMid(head)
        beforemid.next = None
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root
    #利用快慢指针找到中点，偶数是左右均可，保证平衡即可
    def getMid(self,head):
        fast,slow,lastone = head,head,head
        while fast and fast.next:
            fast = fast.next.next
            lastone = slow
            slow = slow.next
        return slow,lastone
```
> 一种不用每次找中点的方法，但是目前无法理解，应该是利用反中序遍历去做
```python
class Solution:
    def __init__(self):
        self.head = None
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        n, self.head = 0, head
        while head:
            head = head.next
            n += 1
        return self.to_bst(0, n - 1)
    def to_bst(self, left, right):
        if left > right: return
        m = (left + right) // 2
        left_child = self.to_bst(left, m - 1)
        father = TreeNode(self.head.val)
        self.head = self.head.next
        father.left = left_child
        father.right = self.to_bst(m + 1, right)
        return father
```
    '''
    thoughts = '难度比108高一些，主要是涉及到链表操作，这个题目也可以完全转化为数组去做，用空间换时间。加油！但行善事！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
