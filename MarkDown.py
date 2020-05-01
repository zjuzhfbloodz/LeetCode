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

    id = 141
    word = '这两天太热了，心态也很浮躁，明天去采摘，后天几个家庭聚餐，希望过后可以踏下心来！'
    idea = '可以利用列表（哈希表）去存储，如果遇到相同的元素则有环；如果空间O(1)的话快慢指针很棒，想法也很巧妙'
    code = '''
> 上述思路，利用哈希表
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodedict,node = [],head
        while node:
            if node in nodedict: return True
            nodedict.append(node)
            node = node.next
        return False
```
> 快慢指针，两指针在环中的移动就好像两个人在跑圈，快的总会追上慢的，故当slow==fast时即有环，否则当快的到终点就是无环，很巧妙
```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            fast,slow = fast.next.next,slow.next
            if fast == slow: return True
        return False
```
    '''
    thoughts = '快慢指针是双指针很经典的思想！继续学习！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
