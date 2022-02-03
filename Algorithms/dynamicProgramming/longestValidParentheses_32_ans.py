class Solution:
    '''
    dp/栈/正反遍历 三种方法
    Runtime: 32 ms, faster than 99.38% of Python3 online submissions for Longest Valid Parentheses.
Memory Usage: 14.5 MB, less than 78.02% of Python3 online submissions for Longest Valid Parentheses.
    '''
    def longestValidParentheses(self, s: str) -> int:
        lens = len(s)
        if lens == 0: return 0
        else:
            dp = [0]*lens
            for i in range(lens):
                if s[i]==')' and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':   # i-dp[i-1]-1 是对称点的坐标
                    '''
                    第一个条件就不说了，这个只有当出现右括号的时候才会有有效括号的可能
                    第二个条件意思是确保当前这个右括号的对称点的坐标在右括号的左边
                    第三个条件是确保当前这个右括号的对称点正好是左括号
                    '''
                    dp[i] = dp[i-1]+dp[i-dp[i-1]-2]+2  # 有一个惊人的细节：因为dp[-1]的值还没计算出所以就算误加了也没事
                    # 因为会有两个相邻的有效括号的情况，所以要把对称点前一位的dp值加上去，因为对称点开头已经确保大于等于零了，所以前一位最小就是-1，也就是dp的最后一位，加了也没事的原因上面已经解释过了，最后一位是无论如何也不会计算出来的
        return max(dp)




if __name__=='__main__':

    # print(Solution().longestValidParentheses('))()()()'))
    print(Solution().longestValidParentheses("(()))())("))
    # print(Solution().longestValidParentheses("(()"))
    # print(Solution().longestValidParentheses("(()()()(())"))
    # print(Solution().longestValidParentheses(")()"))
    #
    # ")()())()()("
    # print(Solution().longestValidParentheses("()(()"))
    # print(Solution().longestValidParentheses(")()())()()("))
    #
    # print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))
    # print(Solution().longestValidParentheses(")("))