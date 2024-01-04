def list1_start_with_list_2(list1, list2):
    if len(list1) < len(list2):
        return False
    for i in range (len(list2)):
        if list1[i] != list2[i]:
            return False
    return True

list1 = [1,2,3]
list2 = [1,2]
print(list1_start_with_list_2(list1, list2))
