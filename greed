lst = [4, 4, 4, 3, 3]

def score(dice):
    triplets = 0
    dif = 0    
    ind_1 = 0
    ind_5 = 0
    if dice.count(6) >= 3:
        triplets = 600            
    if dice.count(4) >= 3:
        triplets = 400
    elif dice.count(3) >= 3:
        triplets = 300 
    elif dice.count(2) >= 3:
        triplets = 200

    elif dice.count(5) >= 3:
        triplets = 500        
        total_num = dice.count(5) - 3
        dif = total_num * 50    
    
    elif dice.count(1) >= 3:
        triplets = 1000
        total_num = dice.count(1) - 3
        dif = total_num * 100
    
    if dice.count(1) < 3:
        ind_1 = dice.count(1) * 100
    if dice.count(5) < 3:
        ind_5 = dice.count(5) * 50
        
    result = triplets + dif + ind_1 + ind_5
 
    return result    
    
    
  

print(score(lst))

