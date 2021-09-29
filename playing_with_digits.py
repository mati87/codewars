
def dig_pow(n,p):
    numbers_lst = [ int(digits) for digits in str(n)] #convert number into single digits  list.
    count = p
    total_lst = [] 

    for number in numbers_lst:    #iterate over each digit and perform each digit to the power, append each result into a new list
        expon = number ** count
        count +=1 
        total_lst.append(expon)
    
    result = sum(total_lst) #get the total
    k = result // n # find out the value of k        
    check_float_k = isinstance(k, float) #check if k is float

    if check_float_k == True:
        return -1

    elif k * n == result: #compare and return k
        return k
    else:
        return -1


print(dig_pow(89, 1))