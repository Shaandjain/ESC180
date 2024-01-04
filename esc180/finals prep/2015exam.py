# def is_sorted(L):
#     ascending = True
#     descending = True
#     for i in range(1, len(L)):
#         if L[i] < L[i-1]:
#             ascending = False
#         if L[i] > L[i-1]:
#             descending = False
#     return ascending or descending

# print(is_sorted([4, 5, 6, 7, 8, 2]))
# print(is_sorted([4, 5, 5, 6]) )

# #O(n)

def euc_distance(u, v):
    sum = 0
    distance = 0
    for i in u:
        if i in v:
            sum += (u[i]-v[i])**2
        else:
            sum += (u[i])**2

    for i in v:
        if i not in u:
            sum += (v[i])**2


    distance += sum**0.5
    return distance

# print(euc_distance({2: 1, 4: 2, 5: 3}, {6: 1, 4: 2, 7: 3}))


# def merge(L1, L2):
#     if L1 == []:
#         return L2
#     elif L2 == []:
#         return L1
#     elif L1[0] < L2[0]:
#         return [L1[0]] + merge(L1[1:], L2)
#     else:
#         return [L2[0]] + merge(L1, L2[1:])

# print(merge([4, 8, 10], [2, 5]))





def luckiest_kid(haul_dataset):
    count = {}
    for house, housedet in haul_dataset.items():
        for child in housedet:
            if child not in count:
                count[child] = 1
            else:
                count[child] += 1
    max = 0
    for child, num in count.items():
        if num > max:
            max = num
            lucky = child
    return lucky

halloween_haul = {"house1": {"Annie": ["snickers", "mars"],
"Johnny": ["snickers"] },
"house2": {"Annie": ["coffee break", "mars"],
"Jackie":["coffee break"]}}

print(luckiest_kid(halloween_haul))

def movies_by_release_date(movies):
    for movie in movies:
        if "a long time ago" in movies[movie]:
            movies[movie] = -9999
        else:
            movies[movie] = int(movies[movie][:4])
    return sorted(movies, key=movies.get, reverse=True)

movies = {"Dude, Where’s My Death Star": "a long time ago, in a galaxy far far away",
"Star Wars: The Force Awakens": "2015, in Los Angeles",
"Star Wars": "1977, in Los Angbeles",
"Sleepless in Aldera": "a long time ago, in Alderaan City",
"Jurassic World": "2015, in New York"}
print(movies_by_release_date(movies))


def is_sorted (L):
    ascending = True
    descending = True
    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            ascending = False
        if L[i] > L[i-1]:
            descending = False
    return ascending or descending


def merge(L1, L2):
    if L1 == []:
        return L2
    elif L2 == []:
        return L1
    elif L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    elif L1[0] > L2[0]:
        return [L2[0]] + merge(L2[1:], L1)

print(merge([4, 8, 10], [2, 5]))
    