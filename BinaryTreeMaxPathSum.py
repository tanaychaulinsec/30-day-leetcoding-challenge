class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root,largest):
            if root==None:
                return 0
            left=dfs(root.left,largest)
            right=dfs(root.right,largest)
            largest[0]=max(largest[0],left+right+root.val,left+root.val,right+root.val,root.val)
            return max(max(left,right)+root.val,root.val)
            
        largest=[-2**32]
        dfs(root,largest)
        return largest[0]