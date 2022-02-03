from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        两个指针快的叫nonzero，慢的叫whatever
        slow只有换值了才会进一,fast每次进一
        """
        slow,fast = 0,0
        while fast!=len(nums):
            if nums[fast]!=0:
                nums[slow] = nums[fast]
                slow+=1
            fast+=1
        while slow!=fast:
            nums[slow] = 0
            slow+=1