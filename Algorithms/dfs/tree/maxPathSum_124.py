# Definition for a binary tree node.
# 题目让你计算二叉树中最大路径和,众所周知,在二叉树中如果将左-中-右连起来的话就没办法在连其他值了,
# 可能这就是record和realrecord存在的意义吧
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        self.record = -99999000
        self.realrecord = -100000000
        self.burnIt(root)
        return max(self.record, self.realrecord)

    def burnIt(self, node):
        if node is None:
            return 0
        left_rat = self.burnIt(node.left)
        right_rat = self.burnIt(node.right)
        self.realrecord = max(left_rat + right_rat + node.val, self.realrecord)
        if left_rat < 0 and right_rat < 0:
            self.record = max(self.record, node.val)
            return node.val
        else:
            s = node.val + max(left_rat, right_rat)
            self.record = max(self.record, s)
            return s
