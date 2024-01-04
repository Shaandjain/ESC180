def get_repeating_ints(L):
    repeated = []
    for i in range (len(L)):
        if L[i] in L[i+1:] and L[i] not in repeated:
            repeated.append(L[i])
    return sorted(repeated)

# print(get_repeating_ints([6, 7, 6, 5, 1, 5, 6]))


def every_third(L):
    if len(L) < 3:
        return []
    return [L[2]] + every_third(L[3:])
    
# print(every_third([5, 6, 7, 12, 0, 4, 6]))


def add_sparse_matrices(A,B,dim):
    M = []
    for i in range(dim):
        row = []
        for j in range(dim):
            row.append(0)
        M.append(row)  # Add this line to append the row to M
    for i in range(len(M)):
        for j in range(len(M)):
            M[i][j] = A[i][j] + B[i][j]
    return M

A = [[5,0,0], [0,0,0], [0,0,0]]  # Define A as a matrix
B = [[0,0,1], [0,0,0], [0,0,0]]  # Define B as a matrix
dim = 3
print(add_sparse_matrices(A,B,dim))


