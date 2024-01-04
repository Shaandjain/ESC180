#Question 3
def initialize():
    global too_much_coffee #declare global variables
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols

    too_much_coffee = False
    current_time = 0
    knols = 0
    last_coffee_time = -100
    last_coffee_time2 = -100

#if the student drinks more than 2 coffees within 2 hours, it is too_much_coffee
def drink_coffee():
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols

    if current_time - last_coffee_time2 <= 120:
        too_much_coffee = True
    else:
        last_coffee_time2 = last_coffee_time
        last_coffee_time = current_time

#when the student drinks coffee right before a study session, they get 10 knols per minute. if it is too much coffee, they get 0 knols per minute. If they don't drink coffee before, it is 5 knols per minute
def study(minutes):
    global too_much_coffee
    global current_time
    global last_coffee_time
    global last_coffee_time2
    global knols

    if too_much_coffee == False:
        if current_time == last_coffee_time:
            knols += 10*minutes
        else:
            knols += 5*minutes
    
    current_time += minutes


initialize()
if __name__ == '__main__':
    initialize() # start the simulation
    study(60) # knols = 300
    print(knols)
    study(20) # knols = 400
    print(knols) 
    drink_coffee() # knols = 400
    study(10) # knols = 500
    print(knols)
    drink_coffee() # knols = 500
    study(10) # knols = 600
    print(knols)
    drink_coffee() # knols = 600, 3rd coffee in 20 minutes
    study(10) # knols = 600
    print(knols)