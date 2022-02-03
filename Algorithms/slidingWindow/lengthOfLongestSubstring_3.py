# 无重复最长字符串
# 滑动窗口,其实没有看上去那么简单
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        window = []
        for i in s:
            if i not in window:
                window.append(i)
                res = max(len(window),res)
            else:
                while i in window:
                    window.pop(0)
                window.append(i)
        return res


if __name__=='__main__':
    s = "pwwkerwrteatew"
    # s = 'aab'
    print(Solution().lengthOfLongestSubstring(s))