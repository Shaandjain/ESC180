n_terms = 555555
approx = 0

for n in range(n_terms):
    approx += ((-1)**n)/(2*n+1)

print(approx*4)

n = 0
approx = 0
while n < n_terms:
    approx += ((-1)**n)/(2*n+1)
    n += 1
print(approx*4)





def gcd(n,m):
    if n == 0:
        return m
    if m == 0:
        return n
    if n > m:
        return gcd(n-m,m)
    else:
        return gcd(n,m-n)
print(gcd(28,12))    


def gcd(n,m):
    i = n
    while i>0:
        if n%i == 0 and m%i == 0:
            return i
        else:
            i -= 1
print(gcd(28,12))

