class Solution:
    def fact(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fact(n-1)

    def trailingZeroes(self, n: int) -> int:
        res = self.fact(n)
        temp = res
        count = 0
        while temp > 0:
            div = temp % 10
            if div == 0:
                count += 1
            if div != 0:
                break
            temp //= 10

        return count


s = Solution()
a = s.trailingZeroes(25)
print(a)
