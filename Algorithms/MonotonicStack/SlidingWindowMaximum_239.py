from typing import List
# 这道题做了两遍,我也不知道为什么, 这是新的
# 同样也是细节拉满,双端队列里面不仅要存放数值,还要存放idx,如果一旦idx超过了k,那么就说明老了,就要pop
# 操作顺序大致就是:先压栈,再出货,最后维护数组长度(如果当前idx减去队列最左边的idx+1==k就说明老了,别问我怎么知道的,试出来的)

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        stack = [(0, nums[0])]
        result = []

        for i in range(1, k):
            while stack and nums[i] > stack[-1][1]:
                stack.pop(-1)
            stack.append((i, nums[i]))
        result.append(stack[0][1])

        if stack[0][0] + k - 1 == i:  # 说明左边的老了
            stack.pop(0)

        for i in range(k, len(nums)):
            while stack and nums[i] > stack[-1][1]:
                stack.pop(-1)
            stack.append((i, nums[i]))
            result.append(stack[0][1])
            if stack[0][0] + k - 1 == i:
                stack.pop(0)
        return result
