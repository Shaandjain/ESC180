def sum_cubes(k):
    sum = 0
    for i in range(1, k+1):
        sum += i**3
    return sum
print(sum_cubes(2))

def sum_cubes_num_terms(n):
    sum = 0
    k = 1
    while sum <n:
        sum += k**3
        if sum < n:
            k+=1
    return k
print(sum_cubes_num_terms(10))


x = [1,2,3,4,5,6,7,8,9,10]

mp = filter(lambda i: i%2 == 0, x)
print(list(mp))


