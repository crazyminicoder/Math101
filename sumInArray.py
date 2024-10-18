# Given an array of non negative numbers return is there a war to acheiving the sum
# eample Array[2,7,5,4] Target = 12
# There are many ways of getting the sum
# eg: 2+2+2+2+2+2+2+2+2+2+2+2= 12 or 7+5 = 12 given this return True if it is possible or else False

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
