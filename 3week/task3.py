"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum-closest/description/
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = float("inf")

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(current_sum - target) < abs(result - target):
                    result = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum

        return result
