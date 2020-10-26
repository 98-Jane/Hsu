#235 二叉搜索树的最近公共祖先
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """ :type root: TreeNode
#             :type p: TreeNode
#             :type q: TreeNode
#             :rtype: TreeNode
#         """
#         if not root or not p or not q:
#             return None
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val >root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root

# class Solution():
#     def lowestCommonAncestor(self, root, p, q):
#         if root is None or p is None or q is None:
#             return None
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root

#20200825-第2次默写：if语句里面少了return，感觉还是没搞太懂内部运行，建议debug看看;

# class Solution:
#     def lowestCommonAncestor(self,root,p,q):
#         if root is None or p is None or q is None:
#             return None
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root

# #20200825-第3次默写：多加了root！=None
# class Solution:
#     def lowestCommonAncestor(self,root: TreeNode, p:TreeNode, q:TreeNode):
#         if root is None or p is None or q is None:
#             return None
#         while root != None:
#             if p.val < root.val and q.val < root.val:
#                 return self.lowestCommonAncestor(root.left, p, q)
#             elif p.val > root.val and q.val > root.val:
#                 return self.lowestCommonAncestor(root.right, p, q)
#             else:
#                 return root

# # #20200828-第4次默写：少写了p，q
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if root is None or p is None or q is None:
#             return None
#         if root.val>p.val and root.val>q.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif root.val<p.val and root.val<q.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root

# # # #20200910-第5次默写：完全不记得了，还少写了p，q
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if root is None or p is None or q is None:
#             return None
#         if p.val < root.val and q.val < root.val:
#             return self.lowestCommonAncestor(root.left, p, q)
#         elif p.val > root.val and q.val > root.val:
#             return self.lowestCommonAncestor(root.right, p, q)
#         else:
#             return root






if __name__ == '__main__':
    Node_6 = TreeNode(6)
    Node_2 = Node_6.left = TreeNode(2)
    Node_8 = Node_6.right = TreeNode(8)
    Node_0 = Node_2.left = TreeNode(0)
    Node_4 = Node_2.right = TreeNode(4)
    Node_7 = Node_8.left = TreeNode(7)
    Node_9 = Node_8.right = TreeNode(9)
    Node_3 = Node_4.left = TreeNode(3)
    Node_5 = Node_4.right = TreeNode(5)
    s = Solution()
    print(s.lowestCommonAncestor(Node_6, Node_0, Node_4).val)