# /#link - https://leetcode.com/problems/min-stack/submissions/
#
# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#         self.min = []
#         self.size = 0
#
#     def push(self, x: int) -> None:
#         if self.size == 0:
#             self.min.append(x)
#
#         else:
#             if x <= self.min[-1]:
#                 self.min.append(x)
#
#         self.stack.append(x)
#         self.size += 1
#
#     def pop(self) -> None:
#         temp = self.stack.pop()
#         self.size -= 1
#         if temp == self.min[-1]:
#             self.min.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         return self.min[-1]
#
# # Your MinStack object will be instantiated and called as such:
# # obj = MinStack()
# # obj.push(x)
# # obj.pop()
# # param_3 = obj.top()
# # param_4 = obj.getMin()3
#
# # Accepted
# # Runtime: 44 ms
# # Your input
# # ["MinStack","push","push","push","getMin","pop","top","getMin"]
# # [[],[-2],[0],[-3],[],[],[],[]]
# # Output
# # [null,null,null,null,-3,null,0,-2]
# # Expected
# # [null,null,null,null,-3,null,0,-2]

# n = int(input("enter:"))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
#     print("  "*(n-i), "* "*(2*i-1))


