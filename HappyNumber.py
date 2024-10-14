class Solution:
    def sumSquare(self, n):
        totalSum = 0
        while n > 0:
            digit = n % 10
            totalSum += digit**2
            n //= 10

        # print('in sum function:', sum)
        return totalSum

    def isHappy(self, n):
        seen = set()
        totalSum = n
        while totalSum != 1:
            if totalSum in seen:
                return False
            seen.add(totalSum)
            totalSum = self.sumSquare(totalSum)

        return True


res = Solution()
ans = res.isHappy(19)
print(ans)
