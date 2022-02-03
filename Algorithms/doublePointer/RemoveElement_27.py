from typing import List
# 滑动窗口,右指针到头就结束
# 滑动窗口用for rather than pop, without try
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = len(nums)-1
        fast = 0
        count = 0
        while nums[slow]==val:
            nums[slow] = 0
            count += 1
            slow-=1
        while fast<slow:
            if nums[fast]==val:
                nums[fast] = nums[slow]
                nums[slow] = 0
                count += 1
                slow -= 1
                while nums[slow]==val:
                    nums[slow] = 0
                    count += 1
                    slow-=1
            fast+=1
        return len(nums)-count


if __name__=='__main__':
    print(Solution().removeElement([0,1,2,2,3,0,4,2],2))
    print(Solution().removeElement([3,2,2,3], 3))