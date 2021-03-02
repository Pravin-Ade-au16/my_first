# stack data structure
# work on push and pop are two main
# FILO or LIFO First in last out ot last in first out

def push(my_stack, val):
    my_stack.append(val)
    print("Push item successfully...")

def popitem(my_stack):
    store = my_stack.pop()
    print("Item poped:", store)

def peekitem(my_stack):
    idx = len(my_stack)-1
    print("Peek item is:", idx[my_stack]) # index suppose len of my_stack is 4 then 4-1 = 3 python follow 0th idx

def display_all_items(my_stack):
    for i in range(len(my_stack)-1, -1, -1):
        print(my_stack[i])

my_stack = [] # empty stack
while True:
    choice = int(input("1 - Push\n2 - Pop\n3 - Peek\n4 - Exit\n5 - Display\nEnter yur choice: "))
    if choice == 1:
        val = int(input("Enter push value: "))

    elif choice == 2:
        if len(my_stack) == 0:
            print("Stack underflow")
        else:
            popitem(my_stack)

    elif choice == 3:
        if len(my_stack) == 0:
            print("Stack underflow")
        else:
            peekitem(my_stack)

    elif choice == 4:
        if len(my_stack) == 0:
            print("Stack underflow")
        else:
            display_all_items(my_stack)
    else:
        break