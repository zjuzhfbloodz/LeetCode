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

    id = 213
    word = '今天写完了毕设的第一章，第二章开了个头，对算法的想法有了一些新的感悟，明天把程序写完，后天希望可以和朋哥聊一聊！加油！'
    idea = '加强版抢劫，最后一个房子和第一个连起来了，只能偷其中1个或者两个都不偷'
    code = '''
> 自己的想法，分成正常和不能偷第1家两种情况，更新还是抢劫的原理，取偷当前+f(n-2)和f(n-1)的max
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        #同时记录正常和不偷1的最大值
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        f1 = (nums[0],0) #从第一家开始，正常情况max是偷第一家，第二维是不能偷第一家的max
        f2 = (max(nums[0],nums[1]),nums[1]) #第二家正常是max（0,1）在第一维，第二维不能偷第一家那么max是第二家的
        for i in range(2,len(nums)-1):
            normal = max(f2[0],f1[0]+nums[i]) #后续的更新二者就一样了，因为已经在第一家和第二家定义了不偷第1家
            nots1 = max(f2[1],f1[1]+nums[i])
            f1,f2 = f2,(normal,nots1)
        return max(f2[0],nums[-1]+f1[1])
```
> 这个解法也不错，要遍历两次，所以时间复杂度高，但是空间复杂度低一些。原理是所有情况可以分解为：不抢1和不抢最后一间的两种情况（其实和我的想法是一样的，只不过实现层面不一样），故分别做[1:]和[:-1]即可，[参考](https://leetcode-cn.com/problems/house-robber-ii/solution/213-da-jia-jie-she-iidong-tai-gui-hua-jie-gou-hua-/)
```python
class Solution:
    def rob(self, nums: [int]) -> int:
        def my_rob(nums):
            cur, pre = 0, 0
            for num in nums:
                cur, pre = max(pre + num, cur), cur
            return cur
        return max(my_rob(nums[:-1]),my_rob(nums[1:])) if len(nums) != 1 else nums[0]
```
'''
    thoughts = '明天写实验部分剩下的代码，希望顺利！！'
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
