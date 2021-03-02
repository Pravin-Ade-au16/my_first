# link - https://leetcode.com/problems/pascals-triangle/submissions/
# source code
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tri = []

        for i in range(numRows):
            # 1st and last elements are always 1
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            # each element is equal to the sum of the elements
            for j in range(1, len(row) - 1):
                row[j] = tri[i - 1][j - 1] + tri[i - 1][j]

            tri.append(row)
        return tri

# output :Accepted
# Runtime: 40 ms
# Your input
# 5
# Output
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Expected
# [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]