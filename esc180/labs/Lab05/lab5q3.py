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
print(lists_are_the_same(list1, list2))
list1 = [1,2,3]
list2 = [1,2,3]
print(lists_are_the_same(list1, list2))

