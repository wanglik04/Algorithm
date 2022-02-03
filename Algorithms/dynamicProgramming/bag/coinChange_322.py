from typing import List


# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # INFINITY = 2**31
#         # dp = {i:INFINITY for i in range(amount) if i!=0 else i:0} # 不存在没有值的可能了
#         dp = {0:0}
#         for coin in coins:
#             for money in range(1,amount+1):
#                 if dp.get(money):
#                     if money>=coin:# 有值且大于coin值
#                         dp[money] = min(dp[money],dp[money-coin]+1)
#                     else:# 有值但小于coin值,维持不变
#                         continue
#                 elif money<coin: # 没有值且小于coin值
#                     dp[money] = float("inf")
#                 else: #没有值但是大于coin值
#                     dp[money] = dp[money-coin]+1
#         return dp[amount] if dp[amount]<float("inf") else -1
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {i:float("inf") for i in range(1,amount+1)} # 不存在没有值的可能了
        dp[0]=0
        for coin in coins:
            for money in range(1,amount+1):
                if money>=coin and dp.get(money):# 有值且大于coin值
                    dp[money] = min(dp[money],dp[money-coin]+1)
        return dp[amount] if dp[amount]<float("inf") else -1
if __name__=='__main__':
    print(Solution().coinChange())