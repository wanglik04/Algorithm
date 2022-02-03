# 去掉没用的括号,打印所有合法的括号.最骚的是里面会有英文,isValid函数是我自己发明的,有一种别的方法是用栈
# 看了一眼提示,用了bfs作出
from typing import List
class Solution:
    def isValid(self, s: str):
        count = 0
        for i in s:
            if i == '(':
                count += 1
            elif i == ')':
                count -= 1
                if count < 0:
                    return False
        return True if count == 0 else False
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if self.isValid(s):
            return [s]
        result = set()
        cur_task = set()
        next_task = set()
        for i in range(len(s)):
            if s[i].isalpha():
                continue
            if self.isValid(s[:i]+s[i+1:]) is False:
                cur_task.add(s[:i]+s[i+1:])
                continue
            result.add(s[:i]+s[i+1:])
        while cur_task:
            while cur_task:
                cur = cur_task.pop()
                for i in range(len(cur)):
                    if cur[i].isalpha():
                        continue
                    if self.isValid(cur[:i]+cur[i+1:]) is False:
                        next_task.add(cur[:i]+cur[i+1:])
                        continue
                    result.add(cur[:i]+cur[i+1:])
            if len(result)==0:
                cur_task = next_task
                next_task = set()
        return list(result) if len(result)!=0 else [""]

if __name__=='__main__':
    # print(Solution().removeInvalidParentheses("(a)())()"))
    # print(Solution().removeInvalidParentheses("n"))  # ["n"]
    # print(Solution().removeInvalidParentheses("()"))
    # print(Solution().removeInvalidParentheses("(j))(")) # ["(j)"]
    # print(Solution().removeInvalidParentheses(")(")) # [""]
    # print(Solution().removeInvalidParentheses("(n)"))
    # print(Solution().removeInvalidParentheses("x("))

    print(Solution().removeInvalidParentheses("((()((s((((()"))
