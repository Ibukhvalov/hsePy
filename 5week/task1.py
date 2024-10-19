"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        result = 0
        left = 0
        right = len(height) - 1

        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return result
