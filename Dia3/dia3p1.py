with open("input.txt","r") as f:
    sum = 0
    for l in f:
        act = 0
        line = l.replace("\n","")
       
        first = line[: int(len(line)/2)]
        second = line[int(len(line)/2):]
        
        
        for c in first:
            if c in second:
                if c.isupper():
                    if act < ord(c.lower()) - 96 + 26:
                        act = ord(c.lower()) - 96 + 26
                else:
                    if act < ord(c.lower()) - 96:
                        act = ord(c.lower()) - 96 
        
        sum+=act
    
print(sum)