from typing import List
# 王离开自主研发的动态规划解题模版,无需状态压缩,适用于一维数组的最大/最小的加减乘除subarray,注意必须要连续,就是最严格的那一类子串
# 首先定义一个result变量用来存放记录,然后节省空间直接在原数组上原地动态规划,因为乘法有可能负负得正,所以还需要定义两个变量big和small,big用来存放正数,small用来存放负数
# big的意思是当前连续的最大数,small就是当前连续的最小数,其实可以像第一条写的把big或small存在原数组里以此节约空间
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        big = 1
        small = 1
        for i in nums:
            big,small = max(i*small,i*big,i),min(i*small,i*big,i)
            res = max(res,big)
        return res