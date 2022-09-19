[toc]
# 贪心算法

#### [455. 分发饼干](https://leetcode.cn/problems/assign-cookies/)

- 因为考虑满足孩子的数量最大，故先满足小的好，这就是贪心
- 可以通过排序+双指针的方法进行贪心的过程

```python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #因为是数量，故先满足小的好
        #双指针？
        g,s = sorted(g),sorted(s)
        m,n = len(g),len(s)
        l,r = 0,0
        while l < m and r < n:
            while r < n and g[l] > s[r]:
                r += 1
            if r < n:
                l += 1
                r += 1
        return l
```



#### [435. 无重叠区间](https://leetcode.cn/problems/non-overlapping-intervals/)

- 自己的方法，按照传统左区间进行排序（会出现前包后的情况，判断if条件更多，但是复杂度一样），思路很清晰，站在后面判断能否进去

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # 类似刚才的孩子发🍬，因为是最小数量，故排序后越宽的(位于后面)越要移除，贪心思想
        # 针对某一个区间，遍历后面，遇到小的就把自己删除，直到后面的和自己无冲突
        # 应该站在后面看前面，这样比较容易判断
        intervals = sorted(intervals)
        n = len(intervals)
        output = 0
        index = 0
        for i in range(1,n):
            if intervals[i][1] <= intervals[index][1]: # 前包后
                output += 1
                index = i
            elif intervals[i][0] < intervals[index][1]: # 交叉
                output += 1
            else:
                index = i
        return output
```

- 更巧妙的方法，按右区间排序，这样只用判断左区间是否满足情况，不会存在前包后的情况

```python
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals,key=lambda x:x[1])
        n = len(intervals)
        r = [intervals[0]]
        for i in range(1,n):
            if intervals[i][1] == r[-1][1]:
                continue
            if intervals[i][0] >= r[-1][1]:
                r.append(intervals[i])
        return n-len(r)
```



#### [452. 用最少数量的箭引爆气球](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/)

- 类似删除区间，找区间的并集，如果在里面不用更新，否则需要更新；同样右区间判断更简单些

```python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda balloon: balloon[1])
        pos = points[0][1]
        ans = 1
        for balloon in points:
            if balloon[0] > pos:
                pos = balloon[1]
                ans += 1
        
        return ans
```

#### [406. 根据身高重建队列](https://leetcode.cn/problems/queue-reconstruction-by-height/)

- 矮的人对高的人的排序不影响，故按身高逆序排，排在前面的位置就确定了，只需要遍历后面的，后面的第二个值就是index

- 我们先按照身高从大到小排序（身高相同的情况下K小的在前面），这样的话，无论哪个人的身高都小于等于他前面人的身高。所以接下来只要按照K值将他插入相应的位置就可以了。
  例如：示例1排完序：[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

  新建一个二维vector：
  [7,0]插入第0的位置
  [7,1]插入第1的位置
  [6,1]插入第1的位置，这时[7,1]就往后移一位了

```python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        #一层一层的排序，复杂度是o(N2)
        #每一层的相对排序是正确的，是无序的
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        n = len(people)
        ans = list()
        for person in people:
            ans[person[1]:person[1]] = [person]
        return ans
```



#### [121. 买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/)

- 按卖出遍历，不断更新k天前的最小值，然后用第k天的price更新output

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        output = 0
        for p in prices:
            output = max(output,p-min_price)
            min_price = min(p,min_price)
        return output
```

#### [122. 买卖股票的最佳时机 II](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-ii/)

- 不限制次数交易，只要后一天比前一天价格高就买入然后卖出

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #只要赚钱就能买
        output = 0
        n = len(prices)
        for i in range(1,n):
            output += max(0,prices[i]-prices[i-1])
        return output
```

#### [392. 判断子序列](https://leetcode.cn/problems/is-subsequence/)

- 双指针，没啥说的

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n,m = len(s),len(t)
        p1,p2 = 0,0
        while p1 < n and p2 < m:
            if s[p1] == t[p2]:
                p1 += 1
            p2 += 1
        return True if p1 == n else False
```

#### [665. 非递减数列](https://leetcode.cn/problems/non-decreasing-array/)

- 因为不是删除，所以要注意犯错的时候的更改措施，需要让之前和之后的序列保证一致

```python
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        flag = 1
        index = 0
        while index < n-1:
            if nums[index] > nums[index+1]:
                if flag:
                    flag = 0
                    if index == 0 or nums[index+1] >= nums[index-1]:
                        nums[index] = nums[index+1]
                    else:
                        nums[index+1] = nums[index]
                else:
                    return False
            else:
                pass
            index += 1
        return True
```

#### [763. 划分字母区间](https://leetcode.cn/problems/partition-labels/)

