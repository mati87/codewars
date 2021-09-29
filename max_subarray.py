lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
plus = 0
def max_sequence(array):
    total_lst = []
    plus = 0    
    if all(n == 0 for n in array) or all( n < 0 for n in array): #filtrate negative intergers and 0
        return 0
    else:           
        for i in range(len(array)): #iterate one time through each element. 
            for n in array[i:]: # Iterate from the first element onwards and append the sum
                plus+= n      
                total_lst.append(plus)         
            plus = 0
        max_sum = max(total_lst) #check wich is the biggest number
    return max_sum
    

print(max_sequence(lst))
