# 113-二叉树的最近公共祖先
# 题目：给定一个二叉树, 找到该树中两个指定节点的最近公共祖先
'''中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，
满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”'''


# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出: 3
# 解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

# 输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出: 5
# 解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


# 所有节点的值都是唯一的。
# p、q为不同节点且均存在于给定的二叉树中。

# Definition for binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution:
#     def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode) -> TreeNode:
#         self.ans = None
#         def helper(node):
#             if not node:
#                 return False
#             left = helper(node.left)
#             right = helper(node.right)
#             mid = node==p or node ==q
#             if mid+left+right >= 2:
#                 self.ans = node
#             return mid or left or right
#         helper(root)
#         return self.ans

# #20200825-第二次默写，注意判断为node==p or node==q，否则会出现不匹配的情况
# class Solution:
#     def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
#         self.ans = None
#
#         def helper(node):
#             if not node:
#                 return False
#             left = helper(node.left)
#             right = helper(node.right)
#             mid = node== p or node== q
#             if mid + left + right >= 2:
#                 self.ans = node
#             return mid or left or right
#
#         helper(root)
#         return self.ans


# # #20200826-第3次默写，50%不记得了,记住二叉数最近公共祖先是return False和True
# class Solution:
#     def lowestCommonAncestor(self,root: TreeNode, p: TreeNode, q: TreeNode):
#         self.ans = None
#         def helper(node):
#             if node is None:
#                 return False
#             left = helper(node.left)
#             right = helper(node.right)
#             mid = node==p or node==q
#             if mid+left+right >= 2:
#                 self.ans = node
#             return mid or left or right #
#         helper(root)
#         return self.ans

# # # #20200828-第4次默写,都不记得了
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         self.ans = None
#         def helper(node):
#             if node is None:
#                 return False
#             left = helper(node.left)
#             right = helper(node.right)
#             mid = node==p or node==q
#             if mid+left+right >=2:
#                 self.ans = node
#             return mid or left or right
#         helper(root)
#         return self.ans


# # # # #20200910-第5次默写,都不记得了
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         self.ans = None
#         def helper(node):
#             if node is None:
#                 return False
#             left = helper(node.left)
#             right = helper(node.right)
#             mid = node==p or node==q
#             if mid+left+right >= 2:
#                 self.ans = node
#             return mid or left or right
#         helper(root)
#         return self.ans



Node_3 = Tree = TreeNode(3)
Node_5 = Node_3.left = TreeNode(5)
Node_1 = Node_3.right = TreeNode(1)
Node_6 = Node_5.left = TreeNode(6)
Node_2 = Node_5.right = TreeNode(2)
Node_0 = Node_1.left = TreeNode(0)
Node_8 = Node_1.right = TreeNode(8)
Node_7 = Node_2.left = TreeNode(7)
Node_4 = Node_2.right = TreeNode(4)
s = Solution()
print(s.lowestCommonAncestor(Tree, Node_5, Node_4).val)
