cont = 0
with open("input.txt","r") as f:
    for l in f:
        first, second = l.strip("\n").split(",")
        first = first.split("-")
        second = second.split("-")

        if (int(first[0]) >= int(second[0]) and int(first[1]) <= int(second[1])) or (int(second[0]) >= int(first[0]) and int(second[1]) <= int(first[1])):
            cont+=1
print(cont)