#QUESTION 4
n_terms = 555555
approx = 0

for n in range(n_terms):
    approx += ((-1)**n)/(2*n+1)

print(approx*4)
