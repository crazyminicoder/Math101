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
