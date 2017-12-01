# sum
# returns the sum of array elements over a given axis

# import numpy

# my_array = numpy.array([[1, 2, 3], [3, 4, 5], [6,7,8]])

# print (numpy.sum(my_array, axis = 0))
# print (numpy.sum(my_array, axis = 1))
# print (numpy.sum(my_array)
# )

# prod
# return product of array elements over a given axis -> product element A * element B

# import numpy

# my_array = numpy.array([[1, 2], [3, 4]])

# print (numpy.prod(my_array, axis = 0))
# print (numpy.prod(my_array, axis = 1))
# print (numpy.prod(my_array, axis = None))

import numpy

n, m = input().split()
n, m = int(n), int(m)
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
    
sum_array = numpy.sum(array, axis = 0)
product_array = numpy.prod(sum_array)
print (sum_array, product_array, sep = '\n')