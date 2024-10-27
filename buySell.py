class Solution:
    def buySell(self, prices):
        max = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                temp = abs(prices[i] - prices[j])
                if temp > max and prices[j] > prices[i]:
                    max = temp
                    print('i', prices[i])
                    print('j', prices[j])

        return max


a = Solution()
res = a.buySell([7, 6, 4, 3, 1])
print(res)
