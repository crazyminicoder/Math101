class Solution:
    def numSquares(self, n):
        # Initialize the DP array with infinity for all indices
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # base case

        # Precompute all perfect squares less than or equal to n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        # Fill in the DP array
        for i in range(1, n + 1):
            for square in squares:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)
        for i in range(n+1):
            for j in range(n+1):
                print(dp[i][j])
        return dp[n]


res = Solution()
a = res.numSquares(159)
print(a)
