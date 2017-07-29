n = 5
k = 3
arr_problems = [4, 2, 6 ,1 ,10]

# n,k = input().strip().split(' ')
# n,k = [int(n),int(k)]
# arr_problems = [int(temp) for temp in input().strip().split(' ')]

def count_special_problem(current_page,number_problems):
    steps = 1
    count_special = 0    
    page_index = current_page + 1
    while steps <= number_problems:
        if steps == page_index:
            #print ("page index %d and page number %d"%(page_index, steps))
            count_special +=1
        if  steps % k == 0:
            page_index += 1

        print ("page index %d"%(page_index))
        steps += 1

    page_in_chapter = (int)(number_problems / k)
    if number_problems % k != 0:
        page_in_chapter += 1

    #print ("number of page in chapter %d" % page_in_chapter)
    
    page = current_page + page_in_chapter

    #print ("end page %d" % page)
    
    return (count_special,page)
        
at_page = 0
special_page = 0
for index ,item in enumerate(arr_problems):
    #print("chapter %d" % (index + 1))
    tuple_special = count_special_problem(at_page,item)
    special_page += tuple_special[0]
    at_page = tuple_special[1]

print(special_page)



