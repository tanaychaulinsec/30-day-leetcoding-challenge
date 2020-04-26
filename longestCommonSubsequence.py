class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)>len(text2):
            str1,str2=text1,text2
        else:
            str1,str2=text2,text1
        dp=[[0 for x in range(len(str1)+1) ] for y in range(len(str2)+1)]
        for row in range(len(str2)):
            for col in range(len(str1)):
                if str2[row]==str1[col]:
                    dp[row][col]=dp[row-1][col-1] +1
                else:
                    dp[row][col]=max(dp[row][col-1],dp[row-1][col])
        return dp[row][col]