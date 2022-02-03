from typing import List
# 一道单调栈的简单题,list1是list2的子集.让你找到list1里所有在list2里对应的值的下一个更大的值

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashmap = {}
        stack = [nums2.pop(0)]
        for i in nums2:
            while stack and i > stack[-1]:
                hashmap[stack.pop(-1)] = i
            stack.append(i)
        while stack:
            hashmap[stack.pop(-1)] = -1  # 剩下的都是没有最大值的
        for i in nums1:  # 为了节省空间,反正stack已经空了,把stack当成result
            stack.append(hashmap.get(i))
        return stack