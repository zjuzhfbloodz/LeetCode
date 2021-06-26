[TOC]

# 剑指OFFER

## 原理

1. python dict和set的查询都是O(1)，因为都采用了hash的[方法](https://blog.csdn.net/zhao_crystal/article/details/82620524)



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





