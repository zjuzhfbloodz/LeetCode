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

感觉一脸懵逼，后来才知道是复制一模一样的链表，且不能是原来的那个；如果是普通链表，那么直接复制val然后next即可， 但是现在你在复制的过程中不知道random指向的val是什么，故需要两次遍历，存在dict中

```python
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head: return
        hashmap = {}
        node = head
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        while node:
            hashmap[node] = Node(x=node.val)
            node= node.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            hashmap[cur].next = hashmap.get(cur.next,None)
            hashmap[cur].random = hashmap.get(cur.random,None)
            cur = cur.next
        # 5. 返回新链表的头节点
        return hashmap[head]
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

#### [剑指 Offer 28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/)

内置一个判断左右子树是否为镜像二叉树的函数，如果节点值相等，转到左左右右和左右右左

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        def inner(left,right):
            if not left and not right: return True
            if not left or not right: return False
            if left.val == right.val:
                return inner(left.right,right.left) and inner(left.left,right.right)
            return False
        return inner(root.left,root.right)
```

- 依次是：普通层序，分层层序，之字形层序

#### [剑指 Offer 32 - I. 从上到下打印二叉树](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        #层序遍历
        if not root: return []
        queue = [root]
        output = []
        while queue:
            node = queue.pop(0)
            output.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return output
```

#### [剑指 Offer 32 - II. 从上到下打印二叉树 II](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #层序遍历
        if not root: return []
        queue = [(root,0)]
        depth = -1
        output = []
        while queue:
            node,d = queue.pop(0)
            if d > depth:
                depth = d
                output.append([])
            output[-1].append(node.val)
            if node.left: queue.append((node.left,d+1))
            if node.right: queue.append((node.right,d+1))
        return output
```

#### [剑指 Offer 32 - III. 从上到下打印二叉树 III](https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/)

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        #层序遍历
        if not root: return []
        queue = [(root,0)]
        depth = -1
        output = []
        while queue:
            node,d = queue.pop(0)
            if d > depth:
                depth = d
                output.append([])
            if d%2 == 1:
                output[-1].insert(0,node.val)
            else:
                output[-1].append(node.val)
            if node.left: queue.append((node.left,d+1))
            if node.right: queue.append((node.right,d+1))
        return output
```



#### [*剑指 Offer 33. 二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/)

后序遍历左-右-根，先判断左<根且右>根，如果这个都不满足就False，否则继续判断左和右是不是，终止条件就是一个节点的时候

```python
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            p = i
            while postorder[p] < postorder[j]: p += 1
            m = p
            while postorder[p] > postorder[j]: p += 1
            return p == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)
```



#### [剑指 Offer 34. 二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/)

DFS和BFS都可以做

```python
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        output = []
        def dfs(root,target,path):
            if not root: return 
            path.append(root.val)
            if root.val == target and not root.left and not root.right: 
                output.append(path[:])
            dfs(root.left,target-root.val,path[:])
            dfs(root.right,target-root.val,path[:])
        dfs(root,target,[])
        return output
```



#### [剑指 Offer 37. 序列化二叉树](https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/)

层序遍历，空为None；反序列的时候同样走一次层序遍历

```python
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        output = []
        while queue:
            node = queue.pop(0)
            if not node:
                output.append('null')
            else:
                output.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ' '.join(output)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(' ')
        if data == ['null']: return None
        root = TreeNode(int(data.pop(0)))
        queue = [root]
        while queue:
            node = queue.pop(0)
            leftval = data.pop(0)
            if leftval == 'null':
                node.left = None
            else:
                left = TreeNode(int(leftval))
                node.left = left
                queue.append(left)
            rightval = data.pop(0)
            if rightval == 'null':
                node.right = None
            else:
                right = TreeNode(int(rightval))
                node.right = right
                queue.append(right)
        return root
            

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
```



#### [剑指 Offer 68 - I. 二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

利用二叉搜索树性质去找

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return
        if p.val > q.val: p,q = q,p
        if p.val <= root.val <= q.val: return root
        elif root.val < p.val: return self.lowestCommonAncestor(root.right,p,q)
        else: return self.lowestCommonAncestor(root.left,p,q)
```



