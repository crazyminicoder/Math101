class Solution:
    def sortArray(self, nums):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        return nums


a = Solution()
res = a.sortArray([2, 0, 2, 1, 1, 0])
print(res)
