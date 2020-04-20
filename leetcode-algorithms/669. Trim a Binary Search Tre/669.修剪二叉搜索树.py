#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        self.L,self.R = L,R
        if not root: return
        while root and (root.val>R or root.val<L):
            root = self.judge(root) 
        if not root: return
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node: continue
            while node.left and (node.left.val > R or node.left.val < L):
                node.left = self.judge(node.left) 
            queue.append(node.left)
            while node.right and (node.right.val > R or node.right.val < L):
                node.right = self.judge(node.right) 
            queue.append(node.right)
        return root
    #判断当前结点是否满足条件，不满足要进行删除操作，如果小的话那么左子树就没价值了，大的话同理
    def judge(self,node):
        if node.val < self.L:
            node.left = None
            node = self.delNode(node)
        elif node.val > self.R:
            node.right = None
            node = self.delNode(node)
        return node
    #二叉搜索树的删除操作
    def delNode(self,node):
        if not node: return
        if not node.left and not node.right: return None
        if not node.left: return node.right
        if not node.right: return node.left
        leftmax = self.getMax(node.left)
        node.val = leftmax.val
        self.delNode(leftmax)
        return node
    #二叉搜索树找最大值的操作
    def getMax(self,node):
        if not node: return
        while node.right: node = node.right
        return node   

# @lc code=end

