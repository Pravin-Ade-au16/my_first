# insertion sort

size = int(input("Enter size of an array:"))
"""
input from end user for size of an array 
"""
my_list = [] # Empty list
for i in range(size):
    val = int(input("Enter values:"))
    """
    val variable which nothing but elements of list which is append by end user one by one using append()
    in my_list which is initially empty until size of the array.
    """
    my_list.append(val)
    # print(my_list)
for i in range(1, size):
    temp = my_list[i]
    cmp = i-1
    while cmp>=0 and temp<my_list[cmp]:
        """
        if cmp is grater than zero or zero and temp is less than cmp
        """
        my_list[cmp+1] = my_list[cmp]
        cmp = cmp - 1
    my_list[cmp+1] = temp

print("Sorted array is:")
print(my_list)







