#QUESTION 1 -- WARMUP
def my_sqrt(x):
    sqrt = x**0.5
    return sqrt

if __name__ == "__main__":
    res = my_sqrt(25)

#q1 PART A
#nothing was excuted to the screen due to the fact that there was no line of code which would print the result. In order to complete this, add the following line of code.
    print(res)


#q1 PART B
#print(res) would cause an error since 'sqr' is a local variable within the 'my_sqrt' function. This means that it is not accessible to call outside of the fucnction (in this case the main block).
#We can modify this by doing the following (return the function)


def my_sqrt(x):
    sqr = x**0.5
    return sqr

if __name__ == "__main__":
    res = my_sqrt(25)
    print(res)  # This will print the square root without error

#q1 PART C

def my_print_square(x):
    sqr = x**2
    print(sqr)

if __name__ == "__main__":
    my_print_square(25)
#this will call the 'my_print_square' funciton, which will return the square of 25 --> 625

#QUESTION 2 -- WELCOME MESSAGE
if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    print(f"Current value: {current_value}")

#QUESTION 3 -- DISPLAYING THE CURRENT VALUE

def display_current_value(current_value):
    print(f"Current Value: {current_value}")

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    current_value = 0
    display_current_value(current_value) #call the function

#QUESTION 4 -- ADDITION
current_value=0

def display_current_value():
    global current_value
    print(f"Current Value: {current_value}")

def add(to_add):
    global current_value
    current_value += to_add

if __name__ == "__main__":
    print("Welcome to the Calculator Program -- Addition")
    display_current_value()
#run test cases
    add(5)
    display_current_value()
    add(10)
    display_current_value()

#QUESTION 5 -- MULTIPLICATION

current_value=1

def display_current_value():
    global current_value
    print(f"Current Value: {current_value}")

def mult(to_mult):
    global current_value
    current_value*=to_mult

if __name__ == "__main__":
    print("Welcome to the Calculator Program -- Multiplication")
    display_current_value()

    mult(2)
    display_current_value()
    mult(4)
    display_current_value()


#QUESTION 6 -- DIVISION
current_value=4

def display_current_value():
    global current_value
    print(f"Current Value: {current_value}")

def div(to_div):
    global current_value
    if to_div == 0:
        print("You cannot divide by 0")
    else:
        current_value /= to_div

if __name__ == "__main__":
    print("Welcome to the Calculator Program -- DIVISION")
    display_current_value()

    div(0)
    display_current_value()
    div(2)
    display_current_value()


#the values which would cause to_div to have problems is 0. You cannot divide by 0, which will give this function a problem.


#QUESTION 7 -- MEMORY and RECALL


#First I will place all of the functions under one subsection

current_value = 0  # Initialize the current value as a global variable
memory_value = None  # Initialize the memory value

def display_current_value():
    global current_value  # Declare the global variable
    print(f"Current value: {current_value}")

def add(to_add):
    global current_value  # Declare the global variable
    current_value += to_add

def mult(to_mult):
    global current_value  # Declare the global variable
    current_value *= to_mult

def div(to_div):
    global current_value  # Declare the global variable
    if to_div == 0:
        print("You cannot divide by 0")
    else:
        current_value /= to_div

def memory_store(): #This will save the value
    global current_value, memory_value  # Declare global variables
    memory_value = current_value

def memory_recall(): #This will recall the saved value
    global current_value, memory_value
    if memory_value is not None:
        current_value = memory_value

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    display_current_value()  # Display the initial current value

    add(5)  # Add to the current value
    display_current_value()

    memory_store()  # Store the current value in memory
    display_current_value()

    mult(3)  # Multiply the current value by 3
    display_current_value()

    memory_recall()  # Recall the stored value from memory
    display_current_value()

    div(2)  # Divide the current value by 2
    display_current_value()

    memory_recall()  # Recall the stored value from memory again
    display_current_value()


#QUESTION 8 -- UNDO
current_value = 25  # Initialize the current value as a global variable
memory_value = None  # Initialize the memory value
value_history = [] # create a stack to store the previous values created

def display_current_value():
    global current_value  # Declare the global variable
    print(f"Current value: {current_value}")

def add(to_add):
    global current_value, value_history #  Declare the global variables
    value_history.append(current_value) #add the current value to the stack
    current_value += to_add

def mult(to_mult):
    global current_value, value_history # Declare the global variables
    value_history.append(current_value) #add the current value to the stack
    current_value *= to_mult

def div(to_div):
    global current_value, value_history  # Declare the global variables
    if to_div == 0:
        print("You cannot divide by 0")
    else:
        value_history.append(current_value) #add the current value to the stack
        current_value /= to_div

def undo():
    global current_value, value_history #Declare global variables
    if value_history:
        current_value = value_history.pop()

if __name__ == "__main__":
    print("Welcome to the calculator program.")
    display_current_value()

    add(5)
    display_current_value()

    mult(2)
    display_current_value()

    undo()  # Undo the last operation
    display_current_value()  # Display the value after undo

    undo()  # Undo the last operation again
    display_current_value()  # Display the value after undo

