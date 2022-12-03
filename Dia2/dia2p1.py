# A --> rock
# B --> paper
# C --> scissors
dic = {"X" : "A", "Y" : "B", "Z" : "C"}
values = {"A" : 1,"B":2,"C":3}
value = 0
with open("input.txt","r") as f:
    for l in f:
        opponent = l.split(" ")[0]
        me = dic[l.split(" ")[1].replace("\n","")]
        
        value += values[me]
        if opponent == me:
            value += 3
        elif opponent == "A" and me =="C" or opponent == "B" and me == "A" or opponent =="C" and me =="B":
            pass
        else:
            value+=6
        
print(value)
    