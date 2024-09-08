# counting all prime numbers less then the given number
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = set()
        for i in range(2, n):
            if self.isPrime(i):
                prime.add(i)
        return len(prime)

    def isPrime(self, i):
        flag = 0
        if i < 2:
            return False
        for n in range(2, (i//2)+1):
            if i % n == 0:
                flag = 1
                break

        if flag == 1:
            return False
        else:
            return True


s = Solution()
res = s.countPrimes(50)
print(res)
