class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        result = 0
        for i in range(len(s)):
            if len(set(s[i:i + result])) > k:
                continue
            cur_set = set()
            count = 0
            start = i
            while i < len(s) and count < k:
                if s[i] not in cur_set:
                    cur_set.add(s[i])
                    count += 1
                i += 1
            while i < len(s) and s[i] in cur_set:
                i += 1
            result = max(result, len(s[start:i]))
        return result


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstringKDistinct('ybacccccc', 3))
