from typing import List
# 接雨水,单调递减栈

class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stk = []  # 判断0和1
        for k,v in enumerate(height):
            while stk and v>=stk[-1][1]:
                sub = stk.pop()
                if stk:
                    result+=(min(stk[-1][1],v)-sub[1])*(k-stk[-1][0]-1)
            stk.append((k,v))
        return result


if __name__=='__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] # 6
    print(Solution().trap(height))
    print(Solution().trap([4, 2, 0, 3, 2, 5])) # 9
    # print(Solution().trap([4, 2, 1, 0, 3]))  # 6
    # # print(Solution().trap([4, 2, 0, 3]))
    # # print(Solution().trap([4, 2, 0, 5]))
    print(Solution().trap([5,2,1,2,1,5]))
    print(Solution().trap([5,4,1,2]))

