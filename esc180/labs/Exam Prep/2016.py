# def odds_sum(L):
#     sum = 0
#     for i in range(len(L)):
#         if L[i] %2 != 0:
#             sum += L[i]
#     return sum
# print(odds_sum([1,2,3,4,5]))


# i = 5
# while i < 500:
#     print(i)
#     i += 3

# def halloween_surprise():
#     n = 3
#     while n > 0:
#         print(n)
#         n -= 1
#     print("surprise!")


# def has_single_peak(L):
#     peak = False
#     for i in range(len(L)-1):
#         if L[i] > L[i+1]:
#             peak = True
#         if peak and L[i] < L[i+1]:
#             return False
#     return True
           



# print(has_single_peak([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
# print(has_single_peak([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,13,12,11,10,9,8,7,6,5,4,3,2,1]))
# print(has_single_peak([1,2,3,2,3,1]))


def max_arrivals_2hrs(arrivals):
    max_count = 0

    for i in range(len(arrivals)):
        for j in range(len(arrivals)):
            if arrivals[j] -arrivals[i]<120:
                max_count = max(max_count, j-i+1)
    return max_count

print(max_arrivals_2hrs([0,30,40,150,160,170,370]))

        
        
def psl():
    count = 0
    while True:
        order = input("What is your order?")
        print(order)
        if order.lower() == "pumpkin spice latte":
            break
        count += 1
    print (count)

if __name__ == "__main__":
    psl()