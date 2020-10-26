#括号的最大嵌套深度

#输入："()"      输出：1
#输入："{()[]}"  输出：2
#输入："[)]"     输出：0
#输入："([)]"    输出：0

#输入：s = "(1+(2*3)+((8)/4))+1"  输出：3
#输入：s = "(1)+((2))+(((3)))"    输出：3
#输入：s = "1+(2*3)/(2-1)"        输出：1
#输入：s = "1"                    输出：0
class Solution:
    # def maxDepth(self, s:str) -> int:  #只关注括号，遇到括号就更新结果
    #     res = cur = 0
    #     for c in s:
    #         if c == "(":
    #             cur += 1
    #         elif c == ")":
    #             cur -= 1
    #         res = max(res, cur)
    #     return res

    def maxDepth(self, s:str) -> int:
        ret = 0
        depth = 0
        for c in s:
            if c == '(':
                depth += 1
            elif c == '[':
                depth += 1
            elif c == '{':
                depth += 1
            elif c == ')':
                depth -= 1
            elif c == ']':
                depth -= 1
            elif c == '}':
                depth -= 1
            ret = max(ret, depth)
        return ret

if __name__ == "__main__":
    sol = Solution()
    out = sol.maxDepth("([)]")
    print(out)

    #输入："()"      输出：1
#输入："{()[]}"  输出：2
#输入："[)]"     输出：0
#输入："([)]"    输出：0