# Method 1

# import re
# def is_palindrome(phrase):
#     forward = "".join(re.findall(r'[a-z]+',phrase.lower()))
#     backward = forward[::-1]
#     return forward == backward
# a = input("String:",)
# s = (is_palindrome(a))
# print("string:", s)

# Bu using inbuilt method
my_string = input("Enter the string to check:")
""" 
taking input from end user
"""
forward = list(my_string)
""" 
convert string into list
"""
reverse = list(reversed(my_string))
"""
convert string to list and Reverse the list 
"""
if forward == reverse:
    """
    compare forward and reverse variable by using equality operator 
    """
    print("This is palindrome")
else:
    print("This is not a palindrome")