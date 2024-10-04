class Solution:
    def containerArea(self, height):
        area = 0
        left = 0
        right = len(height)-1
        width = 0
        maxArea = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])
            area = width * current_height
            maxArea = max(maxArea, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea


res = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(res.containerArea(height))
