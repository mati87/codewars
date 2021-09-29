lst= ['a']
   
def unique_in_order(iterable):
    new_lst=[]
    if len(iterable) == 1: # check if it's a one character string or a multi- character string
        string = iterable[0]
        lst_iterable = list(string)
        if len(lst_iterable) == 1:
            return lst_iterable
        else:
            iterable = lst_iterable
    else:                            # #else is a list of intergers
        iterable = iterable    
    
    for n, i in zip(iterable, iterable[1:]): ##use zip function to create two iterable objects and compare each pair of elements.
            print(n, i)                    
            if n != i:
                if n in new_lst:
                    if n != new_lst[-1]:
                        new_lst.append(n)  
                if n not in new_lst:
                    new_lst.append(n)              
                
                elif i not in new_lst:
                    new_lst.append(i)
            elif n == i:
                if n in new_lst:
                    if n != new_lst[-1]:
                        new_lst.append(n)
                elif n not in new_lst:
                    new_lst.append(n)    
    return new_lst
        
    
print(unique_in_order(lst))        
 

