#offer18 删除链表的节点
#给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。返回删除后的链表的头节点。

# 输入: head = [4,5,1,9], val = 5
# 输出: [4,1,9]
# 解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
#
# 输入: head = [4,5,1,9], val = 1
# 输出: [4,5,9]
# 解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # def deleteNode(self, head: ListNode, val: int) -> ListNode:
    #     prehead = ListNode(-1)
    #     prehead.next = head
    #     last, pos = prehead, head
    #     while pos is not None:
    #         if pos.val == val:
    #             last.next = pos.next
    #         else:
    #             last = pos
    #         pos = pos.next
    #     return prehead.next

    def deletenode(self,head:ListNode, val:int) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        last, pos = prehead, head
        while pos is not None:
            if pos.val == val:
                last.next = pos.next
            else:
                last = pos
            pos = pos.next
        return prehead.next


if __name__ == '__main__':
    l1 = ListNode(3)
    l1.next = ListNode(2)
    l1.next.next = ListNode(1)
    l1.next.next.next = ListNode(9)
    s = Solution()
    l = s.deletenode(l1, 3)
    print(l.val, l.next.val, l.next.next.val)

# if head == None or val==None:
#     return None
# M, R = None, head
# while R.next != None:
#
#     if R.val == val:
#         R = R.next
#         return R
#     R = R.next
