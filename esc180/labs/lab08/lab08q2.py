L = open("/Users/shaanjain/Downloads/ENGSCI/FIRST YEAR/SEM 1/esc180/labs/lab08/text.txt", encoding = "latin-1").read().split()


def word_count(L):
    D = {}
    for word in L:
        if word in D:
            D[word] += 1
        else:
            D[word] = 1
    return D
 


# def ten_largest(L):
#     sorted_L = sorted(L)
#     top_ten = sorted_L[-10:]
#     return top_ten


# L = []
# for i in range(100):
#     L.append(i)
    
# print(ten_largest(L))


def top_ten_words(L):
    D = word_count(L)
    sorted_D = sorted(D.items(), key=lambda x: x[1], reverse=True)
    top_ten = [word for word in sorted_D[:10]]
    return top_ten

print(top_ten_words(L))

f = lambda x: 2 * x 
f(8)

