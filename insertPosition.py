class Solution:
    def searchIndex(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i

        return len(nums)


s = Solution()

res = s.searchIndex([-1, 3, 5, 6], -2)
print(res)
