# approach 1

def bubble_sort(arr): # no extra space O(1)
    # n = len(arr) # length of array
    """ traversing through all elements """
    for i in range(len(arr)):
        #for j in range(0, n-1): # time complexity O(n**2)
        for j in range(i):
            """ comparing two adjacent elements"""
            if arr[j] > arr[j+1]:
                """ swapping the elements"""
                # temp = arr[j]
                # arr[j] = arr[j+1]
                # arr[j+1] =temp

                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
arr = [1,5,3,2,7]
print(bubble_sort(arr))


# approach 2
def bubble_sort(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            """
            compare two adjacent elements
            """
            if num[j] > num[j+1]:
                """ swapping  """
                temp = num[j]
                num[j] = num[j+1]
                num[j+1] = temp

num = [8,7,52,4,6,0] # len - 6
print(bubble_sort(num))
num.sort()
print((num))

# approach 3

def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(0, n-i-1): # i already sorted
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j] # swap two adjacent elements


arr = [64,34,25,12,55,11,90]
bubble_sort(arr)
print(arr)
