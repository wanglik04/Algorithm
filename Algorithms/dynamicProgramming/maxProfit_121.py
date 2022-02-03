from typing import List
# 买卖股票1
# 动态规划

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        dp[-1] = 0
        for i in range(len(prices)-2,-1,-1):
            dp[i] = max(prices[i+1]-prices[i]+dp[i+1],0)
        return max(dp)

# # 单调栈 Monotonic stack
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         res = []
#         stack = [prices.pop(0)]
#         prices.append(0)
#         for i in range(len(prices)):
#             while stack and prices[i] < stack[0]:
#                 res.append(-stack[-1]+stack.pop(0))
#             stack.insert(0,(prices[i]))
#         return max(res)