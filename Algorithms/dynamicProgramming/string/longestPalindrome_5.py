class Solution:
    def longestPalindrome(self, s: str) -> str:
        record=0
        recordAns = s[0]
        l = len(s)
        for left in range(l):
            right = left
            while right+1<l and s[right+1]==s[left]:
                right+=1
            while right+1<l and left-1>=0 and s[right+1] == s[left-1]:
                right+=1
                left-=1
            if right-left>record:
                record = right-left
                recordAns = s[left:right+1]
        return recordAns
# # 这题动态规划的时间复杂度是O(n^2/2),所以还是用中心扩散吧
# # 非常特殊的一道动态规划求解题目,从左到右,依次从左上角到右下角遍历,行列都是从0到len(s)的坐标,原理很简单因为想要知道dp[i][j]也就是s[i:j+1]是不是回文串就必须满足两个条件:(1)s[i]==s[j],(2)s[i+1:j]是回文串。画个表格细品便知
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         result = (0,0)
#         dp = [[True]*len(s) for _ in range(len(s))]
#         for col in range(1,len(s)):
#             for x in range(len(s)-col):
#                 if s[x]==s[x+col] and dp[x+1][x+col-1]:
#                     dp[x][x+col] = True
#                     result = (x,x+col)
#                     continue
#                 dp[x][x+col] = False
#         return s[result[0]:result[1]+1]
if __name__=='__main__':
    # print(Solution().longestPalindrome("aacabdkacaa"))
    print(Solution().longestPalindrome("a"))



if __name__=='__main__':
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("aacabdkacaa"))
    print(Solution().longestPalindrome("cbbd"))
    print(Solution().longestPalindrome("aacabdkacaa"))
