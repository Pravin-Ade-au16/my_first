# Binary Search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ two variable to store 1st and last index"""
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2
            # return mid

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right = mid - 1

            else:
                left = mid + 1

        return None