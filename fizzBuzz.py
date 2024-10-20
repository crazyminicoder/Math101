class Solution:
    def fizzBuzz(self, n):
        fizzlist = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizzlist.append('FizzBuzz')
            elif i % 3 == 0:
                fizzlist.append('Fizz')
            elif i % 5 == 0:
                fizzlist.append('Buzz')
            else:
                fizzlist.append(str(i))

        return fizzlist


a = Solution()
res = a.fizzBuzz(15)
print(res)
