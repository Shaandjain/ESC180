def sum_nums(L):
    s = 0
    for num in L:
        s += num
    return s
    

def count_evens(L):
    count = 0
    for num in L:
        if num%2 == 0:
            count += 1
    return count
print(count_evens([1,2,3,4,5,6,7,8,9,10]))


def list_to_str(lis):
    result = '['  
    
    for i, num in enumerate(lis):
        if i == 0:
            result += str(num) 
        else:
            result += ', ' + str(num) 

    result += ']' 
    return result

#print(list_to_str([1,2,3,4,5,6,7,8,9,10]))

def lists_are_the_same(list1, list2):
    if len(list1) != len(list2):
        return False
    else:
        for i, num in enumerate(list1):
            if num != list2[i]:
                return False
        return True
list1 = [1,2,3]
list2 = [1,2,4]
#print(lists_are_the_same(list1, list2))


def list1_start_with_list_2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range (len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

list1 = [1,2,3]
list2 = [1,2]
#print(list1_start_with_list_2(list1, list2))



def match_pattern (list1, list2):

    for i in range(len(list1)-len(list2)+1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3]
#print(match_pattern(list1, list2))


def duplicates(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False
list0 = [1,2,3,4,5,6,7,8,9,10]
#print(duplicates(list0))
list0=[1,2,2,3,4,5,6,]
#print(duplicates(list0))


