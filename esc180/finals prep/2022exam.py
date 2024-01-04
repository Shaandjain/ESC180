def get_repeating_ints(L):
    repeated = []
    for i in range(len(L)):
        if L[i] in L[i+1:] and L[i] not in repeated:
            repeated.append(L[i])
    return sorted(repeated)


def my_median(L):
    for i in range(len(L)):
        for j in range(len(L)-1):
            if L[j] > L[j+1]:
                L[j], L[j+1] = L[j+1], L[j]
    return L[len(L)//2]


#the time complexity for the function above is O(n^2) because of the nested for loop

def top10requests(requests):
    choice = {}
    for item in requests:
        if item in choice:
            choice[item] += 1
        else:
            choice[item] = 1
    top = []
    for item, choice in choice.items():
        top.append((choice, item))
    top.sort()
    vars = []
    for i in range (-1, -11, -1):
        vars.append(top[i][1])
    return sorted(vars)







def every_third(L):
    if len(L) < 3:
        return []
    else:
        return [L[2]] + every_third(L[3:])


def f(L):
    L = ["holidays"]
L = ["happy"]
f(L)
print(L)

#output will be "happy"
L = [[[1, 2], 3], [4]]
L1 = []
for sublist in L:
    L1.append(sublist[:])
L[0][0][0] = 5
L[0][1] = 5
L[1][0] = 5
print(L)
print(L1)
#output:
#[[[5, 2], 5], [5]]
#[[[5,2],3], [4]]
# a deep copy is created when you use the slice operator to copy a list

