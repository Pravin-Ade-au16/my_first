# return count in vowels

# def isVowel(ch):
#     return ch.upper() in ["A", "E", "I", "O", "U"]
# def cnt_vow(str):
#     count = 0
#     for i in range(len(str)):
#         if isVowel(str[i]):
#             count += 1
#     return count
#
# str = "JAY SEWALAL"
# print(cnt_vow(str))
#
# fibonacci
#
# def fibonacci(num):
#     if num < 0:
#         print("incorrect input")
#
#     elif num == 1:
#         return 0
#
#     elif num == 2:
#         return 1
#
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
#
# print(fibonacci(9))
#
# string count
# s = "need more practice"
# def str_cnt(str):
#     if s == 0:
#         return 0
#     else :
#         return 1 + str_cnt(s[1:])
# print(str_cnt(s))
#
# def rec_sum(num):
#     if num <= 1:
#         return num
#     else:
#         return num + rec_sum(sum-1)
# nums = 16
# print(rec_sum(nums))

# def recur_sum(n):
#    if n <= 1:
#        return n
#    else:
#        return n + recur_sum(n-1)
# n = 10
# print(recur_sum(n))

# change this value for a different result
# num = 20
# if num < 0:
#    print("Enter a positive number")
# else:

# print("The sum is",recur_sum(num))

# data = {1:"Ade", 2:"Pravin", 3:"Tulshiram"}

# import heapq
#
# if __name__=="__main__":
#     heapq.heappush(heap,10)

### write a program to find sum of 1st n even number fromone to num
num = int(input("Enter number:"))
i = 1
sum = 0
count = 0
while i <= num:
  if i%2 == 0:
      sum = sum + i
      count = count + 1
  i += 1

print("sum of even numbers:", sum)




