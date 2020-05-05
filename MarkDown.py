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

    id = 3
    word = '持续凉快中，今天中午和姥爷去吃自助餐烤肉！说实话有些吃吐了要，这个寒假回来吃了4次了'
    idea = '滑动窗口的题目，感觉和双指针有些像'
    code = '''
> 自己的想法，重复后两个指针都移动到前面字符串重复的元素之后一个的位置，因为那个位置是最开始不重复的，r可以往后走，但是这种方法很慢不知为何，感觉是切片慢？
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,out = 0,0,0
        while r < len(s):
            while r < len(s)-1 and s[r+1] not in s[l:r+1]:
                r += 1
            if out < r - l + 1: out = r - l + 1
            new = s[l:r+1].find(s[r+1]) + l + 1 if r < len(s) - 1 else r+1
            l = r = new
        return out
```
> 更改思路后，转变为滑动窗口，不管l是否是最优，每次+1，肯定能找到所有不重复的子串，输出最大长度即可。
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,out,n = 0,0,0,len(s)
        while l < n and r < n:
            while r+1 < n and s[r+1] not in s[l:r+1]: r += 1
            if out < r - l + 1: out = r - l + 1
            l += 1 #不管怎么样每次都+1
        return out
```
    '''
    thoughts = '似乎可以用列表或集合hashmap来优化，试了试提升不大。但行善事！加油！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
