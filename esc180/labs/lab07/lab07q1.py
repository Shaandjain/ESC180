 #write a function to modify the list L, modifying both L[0] and L[0][0]
def modify(L):
    L[0] = [4,5,6]
    L[0][0] = 1
    return L
L = [[1,2,3],[4,5,6],[7,8,9]]
print(modify(L))
print(L)


def fake_modify(L):
    #change first row of L then print result without modifying global L
    L_copy = [row[:] for row in L]
    L_copy[0] = [4,5,6]
    print (L_copy)

L = [[1,2,3],[4,5,6],[7,8,9]]
fake_modify(L)
print(L)


def f():
    print("hi")
    print("hello")
    

