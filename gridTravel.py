class Solution:
    def travel(self, m, n, memo):
        key = str(m)+','+str(n)
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        memo[key] = self.travel(m, n-1, memo) + self.travel(m-1, n, memo)
        return memo[key]


res = Solution()
memo = {}
a = res.travel(7, 7, memo)
print(a)
