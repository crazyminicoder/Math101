class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        nums1 = nums1[0:m]
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        print(nums1)


res = Solution()
n1 = [1, 2, 3, 0, 0, 0]
n2 = [2, 5, 6]

res.merge(n1, 3, n2, 3)
