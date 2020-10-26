# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# class Solution(object):
#     def lowestCommonAncestor(self, root, p, q):
#         """
#         :type root: TreeNode
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: TreeNode
#         """
#         self.ans = None
#
#         def lowestCommonAncestorHelper(node):
#             if not node:
#                 return False
#             left = lowestCommonAncestorHelper(node.left)
#             right = lowestCommonAncestorHelper(node.right)
#             mid = (node == p) or (node == q)
#             if mid + left + right >= 2:
#                 self.ans = node
#             return mid or left or right
#         lowestCommonAncestorHelper(root)
#         return self.ans

    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # Stack for tree traversal
    #     stack = [root]
    #     # Dictionary for parent pointers
    #     parent = {root: None}
    #     # Iterate until we find both the nodes p and q
    #     while p not in parent or q not in parent:
    #
    #         node = stack.pop()
    #
    #         # While traversing the tree, keep saving the parent pointers.
    #         if node.left:
    #             parent[node.left] = node
    #             stack.append(node.left)
    #         if node.right:
    #             parent[node.right] = node
    #             stack.append(node.right)
    #
    #     # Ancestors set() for node p.
    #     ancestors = set()
    #
    #     # Process all ancestors for node p using parent pointers.
    #     while p:
    #         ancestors.add(p)
    #         p = parent[p]
    #
    #     # The first ancestor of q which appears in
    #     # p's ancestor set() is their lowest common ancestor.
    #     while q not in ancestors:
    #         q = parent[q]
    #     return q


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        self.ans = None
        def helper(node):
            if not node:
                return False  #相当于0,如果node不存在，则返回0
            left = helper(node.left)
            right = helper(node.right)
            mid = (node==p) or (node==q) #如果node等于p或者q，返回1
            if mid + left + right >=2: #如果有两个为1,则说明找到了公共祖先
                self.ans = node
            return mid or left or right #如果有一个不为0,相当于返回1
        helper(root)
        return self.ans

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
