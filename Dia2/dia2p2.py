# A --> rock
# B --> paper
# C --> scissors
winners = {"A" : "B", "B" : "C", "C" : "A"}
losers = {"B" : "A", "C" : "B", "A" : "C"}
values = {"A" : 1,"B":2,"C":3}
value = 0
with open("input.txt","r") as f:
    for l in f:
        opponent = l.split(" ")[0]
        me = l.split(" ")[1].replace("\n","")
        
        if "X" == me:
            value += 0 + values[losers[opponent]]
        elif "Y" == me:
            value += 3 + values[opponent]
        else:
            value+=6 + values[winners[opponent]]
            

print(value)