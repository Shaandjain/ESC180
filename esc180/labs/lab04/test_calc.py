import lab02
if __name__ == '__main__':
    lab02.initialize()
    lab02.add(42)
    if lab02.get_current_value() == 42:
        print("Test 1 passed")
    else:  
        print("Test 1 failed")  

    lab02.subtract(7)
    if lab02.get_current_value() == 35:
        print("Test 2 passed")
    else:   
        print("Test 2 failed")  

    lab02.multiply(2)
    if lab02.get_current_value() == 70:
        print("Test 3 passed")  
    else:   
        print("Test 3 failed")  

