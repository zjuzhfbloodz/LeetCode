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

    id = 345
    word = '昨天去动物园玩了很开心，希望大家都有个好的未来吧！'
    idea = '逆序的题目可以用双指针去做，也可以用栈实现逆序'
    code = '''
> 双指针的思路，一次遍历，应该是最优解
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r,vowel,s = 0,len(s)-1,'AEIOUaeiou',list(s)
        while True:
            while l < r and s[l] not in vowel: l += 1 #先找左边第一个元音字母
            if l >= r: break
            while s[r] not in vowel: r -= 1 #找右边的，然后交换顺序，之后记得l往后，r往前
            s[l], s[r] = s[r], s[l]
            l,r = l+1,r-1
        return ''.join(s)
```
> 栈的思路，更简单明了一些，复杂度相对高一些
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        x= 'aeiouAEIOU'
        res=[]
        ls=[i for i in s if i in x] #用栈来存放元音字母    
        for k in s:
            if k not in x: res.append(k)
            else: res.append(ls.pop()) #是元音字母则用栈来逆序      
        return ''.join(res)
```
    '''
    thoughts = '双指针可以用于逆序！又收获一种方法！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
