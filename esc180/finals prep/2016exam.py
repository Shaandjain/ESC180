def insert(L, e):
    return sorted(L + [e])

print(insert([3.0, 4.0, 5.0], 3.5))

#time complexity of O(n)


def select_gifts(good_ratings, want_ratings):
    combined_ratings = {}
    for gift in good_ratings:
        combined_ratings[gift] = good_ratings[gift]
    for gift in want_ratings:
        if gift in combined_ratings:
            combined_ratings[gift] += want_ratings[gift]
        else:
            combined_ratings[gift] = want_ratings[gift]
    max_rating = max(combined_ratings.values())
    top_gifts = [gift for gift, rating in combined_ratings.items() if rating == max_rating]
    return sorted(top_gifts)

# good_ratings = {"Calc textbook": 5, "iPhone": 1, "Alarm clock": 4, "Notebooks": 4}
# want_ratings = {"iPhone": 4, "A+ in CSC": 5, "Calc textbook": 4, "Notebooks": 5}
# print(select_gifts(good_ratings, want_ratings))

def transpose(M):
    transposed = []
    for i in range(len(M[0])):
        row = []
        for j in range(len(M)):
            row.append(M[j][i])
        transposed.append(row)
    return transposed



def maxrec(L):
    if len(L) == 1:
        return L[0]
    if len(L) == 0:
        return []
    max = maxrec(L[1:])

    if L[0] > max:
        return L[0]
    else:
        return max

def is_fib(L):
    if len(L) <= 2:
        return True
    else:
        return L[0] + L[1] == L[2] and is_fib(L[1:])












def sorted_timestamps(timestamps):
    d = {}
    sorted_times = []
    answer = []
    for hour, minute in timestamps:
        time = hour*60 + minute
        d[time] = (hour, minute)
        sorted_times.append(time)
    sorted_times.sort()

    for time in sorted_times:
        answer.append(d[time])
        
    return answer
        
    

def max_clique(friends):
    max_clique = []
    for dude in friends:
        clique = [dude]
        for friend in friends[dude]:
            if friend in friends:
                clique.append(friend)
        if len(clique) > len(max_clique):
            max_clique = clique
    return max_clique

friends = {"Carl Gauss": ["Isaac Newton", "Gottfried Leibniz", "Charles Babbage"],
"Gottfried Leibniz": ["Carl Gauss"],
"Isaac Newton": ["Carl Gauss", "Charles Babbage"],
"Ada Lovelace": ["Charles Babbage", "Michael Faraday"],
"Charles Babbage": ["Isaac Newton", "Carl Gauss", "Ada Lovelace"],
"Michael Faraday": ["Ada Lovelace"]}

print(max_clique(friends))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(binary_search(arr, target))
