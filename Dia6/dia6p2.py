with open("input.txt","r") as f:
    l = f.readline()
    arr = []
    for c in range(len(l)):
        ismark = True
        if len(arr) < 14: arr.append(l[c])
        else:
            arr.pop(0)
            arr.append(l[c])
        
            if len(set(arr)) != 14: ismark = False
            
            if ismark:
                print(c+1)
                break