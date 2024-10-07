class Solution:
    def sum3(self, nums):
        nums.sort()
        finalSet = set()
        sum = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    # print('i', nums[i], 'j', nums[j], 'k', nums[k])
                    # if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    sum = nums[i]+nums[j]+nums[k]
                    # print('sum ', sum)
                    if sum == 0:
                        finalSet.add((nums[i], nums[j], nums[k]))
                        # print('finalSet', finalSet)
        finalList = [list(triplet) for triplet in finalSet]
        return finalList


res = Solution()
a = res.sum3([5, -9, -11, 9, 9, -4, 14, 10, -11, 1, -13, 11, 10, 14, -3, -3, -4, 6, -15, 6, 6, -13, 7, -11, -15, 10, -8, 13, -14, -12, 12, 6, -6, 8, 0, 10, -11, -8, -2, -6, 8, 0, 12, 3, -9, -6, 8, 3, -15, 0, -6, -1,
             3, 9, -5, -5, 4, 2, -15, -3, 5, 13, -11, 7, 6, -4, 2, 11, -5, 7, 12, -11, -15, 1, -1, -9, 10, -8, 1, 2, 8, 11, -14, -4, -3, -12, -2, 8, 5, -1, -9, -4, -3, -13, -12, -12, -10, -3, 6, 1, 12, 3, -3, 12, 11, 11, 10])
print(a)
