def add_rows_coefs(r1, c1, r2, c2):
    new_list = [[0] * len(r1), [0] * len(r2)]
    for i in range(len(r1)):
        new_list[0][i] = c1 * r1[i]
        new_list[1][i] = c2 * r2[i]
    return new_list

print(add_rows_coefs([1, 1, 1], 2, [1, 1, 1], 3))
