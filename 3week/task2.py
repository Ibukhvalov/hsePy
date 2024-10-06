"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if not (i > 0 and nums[i] == nums[i - 1]):
                j = i + 1
                k = len(nums) - 1

                while j < k:
                    sum = nums[i] + nums[j] + nums[k]

                    if sum > 0:
                        k -= 1
                    elif sum < 0:
                        j += 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1

                        while nums[j] == nums[j - 1] and j < k:
                            j += 1

        return res
