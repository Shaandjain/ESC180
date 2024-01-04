def duplicates(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False
list0 = [1,2,3,4,5,6,7,8,9,10]
print(duplicates(list0))
list0=[1,2,2,3,4,5,6,]
print(duplicates(list0))