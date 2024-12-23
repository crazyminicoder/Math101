# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.


# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

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

    def findHappyNo(self, n):
        happyNumbers = []
        for i in range(1, n):
            temp = self.isHappy(i)
            if temp:
                happyNumbers.append(i)

        return happyNumbers


res = Solution()
ans = res.isHappy(19)
print(ans)

print(res.findHappyNo(100))
# Date: 14th October 2024
