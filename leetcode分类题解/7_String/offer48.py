#从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度
#输入："abcabcbb"  3  #输入："bbbbb"  1  #输入："pwwkew"  3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        head, tail = 0, 0
        maxLen = 1
        while tail+1 < len(s):
            tail += 1 #往窗口添加元素
            s_tail, s_head_tail = s[tail], s[head:tail]
            print(s_tail), print(s_head_tail)
            if s[tail] not in s[head:tail]: #窗口内没有重复的字符，实时更新窗口最大长度
                maxLen = max(maxLen, tail-head+1)
            else:
                while s[tail] in s[head:tail]:
                    head += 1
        return maxLen

if __name__ == "__main__":
    sol = Solution()
    out = sol.lengthOfLongestSubstring('abcabcbb')
    print(out)