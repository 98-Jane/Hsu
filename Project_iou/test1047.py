
class Solution:
    def removeDuplicates(self, S:str) -> str:
        stack = [',']
        for i in S:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
        return ''.join(stack[1:])

S = 'abbaca'
out = Solution().removeDuplicates(S)
print (out)
