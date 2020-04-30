class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(root,index):
            size=len(arr)
            if not root or index == size or arr[index] != root.val:
                return False
            if index == size - 1 and not (root.left or root.right):
                return True
            return ((index < size-1) and (root.val == arr[index]) and 
            (dfs(root.left,index + 1) or
             dfs(root.right,index + 1)))
        
        return dfs(root,0)