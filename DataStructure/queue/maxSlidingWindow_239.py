# 单调栈？双端队列!
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        twq = []
        for i in range(k):
            while twq and twq[-1][1]<nums[i]:
                twq.pop()
            else:
                twq.append((i,nums[i]))
        result = [twq[0][1]]
        for i in range(k,len(nums)):
            while twq and twq[-1][1]<nums[i]:
                twq.pop()
            twq.append((i,nums[i]))
            if i-twq[0][0]==k:
                twq.pop(0)
            result.append(twq[0][1])
        return result

if __name__=='__main__':
    print(Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))
    # print(Solution().maxSlidingWindow([1, -1], 1))
    print(Solution().maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))  # [3,3,2,5]
