class Solution:
    def isSum(self, array, target):
        if target == 0:
            return True
        if target < 0:
            return False

        for num in array:
            res = target-num
            if self.isSum(array, res):
                return True

        return False


res = Solution()
a = res.isSum([2, 7, 5, 4], 56)
print(a)
