from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])  # Initialize queue with the root node
        res = []  # Store the right-side view result

        while q:
            q_len = len(q)  # Get number of nodes in the current level
            right_most = None  # Track the rightmost node of this level

            for _ in range(q_len):
                node = q.popleft()  # Remove node from the front of the queue
                right_most = node  # Always update right_most with the last node processed

                if node.left:
                    q.append(node.left)  
                if node.right:
                    q.append(node.right)  

            res.append(right_most.val)  # Add the last node of this level to the result

        return res
