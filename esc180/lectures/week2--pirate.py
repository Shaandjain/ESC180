def piratify_string(s):
    '''Return a piratified version of string s'''
    return "Ahoy!"+s+"Yarr!"

def pirate_print(s):
    '''Print the piratified version of s'''
    print(piratify_string(str(s)))

def print_x():
    global x
    print(x)

def set_x_to_43():
    global x
    x =43

if __name__ =='__main__':
    x = 42 #x is a global variable, defined outside of any function 
    print_x()
    set_x_to_43()
    print_x()
    print(x)
    #piratify_string("I LOVE PRAXIS <3")
    #print(piratify_string("I LOVE PRAXIS <3"))
    #pirate_print("PHY!")
    #pirate_print(42)
    #p1 = piratify_string("hi")
    #p2 = piratify_string("bye")