class Solution:
    def __init__(self):
        self.res=0
    def diameterOfBinaryTree(self, root):
        def height(root):
            if not root:
                return 0
            left=height(root.left)
            right=height(root.right)
            self.res=max(self.res,left+right)
            return 1+ max(left,right)
        height(root)
        return self.res