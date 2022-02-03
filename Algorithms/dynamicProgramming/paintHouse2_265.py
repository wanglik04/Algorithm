from typing import List
#这题一开始想歪了，正确的路径就是当前值加上一层除去当前节点的最小值就是当前dp的值，有多少重复的数字不影响
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        for i in range(1,len(costs)): # line
            for j in range(len(costs[0])):  # col
                costs[i][j] += min(costs[i-1][:j]+costs[i-1][j+1:])
        return min(costs[-1])
if __name__=='__main__':
    print(Solution().minCostII([[8 , 16, 12, 18, 9 ],
                                [19, 18, 8 , 2 , 8 ],
                                [8 , 5 , 5 , 13, 4 ],
                                [15, 9 , 3 , 19, 2 ],
                                [8 , 7 , 1 , 8 , 17],
                                [8 , 2 , 8 , 15, 5 ],
                                [8 , 17, 1 , 15, 3 ],
                                [8 , 8 , 5 , 5 , 16],
                                [2 , 2 , 18, 2 , 9 ]])) #