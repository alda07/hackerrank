# 6
# 1 4 3 5 6 2
# Sample Output

# 1 4 3 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 2 3 4 5 6 


def insertion_sort(A):
    n = len(A)
    for j in range( 1, n):
        key = A[j]
        i = j 
        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            i -= 1
        A[i] = key
        print (" ".join(str(x) for x in array))


n = 6
array = [1,4,3,5,6,2]

insertion_sort(array)