#### [剑指 Offer 68 - II. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/)

祖先要么==p要么==q，要么p和q在祖先的左右子树上，递归找下去即可

```python
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #p和q在祖先的左右子树上
        if not root: return 
        if root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if left and right: return root
        if left: return left
        return right
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

#### [剑指 Offer 42. 连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/)

DP或者前缀和

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #DP也行
        #前缀和？
        if not nums: return 0
        n = len(nums)
        minsum = min(nums[0],0)
        output = nums[0]
        cursum = nums[0]
        for i in range(1,n):
            cursum += nums[i]
            output = max(output,cursum-minsum)
            minsum = min(minsum,cursum)
        return output
```

#### [剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/)

动态规划，注意506这种06不能翻译为6

```python
class Solution:
    def translateNum(self, num: int) -> int:
        #DP，DP[i]表示nums[:i]有几种翻译方式
        num = list(str(num))
        n = len(num)
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] += dp[i-1]
            if 9 < int(num[i-2] + num[i-1]) < 26:
                dp[i] += dp[i-2]
        return dp[-1]


```

#### [剑指 Offer 47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/)

可以优化到1D

```python
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        dp = []
        r = 0
        for i in range(n):
            r += grid[0][i]
            dp.append(r)
        for i in range(1,m):
            for j in range(n):
                if j == 0:
                    dp[j] += grid[i][j]
                else:
                    dp[j] = max(dp[j],dp[j-1]) + grid[i][j]
        return dp[-1]
```



#### [剑指 Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

n=1易得，n=2可以看作在1的基础上又投了一次骰子，故1/6的概率+1+2+3+4+5+6，滑动窗口依次加上

```python
class Solution:
    def dicesProbability(self, n: int):
        dp = [1/6 for _ in range(6)]
        for i in range(1,n):
            newdp = [0 for _ in range(6+5*i)] #新的是6+5i种可能
            for j in range(6):
                k = len(dp)
                for x in range(k):
                    newdp[j+x] += dp[x]*1/6 #第i颗骰子有1-6种可能，故滑动加即可
            dp = newdp
        return dp
```



### 双指针&滑动窗口

#### [剑指 Offer 48. 最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/)

同lc3，滑动窗口，可以用字典存储

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        hashmap = {}
        l = 0
        output = 0
        for r in range(n):
            if s[r] in hashmap:
                output = max(output,len(hashmap))
                index = hashmap[s[r]]
                for i in range(l,index+1):
                    hashmap.pop(s[i])
                l = index+1
            hashmap[s[r]] = r
        return max(output,len(hashmap))
```

#### [*剑指 Offer 49. 丑数](https://leetcode-cn.com/problems/chou-shu-lcof/)

dp[i]只能是从之前数的235倍得到，故构造三指针，每次用过了之后就要+1，表示下一个可以被235乘的数

```python
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]
```



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



### 字符串

#### [剑指 Offer 67. 把字符串转换成整数](https://leetcode-cn.com/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/)

考虑空字符串，空格字符串，首字母可以是+-但仅有一个+-不行

```python
class Solution:
    def strToInt(self, str: str) -> int:
        s = [x for x in str.split(' ') if x]
        if not s: return 0
        s = s[0]
        if s[0] not in ['-','+'] and not s[0].isdigit():
            return 0
        n = len(s)
        i = 1
        while i < n:
            if s[i].isdigit():
                i += 1
            else: break
        if i == 1 and s[0] in ['-','+']: return 0 #仅有一个+-，排除
        s = int(s[:i])
        if s < -1*2**31:
            return -1*2**31
        else:
            return min(s,2**31-1)
```

### 贪心算法

#### [剑指 Offer 63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

每天卖出的最大值等于当天-前i天的最小值

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        n = len(prices)
        minprice = prices[0]
        output = 0
        for i in range(n):
            if prices[i] > minprice:
                output = max(output,prices[i]-minprice)
            else:
                minprice = prices[i]
        return output
```

### 数学

#### [剑指 Offer 39. 数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)

