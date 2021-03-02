# link - https://leetcode.com/problems/trapping-rain-water/submissions/

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)  # for indexing

        total_water_trapped = 0  # initially zero

        for idx, h in enumerate(height):
            max_value_right = float("-inf")
            for i in range(idx + 1, n):
                if height[i] > max_value_right:
                    max_value_right = height[i]

            max_value_left = float("-inf")
            for i in range(0, idx):
                if height[i] > max_value_left:
                    max_value_left = height[i]

            water_trapped = min(max_value_right, max_value_left) - height[idx]
            if water_trapped > 0:
                total_water_trapped += water_trapped

        return total_water_trapped

# output _
# Accepted
# Runtime: 36 ms
# Your input
# [0,1,0,2,1,0,1,3,2,1,2,1]
# Output
# 6
# Expected
# 6



