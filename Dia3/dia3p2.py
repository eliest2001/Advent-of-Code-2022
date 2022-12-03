with open("input.txt","r") as f:
    sum = 0
    cont = 0
    first =""
    second =""
    third = ""
    for l in f:
        cont+=1
        act = 0
        line = l.replace("\n","")
        if cont == 1:
            first = line
        elif cont == 2:
            second = line
        elif cont == 3:
            third = line
        
            for c in first:
                if c in second:
                    if c in third:
                        if c.isupper():
                            if act < ord(c.lower()) - 96 + 26:
                                act = ord(c.lower()) - 96 + 26
                        else:
                            if act < ord(c.lower()) - 96:
                                act = ord(c.lower()) - 96 
        
            sum+=act
            cont = 0
        
    
print(sum)