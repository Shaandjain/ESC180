def get_nums(L):
    nums = []
    for i in range(len(L)):
        nums.append(L[i][1])
    return nums

L = [["CIV", 92],
     ["180", 98], 
     ["103", 99],
     ["194", 95]]
print(get_nums(L))