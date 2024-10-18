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

    def howSum(self, array, target):
        if target == 0:
            return []
        if target < 0:
            return None

        for num in array:
            res = target-num
            result = self.howSum(array, res)
            if result is not None:
                return result + [num]

        return None


res = Solution()
a = res.isSum([2, 7, 5, 4], 56)
print(a)
b = res.howSum([7, 5, 2, 4], 12)
print(b)
