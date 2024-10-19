class Solution:
    def isperfectsquare(self, n):
        if n == 1:
            return True
        res = 1
        i = 2
        while res <= n:
            res = i*i
            if res == n:
                return True
            i += 1

        return False


a = Solution()
print(a.isperfectsquare(17))
