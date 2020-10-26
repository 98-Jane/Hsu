#反转从位置m到n的链表，请使用一趟扫描完成反转
#说明：1<=m<=n<= 链表长度
#输入：1——>2>——>3——>4——>5——>NULL, m=2, n=4
#输出：1——>4>——>3——>2——>5——>NULL

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# #把所有链表压入一个列表，然后翻转相应的位置，创建新的链表
# class Solution:
#     def reverseBetween(self, head:ListNode, m:int, n:int) -> ListNode:
#         if head == None:  #如果head不存在返回空
#             return
#         if m == n:  #如果m=n，单个节点反转等于没变动
#             return head
#         stack = []  #新建一个空列表
#         first = ListNode(10000)  #新建一个节点，listnode可以为任意值
#         while head:  #当head不为空时，执行下列操作
#             stack.append(head.val)  #在stack后面append添加head的val
#             head = head.next #
#         stack[m-1:n] = reversed(stack[m-1:n])
#         res = first
#         while stack:
#             first.next = ListNode(stack.pop(0))  # pop(0)移除第一个元素，pop(-1)移除最后一个元素
#             first = first.next                   # pop()（默认最后一个元素），并且返回该元素的值
#         return res.next




# ##20200911-第1次默写, while head然后是while stack
# class Solution:
#     def reverseBetween(self,head,m,n):
#         if head is None:
#             return
#         if m==n:
#             return head
#         stack = []
#         first = ListNode(10000)
#         while head:
#             stack.append(head.val)
#             head = head.next
#         stack[m-1: n] = reversed(stack[m-1: n])
#         res = first
#         while stack:
#             first.next = ListNode(stack.pop(0))
#             first = first.next
#         return res.next



# ##20200911-第2次默写, first.next= ListNode()
class Solution:
    def reverseBetween(self, head, m, n):
        if not head:
            return
        if m==n:
            return head
        stack = []
        first = ListNode(10000)
        while head:
            stack.append(head.val)
            head = head.next
        stack[m-1:n] = reversed(stack[m-1:n])
        res = first
        while stack:
            first.next = ListNode(stack.pop(0))
            first = first.next
        return res.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    s = Solution()
    l = s.reverseBetween(l1, 2, 4)
    print(l.val, l.next.val, l.next.next.val, l.next.next.next.val,l.next.next.next.next.val)
