# approach 1

def selection_sort(arr): # space complexity O(1)
    length = len(arr) # length of an array
    """
    traversing through all elements
    """
    for i in range(length): # time complexity O(n)
        min_elements = arr[i] # elements
        min_elements_index = i # index
        for index in range(i, len(arr)):
            if arr[index] < min_elements:
                min_elements = arr[index]
                min_elements_index = index
                """
                swap two elements
                """
                arr[i], arr[min_elements_index] = arr[min_elements_index], arr[i]
    return arr

arr = ["jay", "gor", "sewalal", "mariyamma", "samat", "dada"]
print(selection_sort(arr))

# approach 2

list = [8,45,2,0,5]

for i in range(len(list)):

    min_val = min(list[i:]) # 0-2nd iteration -1

    min_idx = list.index(min_val)# 5 1

    list[i],list[min_idx] = list[min_idx],list[i]
print(list)


