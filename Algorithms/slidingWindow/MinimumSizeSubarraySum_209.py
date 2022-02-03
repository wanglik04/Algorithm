from typing import List
# 滑动窗口,右指针到头就结束
# 滑动窗口用for rather than pop, without try
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        result = 0
        count = nums[0] #滑动窗口里面数字的总和
        try:
            while right<len(nums):
                while count<target:
                    count+=nums[right]
                    right+=1
                if count>=target:
                    while count>=target:
                        count-=nums[left]
                        left+=1
                    if result==0:
                        result = right - left +1
                    else:
                        result = min(result,right-left+1)
        except IndexError:
            return result
        return result
if __name__=='__main__':
    print(Solution().minSubArrayLen(15,[5,1,3,5,10,7,4,9,2,8]))