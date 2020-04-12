class Solution:
    def Height(self,root):
        if root is None:
            return 0
        else:
            left=self.Height(root.left)
            right=self.Height(root.right)
        return max(1+left,1+right)
    def diameterOfBinaryTree(self, root):
        if root is None:
            return 0
        else:
            left_height=self.Height(root.left)
            right_height=self.Height(root.right)
            
            total_height=left_height+right_height
            
            left_diameter=self.diameterOfBinaryTree(root.left)
            right_diameter=self.diameterOfBinaryTree(root.right)
            max_diameter=max(left_diameter,right_diameter)
        return max(max_diameter,total_height)