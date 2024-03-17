from datetime import datetime, timedelta

def index_max_value(arr):
    result = 0
    ref_max = 0
    
    for index in range(0, len(arr)):
        if arr[index] >= ref_max:
            ref_max = arr[index]
            result = index
            
    
    return result


def factorial(number):
    result = 1
    for n in range(number, 0, -1):
        result = result * n
    
    temp_string = str(result)
    
    result2 = []
    for num in temp_string:
        result2.append(int(num))

    counter_zero = 0
    
    for index in range(len(result2), 0, -1):
        if result2[index - 1] == 0:
            counter_zero += 1
        else:
            break
    
    return counter_zero

