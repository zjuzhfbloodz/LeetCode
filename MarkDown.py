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

    id = 524
    word = '今天陪爷爷出去玩，到了梁庄，买了柿桃，中午吃了饸烙和驴肉火烧，下午去采摘了草莓！爷爷很开心，我也很高兴！计划去草原玩！'
    idea = '双指针做很简单，分别判断d中的每个word是否是s的子序列，然后输出长度最长and字典序最小的一个'
    code = '''
> 上述思路，自己的想法
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
    def findLongestWord(self, s: str, d: List[str]) -> str:
        out = '' #定义输出，初始化为字符串
        for word in d:
            l,r = 0,0
            #先判断当前单词是否符合覆盖out的条件，满足再判断是否在s中
            flag = True if len(word) > len(out) or len(word) == len(out) and word < out else False
            #判断是否在s中，若是lr均+1，否则只有l+1
            while  flag and l < len(s) and r < len(word) and word[r] in s:
                if s[l] == word[r]: r += 1
                l += 1
            #只有r==len(word)时才确定word在s中，替代
            if r == len(word): out = word
        return out
```
> 先用sort函数分别按照字符串长度和字典序方向排序，之后再做，遇到匹配的直接输出就行，复杂度差不多
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        #先sort排序，将lambda函数定义为字符串长度和字典序，速度差不多
        d.sort(key = lambda x: [-len(x), x])
        for word in d:
            a,b = 0,0
            while a < len(s) and b < len(word):
                if s[a] == word[b]: b += 1
                a += 1
            if len(word) == b: return word
        return ''
```
> 这个dalao用的find函数，速度快的飞起，每次查到word中的每个字母在s中的位置为k，更新为k+1继续查找即可，遇到查不到的就不匹配
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: [-len(x), x])#对字典d进行排序，第一关键字是长度升序，第二关键字是字符串本身字典序
        def f(c):                   #匹配函数
            i = 0
            for j in c:             #遍历单词里的字母
                k = s.find(j, i)    #查找函数，后一个参数是查找起点
                if k == -1:
                    return False    #查找失败就返回错误
                i = k + 1           #查找成功就更新查找起点
            return True
        for c in d:                 #遍历有序字典里的单词
            if f(c):                #如果匹配就返回单词
                return c
        return ''
```
    '''
    thoughts = '双指针思想解决很多问题很棒，今天很累，但是很开心！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
