with open("input.txt","r") as f:
    values = []
    current = 0
    for l in f:
        if l == "\n":
            values.append(current)
            current = 0
        else:
            current += int(l)
values = sorted(values)
print(values[-1]+values[-2]+values[-3])   