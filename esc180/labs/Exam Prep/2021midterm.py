for i in range (100,201):
    if i % 2 == 0:
        print(i)

for i in range(1,11):
    if i % 2 == 0:
        print(i)

def last_ind(L, e):
    for i in range(len(L)-1,-1,-1):
        if L[i] == e:
            return i
    return None
L = [1,4,2,3]
print(last_ind(L, 3))


a = int(input())
b = int(input())
c = int(input())
d = int(input())
n = max(a,b,c,d)

while True:
    if n % a == 0 and n%b == 0 and n%c == 0 and n%d == 0:
        break
    n += 1
print (n)




