#从头出发到底找出最小路径和
# 120. Triangle
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        try:
            result = triangle.pop(0)
        except IndexError:
            return 0
        for i in triangle:
            i[0] += result[0]
            i[-1] += result[-1]
            for j in range(1,len(i)-1):
                i[j] += min(result[j],result[j-1])
            result = i
        return min(result)