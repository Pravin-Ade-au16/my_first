# # simple calculator
# def add(x, y):
#     return x+y
#
# def sub(x,y):
#     return x-y
#
# def mul(x, y):
#     return x*y
#
# def div(x, y):
#     return x/y
#
# print("select opration:")
# print("1. addition")
# print("2. subtraction")
# print("3. multiplication")
# print("4. Division")
#
# while True:
#     # take input from users
#     choice = int(input("Enter Choice (1/2/3/4): "))
#     # if choice is one of the four option
#     if choice in ("1", "2", "3", "4"):
#         num_1 = float(input("Enter 1st number: "))
#         num_2 = float(input("Enter 2nd number: "))
#
#         if choice == "1":
#             print(num_1, "+", num_2, "=", add(num_1, num_2) )
#         elif choice == "2":
#             print(num_1, "-", num_2, "=", sub(num_1, num_2))
#         elif choice == "3":
#             print(num_1, "*", num_2, "=", mul(num_1, num_2))
#         elif choice == "4":
#             print(num_1, "/", num_2, "=", div(num_1, num_2))
#         break
#     else:
#         print("invalid input")

def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select Operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")