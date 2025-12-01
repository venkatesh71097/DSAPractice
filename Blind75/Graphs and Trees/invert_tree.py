# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Iterative approach
        if not root:
            return None
        from collections import deque
        # Start with a queue element as ROOT
        queue = deque([root])

        while queue:
            # Whatever enters first, leaves first - FIFO!
            curr = queue.popleft()
            # Swap the children
            curr.left, curr.right = curr.right, curr.left
            # Right child (now left) goes first into queue
            if curr.left:
                queue.append(curr.left)
            # Left child (now right) goes first into queue
            if curr.right:
                queue.append(curr.right) 
        return root
        
        """
            # Recursion approach
            if not root:
                return None
            temp = self.invertTree(root.right)
            root.right = self.invertTree(root.left)
            root.left = temp
            # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        """