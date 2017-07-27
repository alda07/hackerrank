# import sys


# n,t = raw_input().strip().split(' ')
# n,t = [int(n),int(t)]
# width = map(int,raw_input().strip().split(' '))
# for a0 in xrange(t):
#     i,j = raw_input().strip().split(' ')
#     i,j = [int(i),int(j)]


# 8 5
# 2 3 1 2 3 2 3 3
# 0 3
# 4 6
# 6 7
# 3 5
# 0 7

def find_numer_of_vihicle(from_index,to_index,arr_width):
    i = from_index
    min_vihicles = arr_width[from_index]
    while i <= to_index:
        min_vihicles = min(min_vihicles,arr_width[i])
        print (min_vihicles)
        i += 1
    return min_vihicles

width = [2, 3, 1 ,2 ,3 ,2 ,3, 3]
print (find_numer_of_vihicle(0,3,width))