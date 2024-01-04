import math

def sigfigs(n):
    approx_terms = 0
    pi = int(math.pi * (10 ** (n-1)))
    approximation = 0
    while int(4*approximation * (10 ** (n-1))) != pi:
        approx_terms += 1
        approximation += ((-1) ** (approx_terms - 1)) / (2 * approx_terms - 1)
    return approx_terms

print(sigfigs(3))
    


