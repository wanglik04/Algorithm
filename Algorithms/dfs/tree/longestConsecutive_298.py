# Definition for a binary tree node.
# 让你找到二叉树中从父到子依次递增1的最长子序列的长度
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, node: TreeNode): # 以此计算当前节点左子树的最长子串,和右子树的最长子串,然后更新record,最后选最大值return给上一层,因为有可能两边计算结果都是负数,所以最小值为0
        l = r = 0
        if node.left:
            if node.val == node.left.val - 1:
                l = self.dfs(node.left) + 1
            else:
                self.dfs(node.left)
        if node.right:
            if node.val == node.right.val - 1:
                r = self.dfs(node.right) + 1
            else:
                self.dfs(node.right)
        self.record = max(l, r, self.record)
        return max(l, r, 0)

    def longestConsecutive(self, root: TreeNode) -> int:
        self.record = 0
        self.dfs(root)
        return self.record + 1