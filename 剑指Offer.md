[TOC]

# 剑指OFFER

## 原理

1. python dict和set的查询都是O(1)，因为都采用了hash的[方法](https://blog.csdn.net/zhao_crystal/article/details/82620524)，初始化一个8行3列的数组，hash(key)得到的值i放到对应index=i的格子里，冲突的时候采取了开放寻址的方法，按一定规则找到下一个有空余的位置存放
2. Python3.6之后字典都是有序的，但是占空间更少且查询更快，[原理](https://www.cnblogs.com/xieqiankun/p/python_dict.html)



## 题目

### 数组

#### 03. 数组中重复的数字

注意用dict和set查询即可，复杂度为O(1)

```PYTHON
class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        # dict和set的查询时间都是O(1)
        dic = {}
        n = len(nums)
        for i in range(n):
            if dic.get(nums[i]):
                return nums[i]
            else:
                dic[nums[i]] = 1    
```

#### [04. 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/)

将矩阵逆时针旋转45度就变成了一个二叉树，左子树都小，右子树都大，从根节点往下扫即可，即从左下角或右上角迭代

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        x,y = n-1,0
        while x >= 0 and y < len(matrix[0]):
            if matrix[x][y] == target: return True
            elif matrix[x][y] > target: x -= 1
            else: y += 1
        return False
```

#### 29. 顺时针打印矩阵

顺时针打印遵循的顺序是右下左上，故可以设定四个方向，每次走到头或者遇到已经打印的数就换方向，直到nxm个数字都被打印出来，这是一个思路；另一个思路是右下左上走一层，往内深入一层继续迭代

```python
class Solution:
  #方法1
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]: return []
        n,m = len(matrix), len(matrix[0])
        r = []
        history = [[False for i in range(m)] for j in range(n)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        cur,di = (0,0),0 # di表示方向的index
        for i in range(n*m):
            d = directions[di]
            r.append(matrix[cur[0]][cur[1]])
            history[cur[0]][cur[1]] = True
            new = (cur[0]+d[0], cur[1]+d[1])
            if not (0<=new[0]<n and 0<=new[1]<m) or history[new[0]][new[1]]:
                di = (di+1) % 4
                d = directions[di]
                new = (cur[0]+d[0], cur[1]+d[1])
            cur = new
        return r
  #方法2
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()
        
        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom: #这层判断主要是为了排除只有一层或一列的情况
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order
```



### 链表

#### [06. 从尾到头打印链表](https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/)

练习了逆转链表，感觉性能不好，忘了可以直接用栈的方法，不过复杂度应该一样都是2O(N)，迭代法同样可解

```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        # 逆转链表，好处是不需要额外空间
        pre,cur = None,head
        r = []
        while cur:
            nex = cur.next
            cur.next = pre
            pre,cur = cur,nex
        while pre:
            r.append(pre.val)
            pre = pre.next
        return r
    # 栈
        r1 = []
        r2 = []
        while head:
            r1.append(head.val)
            head = head.next
        while r1:
            r2.append(r1.pop())
        return r2
   	#递归
        if not head: return []
        r = self.reversePrint(head.next)
        r.append(head.val)
        return r
```

### 树

#### [07. 重建二叉树](https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/)

要熟悉二叉树的前中后序遍历

```PYTHON
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder: return None
        root_val = preorder[0]
        index = inorder.index(root_val)
        left_node = self.buildTree(preorder[1:1+index], inorder[:index])
        right_node = self.buildTree(preorder[1+index:], inorder[index+1:])
        root_node = TreeNode(root_val)
        root_node.left = left_node
        root_node.right = right_node
        return root_node
```

### 堆栈

#### [09. 用两个栈实现队列](https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/)

出栈再入栈相当于反转栈，要注意的是不用每次再从2回到1，直到2用完了再找1要

```python
class CQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if len(self.s1) + len(self.s2) == 0: return -1
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
```





### 动态规划

#### 10- I. 斐波那契数列

维护一个DP数组即可，注意取模不要用1e9+7，python有bug，同10-II

```python
class Solution:
    def __init__(self,):
        self.dp = [0,1]

    def fib(self, n: int) -> int:
        if len(self.dp) > n: return int(self.dp[n] % (1000000007))
        while len(self.dp) <= n:
            cur = self.dp[-2] + self.dp[-1]
            self.dp.append(cur)
        return int(self.dp[n] % (1000000007))
```

