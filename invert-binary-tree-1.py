# IDEA: use 2 functions, one for swapping the left and right nodes for a given root
# Second, to do the swap during pre-order traversal
# Input: root of the tree
# Output: root of the inverted tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    def invertTree(self, root: TreeNode) -> TreeNode:

        def swap(root):
            if root is not None:
                tmp = root.left
                root.left = root.right
                root.right = tmp

        def invert_binary_tree(root):
            if root is not None:
                swap(root)
                invert_binary_tree(root.left)
                invert_binary_tree(root.right)

        invert_binary_tree(root)

        return root