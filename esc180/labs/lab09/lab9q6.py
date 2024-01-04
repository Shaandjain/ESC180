
import numpy as np

# Convert a list of lists into an array:
M_listoflists = [[1,-2,3],[3,10,1],[1,5,3]]
M = np.array(M_listoflists)
# Now print it:
# print(M)

M_listoflists = M.tolist() 

def print_matrix(M_lol):
    M = np.array(M_lol)
    print(M)

def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return None

def eliminate(M, row_to_sub, best_lead_ind):
    for i in range(row_to_sub+1, len(M)):
        if M[row_to_sub][best_lead_ind] != 0:
            coef = -M[i][best_lead_ind]/M[row_to_sub][best_lead_ind]
            # print(f'Adding {coef} times row {row_to_sub} to row {i}')
            M[i] = add_rows_coefs(M[row_to_sub], coef, M[i], 1)
    return M

def add_rows_coefs(r1, c1, r2, c2): 
    new_list = [0 for i in range(len(r1))]
    for i in range(len(r1)):
        new_list[i] = c1 * r1[i] + c2 * r2[i]
    return new_list

def get_row_to_swap(M, start_i):
    swap_row = start_i
    smallest_lead_ind = get_lead_ind(M[start_i])
    for i in range(start_i, len(M)):
        if get_lead_ind(M[i]) < smallest_lead_ind:
            smallest_lead_ind = get_lead_ind(M[i])
            swap_row = i
    return swap_row

def swap_rows(M, row1, row2):
    M[row1], M[row2] = M[row2], M[row1]
    return M

def forward_step(M):
    print("Starting matrix:")
    print_matrix(M)

    for i in range(len(M)):
        
        print("Now looking at row", i)
        lead_ind = get_lead_ind(M[i])
        row_to_swap = get_row_to_swap(M, i)
        print("Swapping rows", i, "and", row_to_swap, "so that entry", lead_ind, "in the current row is non-zero")
        swap_rows(M, i, row_to_swap)
        print("The matrix is currently:")
        print_matrix(M)

        print("Adding row", i, "to rows below it to eliminate coefficients in column", lead_ind)
        M = eliminate(M, i, lead_ind)

        print("The matrix is currently:")
        print_matrix(M)

    print("Done with the forward step")
    print("The matrix is currently:")
    print_matrix(M)
    return M


M = [[0., 0., 1., 0., 2.],
     [1., 0., 2., 3., 4.],
     [3., 0., 4., 2., 1.],
     [1., 0., 1., 1., 2.]]
print(forward_step(M))
