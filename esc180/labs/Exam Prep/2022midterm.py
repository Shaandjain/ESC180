# # def matrix_sum(A,B):
# #     if len(A) != len(B) or len(A[0]) != len(B[0]):
# #         return "ERROR"
# #     C = [[0 for _ in range (len(A[0]))] for _ in range (len(A)) ]
# #     for i in range (len(A)):
# #         for j in range (len(A[0])):
# #             C[i][j] = A[i][j] + B[i][j]
# #     return C
# # A = [[1,0,0], [2,3,4]]
# # B = [[1,2,1], [1,2,2]]
# # print(matrix_sum(A,B))
                               
# # def get_perfect_squares(n):
# #     perfect_squares = []
# #     for i in range(1, n+1):
# #         if (i ** 0.5)%1 == 0:
# #             perfect_squares.append(i)
# #     return perfect_squares
# # print(get_perfect_squares(10))



# # def prod(L):
# #     p = 1
# #     for i in L:
# #         p*=i
# #     return p
# # print(prod([2,3,4]))


# # def duplicates(list0):
# #     for i in range(len(list0)-1):
# #         if list0[i] == list0[i+1]:
# #             return True
    
# # print(duplicates([1,2,2,3,4]))

# # # def psl():
# # #     sum = 0
# # #     while True:
# # #         order = input("What is your oder? ").lower()
# # #         if order == "pumpkin spice latte":
# # #             break
# # #         sum+= 1
# # #         print(sum)
# # # print(psl())

# # def matrix_sum (A, B):
# #     if len(A) != len(B) or len(A[0]) != len(B[0]):
# #         return "ERROR"
# #     C = [[0 for k in range(len(A[0]))] for k in range(len(A))]
# #     for i in range(len(A)):
# #         for j in range(len(A[0])):
# #             C[i][j] = A[i][j]+B[i][j]
# #     return C
# # A = [[1,0,0],[2,3,4]]
# # B = [[2,4,3],[1,0,2]]
# # print(matrix_sum(A,B))

# # import math
# # cur_digit = -1
# # def next_digit_pi():
# #     global cur_digit
# #     cur_digit  += 1
# #     return str(math.pi).replace(".","")[cur_digit]
# # print(next_digit_pi())
# # print(next_digit_pi())
# # print(next_digit_pi())
# # print(next_digit_pi())


# def halloween_reaction(thing):
#     if thing in ["ghost", "monster", "midterm"]:
#         return "NOOO!"
#     return "YAY!"
# print(halloween_reaction("Candy"))
# print(halloween_reaction("monster"))
        
# def print_mid_part(L):
#     for i in range(1, len(L)-1):
#         print(L[i])
# print(print_mid_part(["pumpkins", "candy", "costumes", "autumn", "zombies"]))

# def h(L):
#     L.clear()
#     L.append("Fall")
#     L.append("Colours")
    
# if __name__ == "__main__":
#     L = ["tricks", "treats"]
#     h(L)
#     print(L) #should print ["fall", "colours"]
    
# x = "Spice"
# y = "Pumpkin"
# x += x
# print(y+x, "Latte")

def odds_sum(L):
    odds = []
    sum = 0
    for i in L:
        if i %2 != 0:
            odds.append[i]
    sum = odds[i + (i+1)]
    return sum
print(odds_sum([1,3,4,5]))

        
def psl():
    count = 0
    while True:
        order = input("What is your order?")
        if order.lower() == "pumpkin spice latte":
            break
        count += 1
    return count
print(psl)