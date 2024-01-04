def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return None

def get_row_to_swap(M, start_i):
    min_index = len(M[start_i])

    for i in range(start_i+1, len(M)):
        index = get_lead_ind(M[i])
        if index <= min_index:
            min_index = index
            swap = i
    return swap

M = [[5,6,7,8], [0,0,0,1], [0,0,5,2], [0,1,0,0]]
start_i = 1

print(get_row_to_swap(M, start_i))