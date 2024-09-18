# Problem Explanation:
# Given a number, you need to continuously sum its digits until the result is a single digit.

# Example 1:
# Input: num = 38
# Process: 3 + 8 = 11, 1 + 1 = 2
# Output: 2

class Sum:
    def addDigite(self, num) -> int:
        sum = 0
        while num > 0:
            sum += num % 10
            num //= 10
        num = sum

        if num >= 10:
            return self.addDigite(num)
        else:
            return num


sol = Sum()
res = sol.addDigite(1234)
print('Result: ', res)
