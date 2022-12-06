data = {}
with open("input.txt","r") as f:
    cont = 1
    phase2 = False
    for l in f:
        if l == "\n":
            phase2 = True
        elif not phase2:
            for i in range(len(l)):
                if l[i].isalpha():
                    num = int((i-1)/4) +1  
                    if num in data.keys():
                        data[num].insert(0,l[i])
                    else:
                        data[num] = [l[i]]
                
        else:
            _, cant, _, desde, _, to = l.split(" ")        
            newl = []
            for i in range(int(cant)):
                newl.insert(0,data[int(desde)].pop())
            
            for item in newl:
                data[int(to)].append(item)
  
str = ""
for i in sorted(data.keys()):
    str+=data[i][-1]

print(str)