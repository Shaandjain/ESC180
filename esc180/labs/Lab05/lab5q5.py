def match_pattern (list1, list2):

    for i in range(len(list1)-len(list2)+1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3]
print(match_pattern(list1, list2))

