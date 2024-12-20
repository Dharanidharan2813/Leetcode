# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = [root]
        level = 0
        while queue:
            current_level = queue[:]
            queue = []
            for node in current_level:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                values = [node.val for node in current_level]
                for i, node in enumerate(current_level):
                    node.val = values[-(i + 1)]
            level += 1
        return root