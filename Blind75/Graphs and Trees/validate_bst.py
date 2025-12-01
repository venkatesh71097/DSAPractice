# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Iterative: 
        # Let's do DFS... problem seems to be recursive-type: So dig deep till the leftmost/rightmost node for min-max comparisons
        # Same check : low < node < high but with different low and high vals
        if not root:
            return True
        stack = [(root, float('-inf'), float('inf'))]
        # LIFO technique: 
        while stack:
            node, low, high = stack.pop()
            if not node:
                continue
            if low >= node.val or high <= node.val:
                return False
            stack.append([node.left, low, node.val])
            stack.append([node.right, node.val, high])

        return True

        """Recursive: 
        def validate(node, min_val=float('-inf'), max_val=float('inf')):
            if not node:
                return True
            if min_val >= node.val or max_val <= node.val:
                return False 
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)            
        return validate(root)
        """