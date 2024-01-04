#communications information to and from functions

def square(x):
    return x**2
#square(x) = x^2

#docstign: a description of what the function does 
#           enclosed in ''' '''
#           by convention, written in the imperative
def has_roots(a,b,c):
    '''Return True if ax^2+bx+c has root(s), and False otherwise'''

    #disc is a local variable, Think of it as scratch work. It is not accessible outside of the function
    disc = b**2-4*a*c
    if disc >= 0:
        return True
    else:
        return False

if __name__ == '__main__':
    print(square(5))
    print(has_roots(1,-2,1))
