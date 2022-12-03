with open("input.txt","r") as f:
    max = 0
    current = 0
    for l in f:
        if l == "\n":
            if current > max:
                max = current
            current = 0
        else:
            current += int(l)
print(max)
    