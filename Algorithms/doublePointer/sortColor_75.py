# 这道题借鉴了moveZeroes_283,两个指针,其实是三个,一个是非零指针,一个是零指针,一个是1指针
from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Runtime: 36 ms, faster than 62.42% of Python3 online submissions for Sort Colors.
Memory Usage: 14.2 MB, less than 47.72% of Python3 online submissions for Sort Colors.
        """
        nonZero_idx = 0
        try:
            while nums[nonZero_idx]==0:
                nonZero_idx+=1
        except IndexError:  # 说明整个数列全是0
            return
        zero_idx = nonZero_idx
        try:
            while nums[zero_idx]:
                while nums[zero_idx] != 0:
                    zero_idx += 1
                nums[zero_idx],nums[nonZero_idx] = nums[nonZero_idx],nums[zero_idx]
                nonZero_idx+=1
        except IndexError:  # 说明后面已经没0了，后面只剩1和2
                try:
                    while nums[nonZero_idx]==1:
                        nonZero_idx+=1
                except IndexError:  # 说明后面全是1了，也就是这个数列没有2
                    return
                one_idx = nonZero_idx
                try:
                    while nums[one_idx]:
                        while nums[one_idx] != 1:
                            one_idx +=1
                        nums[one_idx],nums[nonZero_idx] = nums[nonZero_idx],nums[one_idx]
                        nonZero_idx += 1
                except IndexError:  # 说明后面全是2，排序结束
                    return

if __name__=='__main__':
    print(Solution().sortColors([2,0,2,1,1,0]))
    print(Solution().sortColors([1, 0]))
    print(Solution().sortColors([2, 0, 1]))
    print(Solution().sortColors([2, 1]))
    print(Solution().sortColors([1, 2, 0]))
    print(Solution().sortColors([1, 0, 2]))
