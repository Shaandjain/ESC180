M_sparse1 = {(1,2): 51, (0,0): 42}
M_sparse2 = {(1,2): 10, (0,1):12}

size = (2, 1000000)

def print_sparse_matrix(M_sparse, size):
    for row in range (size[0]):
        for col in range (size[1]):
            if (row,col) in M_sparse:
                print(M_sparse[(row,col)], end = "\t")
            else:
                print(0, end = "\t")
        print()

def add_sparse_matrices(M1, M2):
    sum = {}
    for coords in M1:
        sum[coords] = M1[coords] + M2.get(coords,0)
    for coords in M2:
        sum[coords] = M1.get(coords,0)+ M2[coords]