投票法，超过半数一定比其他所有的-1都大

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums: return
        n = len(nums)
        can = -1
        count = 0
        for i in range(n):
            if count == 0:
                can = nums[i]
                count += 1
                continue
            if nums[i] == can:
                count += 1
            else:
                count -= 1
        return can
```



#### [*剑指 Offer 43. 1～n 整数中 1 出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)

分别计算1-n中每一位上的数字1的个数如1234中十位上1的个数，1200中每100个包含完整的10个10-19，34如果超过20也包含10个，否则有几个算几个。

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        # mulk 表示 10^k
        # 在下面的代码中，可以发现 k 并没有被直接使用到（都是使用 10^k）
        # 但为了让代码看起来更加直观，这里保留了 k
        k, mulk = 0, 1
        ans = 0
        while n >= mulk:
            ans += (n // (mulk * 10)) * mulk + min(max(n % (mulk * 10) - mulk + 1, 0), mulk)
            k += 1
            mulk *= 10
        return ans
```

#### [剑指 Offer 44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

确定位数+确定数值+确定数字位置

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        r = 9
        while n >= r*digits:
            n -= r*digits
            r *= 10
            digits += 1
        value = 10**(digits-1)+n//digits
        #print(value,n)
        if n%digits == 0: 
            value -= 1
        #确定数字位置
        index = n%digits
        return int(str(value)[index-1])
```

#### [剑指 Offer 45. 把数组排成最小的数](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)

字符串排序，高位值大的在前面，注意3和31或3和34这种需要比较之后再放，故使用cmp_to_key的函数

```python
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rule(x, y):
            a, b = x + y, y + x
            if a > b: return 1
            elif a < b: return -1
            else: return 0
        
        strs = [str(num) for num in nums]
        strs.sort(key = functools.cmp_to_key(sort_rule))
        return ''.join(strs)
```



#### [剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

f(n)=(f(n-1)+m)%n，递推即可[思路](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/jian-zhi-offer-62-yuan-quan-zhong-zui-ho-dcow/)

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        #
        x = 0
        for i in range(2,n+1):
            x = (x+m)%i
        return x
```



### 搜索&回溯

#### [剑指 Offer 38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)

类似全排列，但是有重复字符，故加一个验证：即同一位置不能有同样的字符出现两次

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        #回溯
        n = len(s)
        output = []
        s = list(s)
        def traceback(index):
            if index == n:
                output.append(''.join(s[:]))
                return
            r = set()
            for i in range(index,n):
                if s[i] in r:  #即同一位置不能有同样的字符出现两次
                    continue
                r.add(s[i])
                s[index],s[i] = s[i],s[index]
                traceback(index+1)
                s[index],s[i] = s[i],s[index]
        traceback(0)
        return output
```



### 其他

#### [剑指 Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

前缀和，两次遍历，一次乘左侧的乘积，一次乘右侧的乘积

```python
class Solution:
    def constructArr(self, a):
        #两次遍历
        n = len(a)
        b = [1 for _ in range(n)]
        lefts = 1
        for i in range(n):
            b[i] *= lefts
            lefts *= a[i]
        rights = 1
        for j in range(n-1,-1,-1):
            b[j] *= rights
            rights *= a[j]
        return b
```

#### [剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C），故采用and中的判断来终止迭代

```python
class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:
        n > 1 and self.sumNums(n - 1)
        #print(n)
        self.res += n
        return self.res
```

#### [剑指 Offer 61. 扑克牌中的顺子](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)

我是依次把空缺的牌填上大小王0，如果不够了就是False，否则是True

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] == 0:
                count += 1
            else: break
        for j in range(count,n-1):
            gap = nums[j+1] - nums[j]
            if gap == 1:
                continue
            elif gap == 0:
                return False
            else:
                count -= gap-1
                if count < 0:
                    return False
        return True
#新思路，只要最大牌-最小牌 < 5即可，最小牌就是joke的数量+1-1的位置
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        joker = 0
        nums.sort() # 数组排序
        for i in range(4):
            if nums[i] == 0: joker += 1 # 统计大小王数量
            elif nums[i] == nums[i + 1]: return False # 若有重复，提前返回 false
        return nums[4] - nums[joker] < 5 # 最大牌 - 最小牌 < 5 则可构成顺子

```

