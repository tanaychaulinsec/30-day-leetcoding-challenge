class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1)>len(text2):
            str1,str2=text1,text2
        else:
            str1,str2=text2,text1
        dp = [[0 for x in range(len(str1)+ 1)] for y in range(2)]

        for row in range(len(str2)):
            for col in range(len(str1)):
                if str2[row] == str1[col]:
                    dp[1 - row % 2][col + 1] = 1 + dp[row % 2][col]
                else:
                    dp[1 - row % 2][col + 1] = max(dp[1 - row % 2][col], dp[row % 2][col + 1])

        return dp[len(str2) % 2][len(str1)]