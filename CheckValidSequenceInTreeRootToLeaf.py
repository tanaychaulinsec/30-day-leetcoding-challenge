class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root,index):
            n= len(arr)
            if not root or index==n or arr[index]!=root.val:
                return False
            if index== n-1 and not(root.left or root.right):
                return  True
            return (dfs(root.left,index+1) or dfs(root.right,index+1))
        return dfs(root,0)