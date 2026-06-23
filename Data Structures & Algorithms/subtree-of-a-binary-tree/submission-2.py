# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root,subRoot):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def sameTree(self, p:Optional[TreeNode],q:Optional[TreeNode])-> bool:
        q1,q2=deque(),deque()
        q1.append(p)
        q2.append(q)
        while q1 and q2:
            for _ in range(len(q1)):
                P,Q=q1.popleft(),q2.popleft()
                if P is None and Q is None:
                    continue
                elif P is None or Q is None or P.val != Q.val:
                    return False
                q1.append(P.left)
                q1.append(P.right)
                q2.append(Q.left)
                q2.append(Q.right)
        return True