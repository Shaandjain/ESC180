def binary_search(L, e):
    low = 0
    high = len(L) - 1
    iterations = 0
    while high-low >= 2:
        iterations += 1
        mid = (low + high) // 2
        print(L[low], L[mid], L [high])
        if L[mid] > e:
            high = mid - 1
        elif L[mid] < e:
            low = mid + 1
        else:
            return mid, iterations
    if L[low] == e:
        return low, iterations
    elif L[high] == e:
        return high, iterations
    else:
        return None, iterations
    



# def create_list(e, size):
#     L = [i for i in range(e - size // 2, e + size // 2 + 1)]
#     return L

# e = 40
# size = 100
# L = create_list(e, size)
# print(binary_search(L, e))


def create_list(e,size):
    L = [i for i in range(e, size+e)]
    return L 


e = 1
size = 10
L = create_list(e, size)
print(L)
blank, iterations = binary_search(L, e)
print(f"size: {size}, iterations: {iterations}")




import time

def time_binary_search(e, size):
    L = create_list(e, size)
    start = time.time()
    blank, iterations = binary_search(L, e)
    end = time.time()
    return end - start, iterations

for size in [10, 100, 1000, 10000, 100000, 1000000]:
    time_taken, iterations = time_binary_search(1, size)
    print(f"size: {size}, time: {time_taken}, iterations: {iterations}")



