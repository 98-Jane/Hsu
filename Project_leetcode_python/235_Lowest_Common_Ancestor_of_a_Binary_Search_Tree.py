# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # get all possible paths
    #     paths = {}
    #     self.get_path(paths, root)
    #     # compare paths of p and q
    #     # return the last identical node
    #     p_path, q_path = paths[p][::-1], paths[q][::-1]
    #     ls = min(len(p_path), len(q_path))
    #     pos = 0
    #     last = root
    #     while pos < ls:
    #         if p_path[pos] != q_path[pos]:
    #             return last
    #         last = p_path[pos]
    #         pos += 1
    #     return last
    #
    #
    # def get_path(self, paths, node, curr=[]):
    #     # get all possible path
    #     if node is not None:
    #         paths[node] = [node] + curr
    #         if node.left is not None:
    #             self.get_path(paths, node.left, paths[node])
    #         if node.right is not None:
    #             self.get_path(paths, node.right, paths[node])

    def lowestCommonAncestor(self, root, p, q):
        # use the BST to reduce the search space
        if p is None or q is None or root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root


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
print(s.lowestCommonAncestor(Node_6, Node_0, Node_5).val)
