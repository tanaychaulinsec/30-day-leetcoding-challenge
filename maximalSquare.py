class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        dp=[[1 if matrix[r][c]=='1' else 0 for c in range(len(matrix[0]))] for r in range(len(matrix))]
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                if matrix[r][c]=='1':
                    dp[r][c]=min(dp[r][c-1],dp[r-1][c],dp[r-1][c-1])+1
        res=max(max(row)for row in dp)
        return res**2