- 写的稍微有一些麻烦，原理是记录下每个字母的最后位置，然后遍历更新end，如果end==i就说明可以了，否则继续更新

```python
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #用哈希表来存储每个字母的最后位置
        last_dict = {}
        first_lst = []
        output = []
        n = len(s)
        for i in range(n):
            if s[i] not in last_dict:
                first_lst.append([i,s[i]])
            last_dict[s[i]] = i
        def update_interval(start,end):
            nonlocal first_lst
            k = len(first_lst)
            for i in range(k):
                index,alpha = first_lst[i]
                if index <= end:
                    end = max(end,last_dict[alpha])
                else:
                    break
            first_lst = first_lst[i:]
            return end
        start = 0
        while start < n:
            end = last_dict[s[start]]
            new_end = update_interval(start,end)
            output.append(new_end-start+1)
            start = new_end+1
        return output
```

# 分治

#### [241. 为运算表达式设计优先级](https://leetcode.cn/problems/different-ways-to-add-parentheses/)

- 分治的思想，将运算符左右两边的表达式分别计算结果，然后再计算当前表达式的结果即可

```python
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if len(expression) <= 3:
            return [eval(expression)]
        n = len(expression)
        output = []
        for i in range(n):
            if expression[i] in {'*','+','-'}:
                left_r = self.diffWaysToCompute(expression[:i])
                right_r = self.diffWaysToCompute(expression[i+1:])
                for l in left_r:
                    for r in right_r:
                        if expression[i] == '*':
                            output.append(l*r)
                        elif expression[i] == '+':
                            output.append(l+r)
                        else:
                            output.append(l-r)
        return output
```



#### [95. 不同的二叉搜索树 II](https://leetcode.cn/problems/unique-binary-search-trees-ii/)

- 分治思想，用DP不好做；**但切记root要放在每个子循环中更新，不然id是一个，list装的一样**

```python
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def inner(s,e):
            if s > e:
                return [None]
            elif e == s:
                return [TreeNode(val=s)]
            output = []
            for i in range(s,e+1):
                
                left = inner(s,i-1)
                right = inner(i+1,e)
                for l in left:
                    for r in right:
                        root = TreeNode(val=i)
                        root.left = l
                        root.right = r
                        output.append(root)
            return output

        return inner(1,n)

```



# 搜索

## BFS

#### [127. 单词接龙](https://leetcode.cn/problems/word-ladder/)

- 最短+状态转移=BFS，目前使用的是朴素的26个字母遍历思想，还可以优化为建图比如hit和\*it/h\*t/hi\*的链接表示可以通过一个字母变化

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # 确实类似BFS问题
        direction = [chr(i) for i in range(ord('a'),ord('z')+1)]
        wordSet = set(wordList)
        output = 1
        visited = set([beginWord])
        stack = [(beginWord,1)]
        step = 1
        while stack:
            tmp_stack = []
            for w,step in stack:
                if w == endWord:
                    return step
                alpha_lst = list(w)
                for a in range(len(alpha_lst)):
                    for d in direction:
                        new_word_lst = alpha_lst[:]
                        new_word_lst[a] = d
                        new_word = "".join(new_word_lst)
                        if new_word in wordSet and new_word not in visited:
                            tmp_stack.append((new_word,step+1))
                            visited.add(new_word)
            stack = tmp_stack
        return 0
```

#### [1091. 二进制矩阵中的最短路径](https://leetcode.cn/problems/shortest-path-in-binary-matrix/)

- 标准BFS，八个方向

```python
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #BFS
        m,n = len(grid),len(grid[0])
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        stack = [(0,0,0)]
        ds = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        step = 0
        while stack:
            new_stack = []
            for i,j,step in stack:
                if i == m-1 and j == n-1:
                    return step+1
                for di,dj in ds:
                    if (0<=i+di<m and 0<=j+dj<n and grid[i+di][j+dj]==0):
                        grid[i+di][j+dj] = 1
                        new_stack.append((i+di,j+dj,step+1))
            stack = new_stack
        return -1
```

## 回溯



# 动态规划

#### [413. 等差数列划分](https://leetcode.cn/problems/arithmetic-slices/)

- 先计算差值，前后两个差值相等，说明可以构成一个最短的数列（3），这个新元素带来的新数列数量就是之前的数+1（形成了一个新的3），之后求和

```python
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # 先计算差值
        delta_lst = [nums[i]-nums[i-1] for i in range(1,n)]
        dp = [0 for i in range(n-1)]
        for i in range(1,n-1):
            if delta_lst[i] == delta_lst[i-1]:
                dp[i] = dp[i-1]+1
        return sum(dp)
