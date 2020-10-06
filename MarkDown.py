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
        
        shutil.copy(file_path,'D:\Data\Markdown\LEETCODE')
            

if __name__ == "__main__":

<<<<<<< HEAD
    id = 455
    word = '转眼间已经开学两个月，NUS的midterm都过去了，太快了，瘸腿在家休息，但是学习不能落下，遂捡起leetcode'
    idea = '贪心算法，我的思路是从大到小（因为不能给小的比他大太多的），但是大家都是从小到大'
    code = '''
> 从大到小排序孩子和糖果，依次检索，如果当前孩子不够吃就不给这个孩子了，够吃就都+1，最后糖果划过的窗口数就是喂了的孩子数。
```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g,reverse=True)
        s = sorted(s,reverse=True)
        i,j = 0,0 #i代表孩子指针，j代表食物指针同时也是已经喂孩子的量
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                j += 1
            i += 1
        return j
```
'''
    thoughts = '之前做的也还没复习完，这次想先从DP动态规划入手开始学起'
=======
    id = 34
    word = '电脑到了！感觉不错！不知科研助理如何说法！问问朋哥吧！'
    idea = '进入二分查找部分，这个题目就是利用二分查找找到左右区间的两端'
    code = '''
> 我的想法是先找到等于target的元素（如果没找到说明没有），然后再分别从(l,target)和(target,r)中二分查找找到端点，感觉也不错
```python
#思路是RBK格式的就不放了，其实一样
```
> 一个比较成熟的专门找左右端点的方法，labuladong总结的[这里](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/)
```python
class Solution(object):
    def searchRange(self, nums, target):
        return [self.left_bound(nums,target), self.right_bound(nums,target)]
    #找右边端点
    def right_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if right >= 0 and nums[right] == target: return right # 注意
        else: return -1
    #找左边端点
    def left_bound(self, nums, target):
        if len(nums) == 0:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        if left <= len(nums)-1 and nums[left] == target: return left  # 注意
        else: return -1
```
'''
    thoughts = '既然一时间找不到工作就先把比赛搞搞好！努力总会有结果！加油！'
>>>>>>> a5d1982fcd20a0f5476b3fa5319bfdb9fe80cfe3
    mk = Markdown(id,word,idea,code,thoughts)
    mk.create_solution()
