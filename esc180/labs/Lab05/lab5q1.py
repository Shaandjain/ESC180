def count_evens(L):
    count = 0
    for num in L:
        if num%2 == 0:
            count += 1
    return count
print(count_evens([1,2,3,4,5,6,7,8,9,10]))

