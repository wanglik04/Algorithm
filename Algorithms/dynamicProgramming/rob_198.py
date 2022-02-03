from typing import List
# 打家劫舍,应该是一道基础的动态规划题吧,我发现之前写的动态规划怎么都是从后往前遍历,不过其实仔细想想也不难理解

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums) if nums!=[] else 0
        for i in range(len(nums)-3,-1,-1):
            nums[i] += max(nums[i+2:])
        return max(nums)


if __name__=='__main__':
    print(Solution().rob([2,399,4]))