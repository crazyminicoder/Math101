class Solution:
    def travel(self, m, n, memo):
        # checking if the key is in memo if yes return it makes the program much faster
        key = f"{m},{n}"
        if key in memo:
            return memo[key]

        # base case
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0

        memo[key] = self.travel(m, n-1, memo) + self.travel(m-1, n, memo)
        return memo[key]


res = Solution()
memo = {}
a = res.travel(29, 29, memo)
print(a)
