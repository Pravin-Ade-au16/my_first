# https://leetcode.com/problems/peak-index-in-a-mountain-array/submissions/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # binary Search
        start = 0 # 0th index
        end = len(arr)
        while start < end:
            # middle of the
            mid = int(start + end/2)
            if arr[mid] < arr[mid-1]:
                end = mid
            elif arr[mid] < arr[mid + 1]:
                start = mid
            else:
                return mid
        return start

# output

# Accepted
# Runtime: 24 ms
# Your input
# [0,1,0]
# Output
# 1
# Expected
# 1