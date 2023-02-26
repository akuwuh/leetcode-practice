class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # notes: 

        # insert char
        # delete char
        # replace char

        # dp moment rofl

        # conditions:
        # if equal:
        # cell min of 3 dir
        # if not then add 1 to min of 3 dir 

        # initialize 0 array with n + 1, m + 1 dimensions
        # start from the bottom up

        n = len(word1)
        m = len(word2)

        if not n or not m: # one of them = 0 
            return max(n,m)

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(0,n):
            dp[i][m] = n - i
        for j in range(0,m):
            dp[n][j] = m - j
        
        for i in range(n -1, -1, -1):
            for j in range(m -1,-1,-1):
                if word1[i] != word2[j]: 
                    dp[i][j] = min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1]) + 1
                else: 
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]

