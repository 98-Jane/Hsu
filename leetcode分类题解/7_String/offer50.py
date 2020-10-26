#第一个只出现一次的字符
#s="abaccdeff"  返回 b
#s=""  返回 " "
#字典
import collections

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = not c in dic
        for k,v in dic.items():
            if v: return k
        return ' '

if __name__ == "__main__":
    sol = Solution()
    out = sol.firstUniqChar('')
    print(out)