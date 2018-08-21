# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        return self.gen_helper({}, 1, n)
        
    def gen_helper(self, memo, start, end):
        if start > end:
            return [None]
        if (start, end) in memo:
            return memo[(start, end)]
        memo[(start, end)] = []
        for root_val in xrange(start, end+1):
            for left_child in self.gen_helper(memo, start, root_val-1):
                for right_child in self.gen_helper(memo, root_val+1, end):
                    root = TreeNode(root_val)
                    root.left, root.right = left_child, right_child
                    memo[(start, end)].append(root)
        return memo[(start, end)]
