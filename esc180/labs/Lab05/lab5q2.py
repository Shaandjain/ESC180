def list_to_str(lis):
    result = '['  
    
    for i, num in enumerate(lis):
        if i == 0:
            result += str(num) 
        else:
            result += ', ' + str(num) 

    result += ']' 
    return result

print(list_to_str([1,2,3,4,5,6,7,8,9,10]))