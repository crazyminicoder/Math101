def fib(n):
    if n == 1 or n == 2:
        return 1
    dp = [None] * (n+1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1]+dp[i-2]
    # print(dp)
    return dp[n-1]


res = fib(1000)
print(res)
