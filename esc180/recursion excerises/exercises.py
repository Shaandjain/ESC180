def multiply(a,b):
    if a or b == 0:
        return 0
    else:
        return a + multiply(a,b-1)


def exponent(base, exp):
    if base == 1 or exp == 0:
        return 1
    else:
        return base * exponent(base, exp-1)
    
def print_nums(n):
    if n == 0:
        return
    else:
        print(n)
        print_nums(n-1)

def print_nums_reverse(n):
    if n == 0:
        return 0
    else:
        print_nums(n-1)
        print(n)



def reverse_string(string):
    if len(string) == 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if n % i == 0 and n != i and i != n:
        return False
    if i == n:
        return True
    return is_prime(n, i+1)



