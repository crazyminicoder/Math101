class Solution:
    def base7(self, num):
        res = 0
        while num > 0:
            res *= 10
            res += num % 7
            num //= 7

        return res


s = Solution()
resu = s.base7(100)

print(resu)
