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

#### 18. 删除链表的节点

需要提前判断当前节点的next的val不是指定的val，个人习惯加个dummy，注意判断特殊情况（见注释）

```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if not head: return None
        dummy = ListNode()
        dummy.next = head
        node = dummy
        while node.next and node.next.val != val: #判断node.next和下面的if同作用，避免val不在
            node = node.next
        if node.next:
            node.next = node.next.next
        return dummy.next
```

#### 22. 链表中倒数第k个节点

同样是双指针，一个走得快cur的先走k步，这样cur为None时pre正好位于倒数第k

```python
class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 双指针
        if not head: return None
        pre,cur = head,head
        for i in range(k): cur = cur.next
        while cur:
            pre,cur = pre.next,cur.next
        return pre
```

#### 24. 反转链表

同样是加个dummy在前面，然后翻转即可

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head: return None
        pre,cur = None,head #None就是dummy
        while cur:
            tmp = cur.next
            cur.next = pre
            pre,cur = cur,tmp
        return pre
```

#### 25. 合并两个排序的链表

依然采用加dummy伪头节点的方法，比较熟悉

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        node = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next
        if l1: node.next = l1
        if l2: node.next = l2
        return dummy.next
```

#### 35. 复杂链表的复制

感觉一脸懵逼，后来才知道是复制一摸一样的链表，且不能是原来的那个；如果是普通链表，那么直接复制val然后next即可， 但是现在你在复制的过程中不知道random指向的val是什么，故需要两次遍历，存在dict中

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]
```



#### 52. 两个链表的第一个公共节点

两个链表连起来即可，注意如果没有交叉点也没问题，最后i==j==None也会输出

```python
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i,j = headA,headB
        while i != j:
            i = i.next if i else headB
            j = j.next if j else headA
        return i
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

#### 30. 包含min函数的栈

这个题目比较难想的就是pop的时候如何更改最小值，即如何记录除最小值之外的后续min；思路是，在当前min之后入栈的数字如果比min大，那么在他们出栈的时候min都不会改变，故他们没有记录的价值，只有比min小的才有记录的价值，因为他们出栈的时候min会自动变成当前的min，故按从大到小记录min即可

```python
class MinStack:
    # 在min值上面的元素都是没价值的，因为他们的pop不会改变min值
    def __init__(self):
        self.stack = []
        self.order = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.order or x <= self.order[-1]:
            self.order.append(x)

    def pop(self) -> None:
        a = self.stack.pop()
        if a == self.order[-1]:
            self.order.pop()

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.order[-1]
```

#### 31. 栈的压入、弹出序列

这个题目容易想复杂，实际上是通过一个辅助栈来模拟入出栈的过程（利用先入后出），按pushed的顺序入栈，遇到popped的第一个元素就要出栈了，不然后续入新的元素之后不可能是第一个出栈，最后stack为空即True

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return not stack
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



### 双指针

#### 57 - II. 和为s的连续正数序列

可以用数学方法解，也可以用双指针的方法通过滑动窗口的方式来解，i和j从1和2开始，小了j往右走，大了i往右走，求i和j之间所有数的和即可，当i==j的时候说明i-1+i>target，到达中止条件

```python
# 数学方法
class Solution:
    def findContinuousSequence(self, target: int):
        n = target // 2
        r = []
        for i in range(1,n+1):
            n_seq = ((1-2*i)+((2*i-1)**2+8*target)**0.5)/2
            if n_seq == int(n_seq):
                r.append([j for j in range(i,i+int(n_seq))])
        return r
# 双指针
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res

      
```

#### 58 - I. 翻转单词顺序

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1 # 搜索首个空格
            res.append(s[i + 1: j + 1]) # 添加单词
            while s[i] == ' ': i -= 1 # 跳过单词间空格
            j = i # j 指向下个单词的尾字符
        return ' '.join(res) # 拼接并返回
```

