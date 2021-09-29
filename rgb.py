def rgb(r, g, b):
    if r < 0:
        r = 0
    elif r > 255:
        r = 255
    if g < 0:
        g = 0
    elif g > 255:
        g = 255
    if b < 0 :
        b = 0
    elif b > 255:
        b = 255
    new_lst = []
    rgb = (r,g,b)
    for num in rgb:
        num = hex(num)
        num = num[-2:]
        if num[-1] == '0' or num[-2] =='x':
            num = num.replace('x','0')
            num = num[-2:]       
        new_lst.append(num)    
        result = "".join(new_lst)
    return result.upper()
print(rgb(0,0,0))