```

#### [343. 整数拆分](https://leetcode.cn/problems/integer-break/)

- 典型DP，可以优化到ON

```python
class Solution:
    def integerBreak(self, n: int) -> int:
        #典型DP
        dp = [1 for i in range(n)]
        for i in range(1,n):
            for j in range(i):
                dp[i] = max(dp[i],max(dp[j],j+1)*(i-j))
        return dp[-1]
```

#### [91. 解码方法](https://leetcode.cn/problems/decode-ways/)

- 标准DP，注意判断两位的情况；同时数列中的00问题会被规避

```python
class Solution:
    def numDecodings(self, s: str) -> int:
        # 标准DP
        if s.startswith("0"): 
            return 0
        n = len(s)
        dp = [0 for i in range(n+1)]
        dp[0] = dp[1] = 1
        double_set = set(map(str,range(10,27)))
        for j in range(2,n+1):
            if s[j-1] != "0":
                dp[j] += dp[j-1]
            if s[j-2:j] in double_set:
                dp[j] += dp[j-2]
        return dp[-1]
```

## 最长递增子序列

#### [300. 最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/)

- 如题

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 维护一个递增的虚拟子串，用二分法复杂度是NlogN
        # DP的复杂度是ON2
        n = len(nums)
        dp = [1 for i in range(n)]
        for x in range(1,n):
            for y in range(x):
                if nums[x] > nums[y]:
                    dp[x] = max(dp[x],dp[y]+1)
        return max(dp)
```

#### [646. 最长数对链](https://leetcode.cn/problems/maximum-length-of-pair-chain/)

- 和300最长递增子序列思路类似，维护一个虚拟子列；另外，区间的题目按右区间排序很好做，贪心

```python
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # 这个题目和最长递增子序列不一样，因为没有固定顺序，所以要人为构造顺序
        # 按右区间排序，前面的不可能跟随在后面；左区间也一样
        pairs = sorted(pairs)
        # 也可以构建虚拟递增子串，每次查的时候用
        # 怎么感觉是贪心，不是
        n = len(pairs)
        def bi_search(nums,target): # 找第一个比target大于等于的
            n = len(nums)
            l,r = 0,n-1
            while l <= r:
                mid = (l+r) // 2
                if nums[mid] >= target:
                    r = mid-1
                else:
                    l = mid+1
            return l
        stack = [pairs[0][1]]
        for i in range(1,n):
            index = bi_search(stack,pairs[i][0])
            if index >= len(stack):
                stack.append(pairs[i][1])
            else:
                stack[index] = min(pairs[i][1],stack[index])
        return len(stack)
```

- 右区间排序+贪心

```python
class Solution(object):
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        cur, res = -inf, 0
        for x, y in sorted(pairs, key=lambda p: p[1]):
            if cur < x:
                cur = y
                res += 1
        return res
```



#### [376. 摆动序列](https://leetcode.cn/problems/wiggle-subsequence/)

- 动态规划和贪心（其实也是动态规划，只不过DP缩小为O1了）

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # DP的思路，一样，需要记录之前的方向（两个方向都要记录）和长度
        n = len(nums)
        dp = [[1,1] for _ in range(n)]
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i][0] = max(dp[i][0],dp[j][1]+1)
                elif nums[i] < nums[j]:
                    dp[i][1] = max(dp[i][1],dp[j][0]+1)
        return max(max(i) for i in dp)
```

- 贪心
假设 up[i] 表示 nums[0:i] 中最后两个数字递增的最长摆动序列长度，down[i] 表示 nums[0:i] 中最后两个数字递减的最长摆动序列长度，只有一个数字时默认为 1。

接下来我们进行分类讨论：

> - nums[i+1] > nums[i]
>   假设 down[i] 表示的最长摆动序列的最远末尾元素下标正好为 i，遇到新的上升元素后，up[i+1] = down[i] + 1 ，这是因为 up 一定从 down 中产生（初始除外），并且 down[i] 此时最大。
>   假设 down[i] 表示的最长摆动序列的最远末尾元素下标小于 i，设为 j，那么 nums[j:i] 一定是递增的，因为若完全递减，最远元素下标等于 i，若波动，那么 down[i] > down[j]。由于 nums[j:i] 递增，down[j:i] 一直等于 down[j] ，依然满足 up[i+1] = down[i] + 1 。
>
> nums[i+1] < nums[i]，类似第一种情况
> nums[i+1] == nums[i]，新的元素不能用于任何序列，保持不变

```python
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # DP的思路，一样，需要记录之前的方向（两个方向都要记录）和长度
        n = len(nums)
        down = up = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(down,up)

```

## 最长公共子序列

#### [1143. 最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/)

- DP[i][j]表示text1[:i]和text2[:j]的最长公共子序列长度

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #DP[i][j]表示text1[:i]和text2[:j]的最长公共子序列长度
        m,n = len(text1),len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i][j],dp[i][j+1],dp[i+1][j])
        return dp[-1][-1]
```