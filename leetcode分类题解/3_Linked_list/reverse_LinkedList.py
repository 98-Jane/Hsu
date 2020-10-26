class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def reverseList(self, head):
#         if head == None:
#             return None
#         L, M, R = None, None, head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

# class Solution:
#     def reverseList(self, head):
#         if head==None:
#             return None
#         L,M,R = None, None, head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

# #20200825-第二次默写
# class Solution:
#     def reverseList(self, head):
#         if head == None:
#             return None
#         L,M,R = None,None,head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

# #20200826-第3次默写
# #写错了R.next = M ，M已经是反转后的3-2-1,而R为4,则是将后续链表赋给R
# class Solution:
#     def reverseList(self, head: Node):
#         if head is None:
#             return None
#         L,M,R = None,None,head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

# # #20200826-第4次默写
# class Solution:
#     def reverseList(self,head):
#         if head is None:
#             return None
#         L,M,R = None,None,head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

# # # #20200828-第5次默写
# class Solution:
#     def reverseList(self, head: Node):
#         if head is None:
#             return None
#         L,M,R = None, None, head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R


# # # # #20200910-第6次默写, 忘记写head
# class Solution:
#     def reverseList(self, head):
#         if head is None:
#             return None
#         L, M, R = None, None, head
#         while R.next != None:
#             L = M
#             M = R
#             R = R.next
#             M.next = L
#         R.next = M
#         return R

class Solution:
    def reverseList(self, head):
        if head is None:
            return None
        L,M,R = None,None,head
        while R.next != None:
            L = M 
            M = R 
            R = R.next
            M.next = L 
        R.next = M
        return R




if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    s = Solution()
    l = s.reverseList(l1)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val)