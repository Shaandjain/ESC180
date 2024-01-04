current_value = 25  # Initialize the current value as a global variable
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

def undo2():
    #undo the last 2 operations
    global current_value, value_history
    if len(value_history) >= 2:
        value_history.pop()
        current_value = value_history.pop()
    elif len(value_history) == 1:
        current_value = value_history.pop()
    else:
        print(None)

        
if __name__ == "__main__":
    print("Welcome to the calculator program.")
    display_current_value()

    add(5)
    display_current_value()

    mult(2)
    display_current_value()

    mult(3)
    display_current_value()

    add(2)
    display_current_value()

    undo2()  # Undo the last two operations
    display_current_value()  # Display the value after undo2

    undo()  # Undo the last operation again
    display_current_value()  # Display the value after undo


