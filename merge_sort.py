# approach 1

def merge2sort(A, B):
    empty_list = list()
    for i in A: # time complexity O(N log n)
        empty_list.append(i)
    for j in B:
        empty_list.append(j)

    empty_list.sort() # sort in ascending order
    return empty_list

A = [1,4,6,7,8,9]
B = [3, 5, 14, 18]
print(merge2sort(A,B))

# approach 2

def merge2sort(A, B):
    n = len(A) # length of A
    m = len(B) # length of B

    i = 0 # indexing for length of A
    j = 0 # indexing for length of B

    c = list()
    """Empty dictionary for merge two list"""
    while i < n and j < m: # as long as i is in n and j is in m
        if A[i] < B[j]:
            c.append(A[i])
            i += 1

        else:
            c.append(B[j])
            j += 1

    while i < n: # one of the pointer might not be complete
        c.append(A[i])
        i += 1

    while j < m:
        c.append(B[j])
        j += 1

    return c

A = [1,4,6,7,8,9]
B = [3, 5, 14, 18]
print(merge2sort(A, B))







