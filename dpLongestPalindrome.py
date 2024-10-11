# abccba
def palin(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(len(s)):
        dp[i][i] = 1

#    print(dp)
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
    print(dp)

    

palin('abccba')
