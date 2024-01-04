def lookup(L, num):
    for i in range(len(L)):
        if L[i][1] == num:
            return L[i][0]
    return None

L = [["CIV", 92], 
    ["180", 98], 
    ["103", 99], 
    ["194", 95]]
print(lookup(L, 95))
print(lookup(L, 100))
