def most_productive_elf(toys_produced):
    max_toys = max(toys_produced.values())
    max_elf = ""
    for elf, toys in toys_produced.items():
        if toys == max_toys:
            max_elf = elf
    return max_elf

def mostprodelf(toys_produced):
    return sorted(toys_produced, key = toys_produced.get, reverse = True)[0]

# toys0 = {"Bob":4000, "Gloria":7000, "Hugo":6000, "Grumbles":42}
# print(most_productive_elf(toys0))

def two_smallest(L):
    small = sorted(L)[:2]
    small[0], small[1] = small[1], small[0]
    return small

# print(two_smallest([5, 3, 10, 4]))


def largest_col_sum(M):
    sums = []
    for i in range(len(M[0])):
        sum = 0
        for j in range(len(M)):
            sum += M[j][i]
        sums.append(sum)
    return max(sums)

M0 = [[1, 2, 3, 4], [5, 0, 5, 0], [6, 7, 8, 9]]
print(largest_col_sum(M0))


def filter_out_odds(L):
    if len(L) == 0:
        return []

    if L[0] % 2 == 0:
        return ([L[0]] + filter_out_odds(L[1:]))
    else:
        return filter_out_odds(L[1:])

print(filter_out_odds([5, -2, 4, 0, 3, 7, 8]) )

def largest_col_sum(M):
    sums = []
    for i in range(len(M[0])):
        sum = 0
        for j in range(len(M)):
            sum += M[j][i]
        sums.append(sum)
    return max(sums)

M0 = [[1, 2, 3, 4], [5, 0, 5, 0], [6, 7, 8, 9]]
print(largest_col_sum(M0))
